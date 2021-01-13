import cv2
import pdb

def get_frame_count(cap):
    
    return cap.get(7)

def read_frame(cap, index):

    #frame_no = 2 / cap.get(7)

    cap.set(2, 1)

    ret, frame = cap.read()
    
    pdb.set_trace()

    return frame



