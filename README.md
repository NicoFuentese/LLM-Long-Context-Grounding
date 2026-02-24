# LLM-Long-Context-Grounding

## Estructura del Proyecto

```powershell
notebooklm_clone/
├── .env                    # (Ya lo creaste) Credenciales estáticas de AWS
├── .gitignore              # Archivo crítico para no subir el .env
├── requirements.txt        # Dependencias del proyecto
├── Dockerfile              # Instrucciones para el contenedor
├── app.py                  # Punto de entrada de la UI (Streamlit)
└── src/                    # Lógica interna de la aplicación
    ├── __init__.py         # Archivo vacío. Indica a Python que 'src' es un módulo
    ├── document_processor.py # Extracción de PDF/TXT y formateo XML jerárquico
    └── bedrock_client.py   # Invocación a Claude 4.6 y configuración de Prompt Caching```
```

## Correr la aplicacion

```powershell
docker run -p 8501:8501 --env-file .env mi-app-notebooklm
```