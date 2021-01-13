import csv
import cv2
import os
import shutil
import pdb

from mytuils import draw_rectangle, draw_circle


vid_path = './videos/Recording001_Participant001_00.00.00-00.45.16.mp4'
csv_path = './csiro/rawfixation/P1.csv'


basename = os.path.basename(vid_path)
vidname = os.path.splitext(basename)[0]

_frm_dir = os.path.join('fixation_frames', vidname)

if os.path.exists(_frm_dir):
    shutil.rmtree(_frm_dir) 
os.mkdir(_frm_dir)




cap = cv2.VideoCapture(vid_path)
assert(cap.get(5) == 25)

with open(csv_path) as fd:
    reader = csv.reader(fd)

    for idx, row in enumerate(reader):
        if idx == 0:
            # skip the first row
            continue


        #if idx < 5000:
        #    continue
        #if idx > 5010:
        #    break

        if idx % 100 == 0:
            print('---- processing idx ', idx)
        #print(idx, row)

        if idx % 2 == 0:
            #print('idx ', idx)
            continue
        
        stamp = row[2] 
        seq = int(int(stamp)/40)

        cap.set(1, seq)
        ret, frame = cap.read()

        #print('row[3]', row[3], row[4], idx)

        
        move_type = row[5]
        if move_type == 'Saccade':
            gx = int(row[3])
            gy = int(row[4])
            #fn = 'frm_%06d.jpg' %seq
            fn = '_%06d.jpg' %seq
            fn = vidname + fn 
            output = draw_circle(frame, (gx, gy))
            #cv2.imwrite(os.path.join(_frm_dir, fn), output)

        elif move_type == 'Unclassified':
            pass
        elif move_type == 'Fixation':
            gx = int(row[3])
            gy = int(row[4])

            fx = int(row[8])
            fy = int(row[9])

            ##output = draw_rectangle(frame, (gx, gy))
            ##output = draw_circle(output, (fx, fy))

            output = frame
            #output = draw_circle(frame, (gx, gy))
            #output = draw_rectangle(output, (fx, fy))

            #fn = 'frm_%06d.jpg' %seq
            fn = '_%06d.jpg' %seq
            fn = vidname + fn 

            cv2.imwrite(os.path.join(_frm_dir, fn), output)
            #pdb.set_trace()
        else:
            pass
            #print('-------- move_type ', move_type)
            #pdb.set_trace()



