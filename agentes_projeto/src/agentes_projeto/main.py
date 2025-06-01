#!/usr/bin/env python
import sys
import warnings
from typing import List, Dict, Any
from ultralytics import YOLO
import cv2
import os
from datetime import datetime
from pathlib import Path
from agentes_projeto.crew import AgentesProjeto

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd") 

def train_model():
    model = YOLO("yolov8n.pt")   
    data_path = Path(r"C:\Users\DELL\Documents\projeto_sistemas_multiagentes\dataset.yaml")
    results = model.train( 
        data=data_path,
        epochs=1,
        name="train_pole_fiber" )
    

    return str(Path(results.save_dir) / "weights" / "best.pt")


def analyze_image(image_path_train, image_path_test) -> List[Dict[str, Any]]:
    
        
        model = YOLO(image_path_train)  
        
        image = cv2.imread(image_path_test)
        results = model.predict(image, stream=False) 
        
        detections = []
        for result in results:
            for box in result.boxes:
                detections.append({
                        'class': model.names[int(box.cls)],
                        'confidence': float(box.conf),
                        'bbox': box.xyxy[0].tolist()
                })
        return detections

def run():
    """
    Run the crew.
    """
    inputs = {
        'detections': analyze_image(train_model(), r"C:\Users\DELL\Documents\projeto_sistemas_multiagentes\dataset\images\train\poste_fibra02.jpg"),
    }
    
    try:
        AgentesProjeto().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        'detections': analyze_image(train_model(),r'C:\\Users\\DELL\\Documents\\projeto_sistemas_multiagentes\\dataset\\images\\train\\', 'C:\\Users\\DELL\\Documents\\projeto_sistemas_multiagentes\\dataset\\images\\val\\poste_fibra01.jpg'),
    }
    try:
        AgentesProjeto().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        AgentesProjeto().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        'detections': analyze_image(train_model(), r'C:\\Users\\DELL\\Documents\\projeto_sistemas_multiagentes\\dataset\\images\\train\\', 'C:\\Users\\DELL\\Documents\\projeto_sistemas_multiagentes\\dataset\\images\\val\\poste_fibra01.jpg'),
    }
    
    try:
        AgentesProjeto().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
