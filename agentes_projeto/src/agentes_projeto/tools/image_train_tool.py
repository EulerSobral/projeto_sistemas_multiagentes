# tools/image_train_tool.py
from crewai.tools import tool 
from ultralytics import YOLO
from pathlib import Path 
import cv2  

@tool
def ImageTrain(name: str, epochs: int = 10,  model_arch: str = "yolov8n.pt") -> str: 
    """Treina um modelo YOLOv8 com as imagens especificadas no arquivo dataset YAML.""" 
    data_yaml = Path(__file__).resolve().parent.parent / "dataset.yaml" 
    image_path_train = Path(__file__).resolve().parent.parent / "dataset" / "images" / "train" 
    image_path_test = Path(__file__).resolve().parent.parent / "dataset" / "images" / "train" / "poste_fibra01.jpg"
    if not Path(data_yaml).exists():
        return f"O arquivo {data_yaml} não existe" 
 
    
    if not Path(image_path_test).exists(): 
        return f"O arquivo {image_path_test} não existe" 

    try:
        model = YOLO(model_arch)
        results = model.train(
            data=str(data_yaml),
            epochs=epochs,
            name=name
        ) 

        results_model_path = f"runs/detect/{name}/weights/best.pt"

        train_model = YOLO(str(results_model_path))  
        
        image = cv2.imread(str(image_path_test))
        results = train_model.predict(image, stream=False) 
        
        detections = []
        for result in results:
            for box in result.boxes:
                detections.append({
                        'class': model.names[int(box.cls)],
                        'confidence': float(box.conf),
                        'bbox': box.xyxy[0].tolist()
                })
        return detections
    except Exception as e:
        return f"Erro no treinamento: {e}"


