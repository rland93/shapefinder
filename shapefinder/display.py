'''
Module to display a frame source multithreaded
'''
from threading import Thread
import cv2

class GetVideo(object):
    def __init__(self, src):
        self.stream = cv2.VideoCapture(src)
        (self.success, self.frame) = self.stream.read()
        self.stopped = False
    
    def start(self):
        Thread(target=self.get, args=()).start()
        return self
    
    def get(self):
        while not self.stopped:
            if not self.success:
                self.stop()
            else:
                (self.success, self.frame) = self.stream.read()

    def stop(self):
        self.stopped = True
    
    def getsize(self):
        (success, frame) = self.stream.read()
        return frame.shape[0], frame.shape[1]


class ShowVideo(object):
    def __init__(self, frame):
        self.frame = frame
        self.stopped = False

    def start(self):
        Thread(target=self.show(), args=()).start()
        return self

    def show(self):
        while not self.stopped:
            cv2.imshow('img', self.frame)
            if cv2.waitKey(0) == ord('g'):
                self.stopped = True

    def stop(self):
        self.stopped = True

def playvideo(src):
    video = GetVideo(src).start()
    video_show  = ShowVideo(video.frame).start()
    while True:
        # check if stop video
        if video.stopped or video_show.stopped:
            video.stop()
            video_show.stop()
            break
        
        ####### process frames
        #
        #
        video_show.frame = colorblock(frame, saturation_thresh, value_thresh, blur_size, clip_size, max_objs_frame)
        #
        #
        ######
        video_show.show()