import cv2
import imutils
import numpy as np
import tkinter as tk
from tkinter import filedialog

# Trained model for human detection
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())


# Detect human in a frame and make a rectangular box around them
def detect(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    bounding_box_coordinates, weights = hog.detectMultiScale(gray, winStride=(9, 9), padding=(2, 2), scale=1.03)

    person = 1
    for x, y, w, h in bounding_box_coordinates:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)
        cv2.putText(frame, f'Person {person}', (x, y - 7), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        person += 1

    cv2.putText(frame, 'Status : Detecting ', (20, 20), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255, 0, 0), 2)
    cv2.putText(frame, f'Total Persons : {person - 1}', (20, 50), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255, 0, 0), 2)
    cv2.imshow('Output', frame)


# Detect human in an image
def detectInImage():
    path = filedialog.askopenfilename(initialdir="/", title="Select File",
                                      filetypes=(('JPG (*.jpg;*.jpeg)', ('*.jpg', '*.jpeg')),
                                                 ('GIF (*.gif)', '*.gif'), ('PNG (*.png)', '*.png'),
                                                 ('All Images Files', ('*.jpg', '*.jpeg', '*.gif', '*.png'))))
    img = cv2.imread(path)
    img = imutils.resize(img, width=min(800, img.shape[1]))
    detect(img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Detect human in a video    
def detectInVideo():
    path = filedialog.askopenfilename(initialdir="/", title="Select File",
                                      filetypes=(('MP4 Video File (*mp4)', '*.mp4'),
                                                 ('MKV Video File (*.mkv)', '*.mkv'), ('All Files', '*.*')))
    video = cv2.VideoCapture(path)

    while True:
        isTrue, frame = video.read()
        frame = imutils.resize(frame, width=min(800, frame.shape[1]))
        detect(frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()


# Detect human in a live video through webcam    
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


# GUI design for input selection    
def gui():
    root = tk.Tk()
    root.title('Human Recogniser & Tracker')
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
    imageButton.place(relwidth=0.7, relheight=0.13, relx=0.15, rely=0.5)

    videoButton = tk.Button(frame, text="Video", fg='black', bg='#C5C0C0', font=('', 20), command=detectInVideo)
    videoButton.place(relwidth=0.7, relheight=0.13, relx=0.15, rely=0.65)

    cameraButton = tk.Button(frame, text="Camera", fg='black', bg='#C5C0C0', font=('', 20), command=detectInCamera)
    cameraButton.place(relwidth=0.7, relheight=0.13, relx=0.15, rely=0.8)

    root.mainloop()


# Start of program
if __name__ == "__main__":
    gui()
