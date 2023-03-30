import cv2
import os

path = os.getcwd()

def take_photo(name : str):
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        raise 'cannot open camera'
        exit(1)
    while True:
        ret, frame = cap.read()

        if not ret:
         raise "can't receive frame(stream end?)"
    
        cv2.imshow('frame', frame)
    
        if cv2.waitkey(1)==ord('q'):
            cv2.inwrite(name,frame)##aqui lo guardamos 
            break

    cap.release()

def save_photo(name: str, frame):    #creamos la carpeta
    dir_photo = os.path.join(path,'photos',name)
    photo_name = os.path.join(dir_photo,name + '.png')
    if not os.path.exists(dir_photo):
        os.mkdir(dir_photo)
    cv2.inwrite(photo_name,frame)

