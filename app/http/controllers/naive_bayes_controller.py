class NaiveBayesController:
    @staticmethod
    def dataset(data: dict):
        """
        Procesa el dataset recibido
        """
        features = data.get('features', [])
        labels = data.get('labels', [])
        
        # Aquí puedes agregar tu lógica de Naive Bayes
        num_samples = len(features)
        num_features = len(features[0]) if features else 0
        unique_labels = len(set(labels)) if labels else 0
        
        return {
            "message": "Dataset procesado exitosamente",
            "status": "success",
            "data": {
                "samples": num_samples,
                "features": num_features,
                "classes": unique_labels,
                "received_features": features,
                "received_labels": labels
            }
        }
