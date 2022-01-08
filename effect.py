import cv2
import numpy as np
from vcam import vcam,meshGen
from PySide6.QtWidgets import QWidget
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QPixmap,QImage

class Effect(QWidget):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load("ui/form_effect.ui",None)
        self.ui.show()
        self.face_detector = cv2.CascadeClassifier("package/face.xml")
        cap = cv2.VideoCapture(0)
        while True:
            _,self.frame = cap.read()
            self.frame = cv2.resize(self.frame,(164,164))
            self.frame_rgb = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
            width,height = self.frame.shape[:2]
            self.sizes = vcam(width,height)
            self.plane = meshGen(width,height)
            
            frame_mirror = self.convex_mirror(20*np.exp(-0.5*((self.plane.X*1.0/self.plane.W)/0.1)**2)/(0.1*np.sqrt(2*np.pi)))
            img1 = QImage(frame_mirror, frame_mirror.shape[1], frame_mirror.shape[0],QImage.Format_BGR888)
            pixmap1 = QPixmap.fromImage(img1)
            self.ui.label_filter1.setPixmap(pixmap1)

            frame_mirror = self.convex_mirror(20*np.exp(-0.5*((self.plane.Y*1.0/self.plane.H)/0.1)**2)/(0.1*np.sqrt(2*np.pi)))
            img2 = QImage(frame_mirror, frame_mirror.shape[1], frame_mirror.shape[0],QImage.Format_BGR888)
            pixmap2 = QPixmap.fromImage(img2)
            self.ui.label_filter2.setPixmap(pixmap2)

            frame_mirror = self.convex_mirror(20*np.sin(2*np.pi*((self.plane.X-self.plane.W/4.0)/self.plane.W)) + 20*np.sin(2*np.pi*((self.plane.Y-self.plane.H/4.0)/self.plane.H)))
            img3 = QImage(frame_mirror, frame_mirror.shape[1], frame_mirror.shape[0],QImage.Format_BGR888)
            pixmap3 = QPixmap.fromImage(img3)
            self.ui.label_filter3.setPixmap(pixmap3)

            frame_flip = self.flip()
            img4 = QImage(frame_flip, frame_flip.shape[1], frame_flip.shape[0],QImage.Format_BGR888)
            pixmap4 = QPixmap.fromImage(img4)
            self.ui.label_filter4.setPixmap(pixmap4)

            frame_pixelate = self.pixelate_face()
            img5 = QImage(frame_pixelate, frame_pixelate.shape[1], frame_pixelate.shape[0],QImage.Format_BGR888)
            pixmap5 = QPixmap.fromImage(img5)
            self.ui.label_filter5.setPixmap(pixmap5)

            frame_blur = self.blur()
            img6 = QImage(frame_blur, frame_blur.shape[1], frame_blur.shape[0],QImage.Format_BGR888)
            pixmap6 = QPixmap.fromImage(img6)
            self.ui.label_filter6.setPixmap(pixmap6)

            frame_cartoon = self.cartoon()
            img7 = QImage(frame_cartoon, frame_cartoon.shape[1], frame_cartoon.shape[0],QImage.Format_BGR888)
            pixmap7 = QPixmap.fromImage(img7)
            self.ui.label_filter7.setPixmap(pixmap7)

            frame_mirror = self.convex_mirror(10*np.sin((self.plane.X/self.plane.W)*2*np.pi*20))
            img8 = QImage(frame_mirror, frame_mirror.shape[1], frame_mirror.shape[0],QImage.Format_BGR888)
            pixmap8 = QPixmap.fromImage(img8)
            self.ui.label_filter8.setPixmap(pixmap8)

            frame_negative = self.negative()
            img9 = QImage(frame_negative, frame_negative.shape[1], frame_negative.shape[0],QImage.Format_BGR888)
            pixmap9 = QPixmap.fromImage(img9)
            self.ui.label_filter9.setPixmap(pixmap9)
            cv2.waitKey(1)          

    def convex_mirror(self,i):
        self.plane.Z = i
        pts3d = self.plane.getPlane()
        pts2d = self.sizes.project(pts3d)
        map_x,map_y = self.sizes.getMaps(pts2d)
        mirror = cv2.remap(self.frame,map_x,map_y,interpolation=cv2.INTER_LINEAR)
        return mirror

    def flip(self):
        frame = cv2.flip(self.frame,0)
        return frame

    def pixelate_face(self):
        blur = self.frame
        pixlate = cv2.resize(blur, (20,20), interpolation=cv2.INTER_LINEAR)
        output = cv2.resize(pixlate, (164, 164), interpolation=cv2.INTER_NEAREST)
        frame = output
        return frame

    def blur(self):
        frame_blur = cv2.blur(self.frame,(15,15))
        return frame_blur

    def cartoon(self):
        gray = cv2.cvtColor(self.frame,cv2.COLOR_BGR2GRAY)
        gray = cv2.medianBlur(gray,5)
        edge = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,9,9)
        color = cv2.bilateralFilter(self.frame,9,250,250)
        cartoon = cv2.bitwise_and(color,color,mask=edge)
        return cartoon

    def negative(self):
        frame_negative = 255 - self.frame
        return frame_negative  