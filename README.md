
# Transcriptor de Audio

Un script simple y fácil de usar para transcribir archivos de audio a texto usando la API de OpenAI.

## Requisitos

- Python 3.x
- Biblioteca `openai`
- Biblioteca `tkinter`

Para instalar las dependencias necesarias, use el siguiente comando:

```bash
pip install openai
```

## Configuración

Antes de ejecutar el script, establezca su clave de API de OpenAI en la variable `openai.api_key`.

## Uso

Ejecuta el script usando un intérprete de Python:

```bash
python whisper_multi.py
```

Una vez ejecutado, aparecerá una ventana con un botón que dice "SELECCIONAR ARCHIVOS". Al hacer clic en él, podrás seleccionar múltiples archivos de audio para transcribir. Los archivos transcritos se guardarán con un nuevo nombre y extensión `.txt` en una carpeta llamada "Transcripciones" ubicada en el mismo directorio donde estaban los archivos de audio originales.


![Captura de pantalla 2023-09-19 000730](https://github.com/HonroAvisp/Auido_Texto/assets/73007200/f6e3320e-6fc4-4d0e-b743-c4255c8b4f80)

### Salida
![Captura de pantalla 2023-09-19 000946](https://github.com/HonroAvisp/Auido_Texto/assets/73007200/e71b8749-1845-42f1-b6bc-ab04ed9a2685)


## Limitaciones

- Por el momento, solo es compatible con archivos de formato `.mp3`, `.wav` y `.m4a`.
- Asegúrate de que tu clave de API tenga suficientes permisos y cuota para realizar transcripciones de audio.

## Contribuciones

Si deseas contribuir al proyecto, ¡siéntete libre de hacer un Pull Request!

## Licencia

Este proyecto está bajo una licencia MIT.
