from pydantic import BaseModel, Field
from typing import List, Union

class DatasetRequest(BaseModel):
    """
    Esquema para el request del dataset de Naive Bayes
    """
    features: List[List[Union[int, float]]] = Field(
        ..., 
        description="Lista de características del dataset",
        example=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    )
    labels: List[Union[int, str]] = Field(
        ..., 
        description="Lista de etiquetas correspondientes a las características",
        example=[0, 1, 0]
    )
    
    class Config:
        schema_extra = {
            "example": {
                "features": [
                    [1, 2, 3],
                    [4, 5, 6], 
                    [7, 8, 9]
                ],
                "labels": [0, 1, 0]
            }
        }

class DatasetResponse(BaseModel):
    """
    Esquema para la respuesta del procesamiento del dataset
    """
    message: str = Field(..., description="Mensaje de respuesta")
    status: str = Field(..., description="Estado del procesamiento")
    data: dict = Field(None, description="Datos procesados del modelo")
    
    class Config:
        schema_extra = {
            "example": {
                "message": "Dataset procesado exitosamente",
                "status": "success",
                "data": {
                    "samples": 3,
                    "features": 3,
                    "classes": 2
                }
            }
        }