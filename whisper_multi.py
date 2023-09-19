import openai
import tkinter as tk
from tkinter import filedialog, messagebox
import os

# Establece tu clave de API
openai.api_key = 'sk-...'

def seleccionar_archivos():
    filenames = filedialog.askopenfilenames(filetypes=[("Audio files", "*.mp3 *.wav *.M4A")])
    if filenames:
        transcribir_audios(filenames)

def transcribir_audios(filenames):
    for filename in filenames:
        # Obtiene el directorio del archivo original (subcarpeta "Audios")
        audios_directory = os.path.dirname(filename)

        # Sube un nivel para obtener el directorio donde se desea crear la carpeta "Transcripciones"
        parent_directory = os.path.dirname(audios_directory)

        # Crea una carpeta "Transcripciones" si no existe en el directorio padre
        transcriptions_dir = os.path.join(parent_directory, "Transcripciones")
        os.makedirs(transcriptions_dir, exist_ok=True)

        with open(filename, "rb") as audio_file:
            transcription = openai.Audio.transcribe("whisper-1", audio_file)
        texto = transcription.get('text')

        # Modifica el nombre del archivo para que tenga el formato nombre_archivo_transcript.txt
        nuevo_nombre_base = os.path.splitext(os.path.basename(filename))[0] + "_transcript.txt"
        nuevo_nombre = os.path.join(transcriptions_dir, nuevo_nombre_base)

        with open(nuevo_nombre, 'w', encoding='utf-8') as f:
            f.write(texto)

    messagebox.showinfo("Transcripciones completas", "Los archivos de texto se guardaron en la carpeta Transcripciones del directorio original.")

root = tk.Tk()
root.title("Transcriptor de Audio")
root.geometry("300x200")  # Configura el tamaño de la ventana

frame = tk.Frame(root)  # Crea un marco para contener el botón
frame.pack(fill=tk.X, padx=50, pady=50)  # Agrega un poco de espacio alrededor del botón

button = tk.Button(frame, text="SELECCIONAR ARCHIVOS", command=seleccionar_archivos)
button.pack()

root.mainloop()
