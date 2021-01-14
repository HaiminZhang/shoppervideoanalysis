import csv
import cv2
import os
import shutil
import glob
import pdb

from myutils import draw_rectangle, draw_circle

from myutils import extract_frame


rt_csvfolder = './csiro/redbullandv'

csvfiles = glob.glob(os.path.join(rt_csvfolder, '*.csv'))
csvfiles = sorted(csvfiles)

for fn in csvfiles:
    extract_frame(fn)

#pdb.set_trace()

#csv_path = './csiro/redbullandv/11.csv'
#extract_frame(csv_path)


