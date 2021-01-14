import csv
import cv2
import os
import shutil
import pdb

from myutils import draw_rectangle, draw_circle

from myutils import extract_frame


csv_path = './csiro/redbullandv/11.csv'
extract_frame(csv_path)


