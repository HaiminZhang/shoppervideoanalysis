import cv2
import pdb

from vidutils import read_frame

path = './videos/Recording001_Participant001_00.00.00-00.45.16.mp4'


cap = cv2.VideoCapture(path)

cap.set(1, cap.get(7)-1)

ret, frame = cap.read()

#for ii in range(1000):
#cnt = 0
#while True:
#    ret, frame = cap.read()
#    if ret == True:
#        cnt = cnt + 1
#    else:
#        break
#
#    if cnt % 1000 == 0:
#        print('cnt ', cnt)
#    #print('ret ', ret)
#print('cnt ', cnt) 
#print(cap.isOpened())
pdb.set_trace()
tmp = read_frame(cap, 1000)


print(type(tmp))

frame_num = cap.get(7)

print('frame num ', frame_num)

vid_rate = cap.get(5)

print('video rate ', vid_rate)
