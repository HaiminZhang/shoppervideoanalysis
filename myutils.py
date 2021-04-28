import csv
import cv2
import os
import pdb

def draw_rectangle(img, cnt_point, thickness=3):
    
    output = img.copy()

    p1 = (cnt_point[0]-50, cnt_point[1]-50)
    p2 = (cnt_point[0]+50, cnt_point[1]+50)

    output = cv2.rectangle(output, p1, p2, (0, 255, 0), thickness)

    return output


def draw_circle(img, pnt, radius=50, thickness=3):

    output = img.copy()

    output = cv2.circle(output, pnt, radius, (0,0,255), thickness)

    return output

    

def extract_frame(csv_path, rt_videos='./videos', rt_dst = './fixation_frames'):
    #csv_path = './csiro/redbullandv/11.csv'
    #rt_videos = './videos'
    #rt_fixation = './fixation_frames'

    print('---- processing csv file ', csv_path)


    with open(csv_path) as fd:
        reader = csv.reader(fd)

        for idx, row in enumerate(reader):
            if idx == 0:
                # skip the first row
                continue

            vidname = row[12]
            path_video = os.path.join(rt_videos, vidname)
            if not os.path.exists(path_video):
                print('video does not exist ', path_video)
                print('csv file ', csv_path)
                return


            if idx == 1:
                cap = cv2.VideoCapture(path_video)
                assert(cap.get(5) == 25)

            seq = int(row[5])
            cap.set(1, seq)
            ret, frame = cap.read()


            fn = '_%06d.png' %seq
            fn = vidname + fn 

            cv2.imwrite(os.path.join(rt_fixation, fn), frame)

        #pdb.set_trace()


def extract_from_baycsv(csv_path, rt_videos='./videos', rt_dst = './dst_frames'):
    #csv_path = './csiro/redbullandv/11.csv'
    #rt_videos = './videos'
    #rt_fixation = './fixation_frames'

    print('---- processing csv file ', csv_path)
    if not os.path.exists(rt_dst):
        #pdb.set_trace()
        os.mkdirs(rt_dst)

    with open(csv_path) as fd:
        reader = csv.reader(fd)

        for idx, row in enumerate(reader):
            if idx == 0:
                # skip the first row
                continue

            vidname = row[12]
            path_video = os.path.join(rt_videos, vidname)
            if not os.path.exists(path_video):
                print('video does not exist ', path_video)
                print('csv file ', csv_path)
                return

            if idx >= 1:
                cap = cv2.VideoCapture(path_video)
                assert(cap.get(5) == 25)

            seq = int(row[5])
            cap.set(1, seq)
            ret, frame = cap.read()


            fn = '_%06d.png' %seq
            fn = vidname + fn 

            cv2.imwrite(os.path.join(rt_dst, fn), frame)

#extract_frame('')
