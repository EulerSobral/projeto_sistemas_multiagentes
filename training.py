from ultralytics import YOLO
import cv2

# para marcar as imagens
# https://www.makesense.ai/

def main(): 
    image_path = 'C:\Users\DELL\Documents\projeto_sistemas_multiagentes\dataset\images\val\projeto_fibra01.jpg'
    model = YOLO("yolov8n.pt")  
    model.train(data="dataset.yaml", epochs=30)  #
    metrics = model('projeto_fibra01.jpg') 
    
    detecoes = []
    for box in metrics.boxes:
        classe = metrics.names[int(box.cls)]
        conf = float(box.conf)
        bbox = box.xyxy.tolist()[0]
        detecoes.append((classe, conf, bbox))


if __name__ == '__main__':
    main()