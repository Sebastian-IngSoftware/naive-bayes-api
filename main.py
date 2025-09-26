from fastapi import FastAPI
from routes.web import router

app = FastAPI(
    title="Naive Bayes API",
    description="""
    ## API para modelo de Naive Bayes
    
    Esta API permite procesar datasets para entrenar y usar modelos Naive Bayes.
    
    ### Características principales:
    * **Dataset Processing**: Procesa datasets con características y etiquetas
    * **Documentación interactiva**: Prueba los endpoints directamente desde aquí
    * **Validación automática**: Los datos se validan automáticamente
    
    ### Cómo usar:
    1. Ve al endpoint `/dataset`
    2. Haz clic en "Try it out"
    3. Modifica el JSON de ejemplo con tus datos
    4. Ejecuta la petición
    """,
    version="1.0.0",
    contact={
        "name": "Sebastian",
        "email": "sebastian@example.com",
    },
    license_info={
        "name": "MIT",
    },
)

app.include_router(router, tags=["Naive Bayes"])
