
from fastapi import APIRouter
from app.http.controllers.home_controller import HomeController
from app.http.controllers.naive_bayes_controller import NaiveBayesController
from app.schemas.dataset_schema import DatasetRequest, DatasetResponse

router = APIRouter()

@router.get("/", 
    summary="Página de inicio",
    description="Endpoint de prueba que retorna un mensaje de bienvenida",
    response_description="Mensaje de bienvenida exitoso"
)
def read_root():
    return HomeController.index()

@router.post("/dataset",
    summary="Procesar dataset para Naive Bayes",
    description="Recibe un dataset con características y etiquetas para procesamiento con Naive Bayes",
    response_model=DatasetResponse,
    response_description="Resultado del procesamiento del dataset"
)
async def dataset(request: DatasetRequest):
    """
    Procesa un dataset para el modelo Naive Bayes.
    
    - **features**: Lista de listas con las características de cada muestra
    - **labels**: Lista con las etiquetas correspondientes a cada muestra
    
    Ejemplo de request body:
    ```json
    {
        "features": [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        "labels": [0, 1, 0]
    }
    ```
    """
    return NaiveBayesController.dataset(request.dict())
