
import cv2
from pathlib import Path

data_path = 'data/'
PATH = data_path + "train.mp4"
vidcap = cv2.VideoCapture(str(PATH))
success, image = vidcap.read()

count = 0
while success:
    cv2.imwrite("train-frames/frame%d.jpg" % count, image)
    success, image = vidcap.read()
    count += 1

assert count == 20400

count = 0
vidcap = cv2.VideoCapture('data/test.mp4')
success, image = vidcap.read()

while success:
    cv2.imwrite("test-frames/frame%d.jpg" % count, image)
    success, image = vidcap.read()
    count += 1

