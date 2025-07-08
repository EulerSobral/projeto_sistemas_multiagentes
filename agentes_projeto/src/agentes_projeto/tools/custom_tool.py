from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field 
from pathlib import Path
from ultralytics import YOLO
import cv2  

class ImageTrain(BaseTool):  
    name: str="Ferramenta de treino de imagens" 
    description: str=("Estruda e treina datasets de imagens")

    def __init__(self, data_yaml: str, name: str,epochs: int = 10, model_arch: str="yolov8n.pt"): 
            self.data_yaml = data_yaml 
            self.name = name
            self.epochs = epochs 
            self.model_arch = model_arch 

    def run(self) -> str:
        if not Path.exists(self.data_yaml): 
            return f"O arquivo {self.data_yaml} não existe"
        
        try:
            model = YOLO(self.model_arch) 
            results = model.train( 
                data=self.data_yaml, 
                epochs=self.epochs, 
                name = self.name
            ) 
            return f" Treinamento bem sucessido{results}" 
        except Exception as e: 
            return f"treinamento com erro: {e}"
