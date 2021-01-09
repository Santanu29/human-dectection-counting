import cv2
import imutils
import numpy as np
import tkinter as tk
from tkinter import filedialog


HOGCV = cv2.HOGDescriptor()
HOGCV.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())


def detect(frame):
    bounding_box_cordinates, weights = HOGCV.detectMultiScale(frame, winStride=(4, 4), padding=(8, 8), scale=1.03)

    person = 1
    for x, y, w, h in bounding_box_cordinates:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)
        cv2.putText(frame, f'Person {person}', (x, y-7), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        person += 1

    cv2.putText(frame, 'Status : Detecting ', (20, 20), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255, 0, 0), 2)
    cv2.putText(frame, f'Total Persons : {person - 1}', (20, 50), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255, 0, 0), 2)
    cv2.imshow('Output', frame)

    # return frame

def detectInImage():
    path = filedialog.askopenfilename(initialdir="/", title="Select File",
                                      filetypes=(('JPG (*.jpg;*.jpeg)',('*.jpg','*.jpeg')),
                                                 ('GIF (*.gif)','*.gif'), ('PNG (*.png)','*.png'),
                                                 ('All Images Files', ('*.jpg','*.jpeg','*.gif','*.png'))))
    img = cv2.imread(path)
    img = imutils.resize(img, width=min(800, img.shape[1]))
    detect(img)
    # cv2.imshow('Detected Image', detected)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

def detectInVideo():
    path = filedialog.askopenfilename(initialdir="/", title="Select File",
                                      filetypes=(('MP4 Video File (*mp4)','*.mp4'),
                                                 ('MKV Video File (*.mkv)','*.mkv'),('All Files','*.*')))
    video = cv2.VideoCapture(path)

    while True:
        isTrue, frame = video.read()
        frame = imutils.resize(frame, width=min(800, frame.shape[1]))
        # cv2.imshow("Video", frame)
        detect(frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()

def detectInCamera():
    live = cv2.VideoCapture(0)

    while True:
        isTrue, frame = live.read()
        cv2.imshow('Camera', frame)
        detect(frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    live.release()
    cv2.destroyAllWindows()

def gui():
    root = tk.Tk()
    root.title('Human Regoniser & Tracker')
    root.iconbitmap(r'icon.ico')

    canvas = tk.Canvas(root, height=500, width=670, bg='#94A2FF')
    canvas.pack()

    frame = tk.Frame(canvas, bg='#CEE6F3')
    frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

    text = tk.Label(frame, bg='white', font=('', 12),
                    text='INSTRUCTIONS\n\nThis is a human recogniser and can detect a human and track them.\n'
                         'Choose the option for detection in Image, Video & Camera')
    text.place(relwidth=0.9, relheight=0.3, relx=0.05, rely=0.1)

    imageButton = tk.Button(frame, text="Image", fg='black', bg='#C5C0C0', font=('', 20), command=detectInImage)
    # imageButton.pack()
    imageButton.place(relwidth=0.7, relheight=0.13, relx=0.15, rely=0.5)

    videoButton = tk.Button(frame, text="Video", fg='black', bg='#C5C0C0', font=('', 20), command=detectInVideo)
    # videoButton.pack()
    videoButton.place(relwidth=0.7, relheight=0.13, relx=0.15, rely=0.65)

    cameraButton = tk.Button(frame, text="Camera", fg='black', bg='#C5C0C0', font=('', 20), command=detectInCamera)
    # videoButton.pack()
    cameraButton.place(relwidth=0.7, relheight=0.13, relx=0.15, rely=0.8)

    root.mainloop()


if __name__=="__main__":
    gui()






