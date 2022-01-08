import cv2
import numpy as np
from PySide6.QtWidgets import QWidget
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QPixmap,QImage

class Pallets(QWidget):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load("ui/form_pallet.ui",None)
        self.ui.show()
        cap = cv2.VideoCapture(0)
        while True:
            _,self.frame = cap.read()
            self.frame = cv2.resize(self.frame,(164,164))
            self.frame_rgb = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
            
            frame_autumn = self.autumn()
            img1 = QImage(frame_autumn, frame_autumn.shape[1], frame_autumn.shape[0],QImage.Format_RGB888)
            pixmap1 = QPixmap.fromImage(img1)
            self.ui.label_filter1.setPixmap(pixmap1)

            frame_bone = self.bone()
            img2 = QImage(frame_bone, frame_bone.shape[1], frame_bone.shape[0],QImage.Format_RGB888)
            pixmap2 = QPixmap.fromImage(img2)
            self.ui.label_filter2.setPixmap(pixmap2)

            frame_jet = self.jet()
            img3 = QImage(frame_jet, frame_jet.shape[1], frame_jet.shape[0],QImage.Format_RGB888)
            pixmap3 = QPixmap.fromImage(img3)
            self.ui.label_filter3.setPixmap(pixmap3)

            frame_winter = self.winter()
            img4 = QImage(frame_winter, frame_winter.shape[1], frame_winter.shape[0],QImage.Format_RGB888)
            pixmap4 = QPixmap.fromImage(img4)
            self.ui.label_filter4.setPixmap(pixmap4)

            frame_ocean = self.ocean()
            img5 = QImage(frame_ocean, frame_ocean.shape[1], frame_ocean.shape[0],QImage.Format_RGB888)
            pixmap5 = QPixmap.fromImage(img5)
            self.ui.label_filter5.setPixmap(pixmap5)

            frame_summer = self.summer()
            img6 = QImage(frame_summer, frame_summer.shape[1], frame_summer.shape[0],QImage.Format_RGB888)
            pixmap6 = QPixmap.fromImage(img6)
            self.ui.label_filter6.setPixmap(pixmap6)

            frame_spring = self.spring()
            img7 = QImage(frame_spring, frame_spring.shape[1], frame_spring.shape[0],QImage.Format_RGB888)
            pixmap7 = QPixmap.fromImage(img7)
            self.ui.label_filter7.setPixmap(pixmap7)

            frame_cool = self.cool()
            img8 = QImage(frame_cool, frame_cool.shape[1], frame_cool.shape[0],QImage.Format_RGB888)
            pixmap8 = QPixmap.fromImage(img8)
            self.ui.label_filter8.setPixmap(pixmap8)

            frame_pink = self.pink()
            img9 = QImage(frame_pink, frame_pink.shape[1], frame_pink.shape[0],QImage.Format_BGR888)
            pixmap9 = QPixmap.fromImage(img9)
            self.ui.label_filter9.setPixmap(pixmap9)
            cv2.waitKey(1)          

    def autumn(self):
        frame_autumn = cv2.applyColorMap(self.frame, cv2.COLORMAP_AUTUMN)
        return frame_autumn

    def bone(self):
        frame_bone = cv2.applyColorMap(self.frame, cv2.COLORMAP_BONE)
        return frame_bone

    def jet(self):
        frame_jet = cv2.applyColorMap(self.frame, cv2.COLORMAP_JET)
        return frame_jet

    def winter(self):
        frame_winter = cv2.applyColorMap(self.frame, cv2.COLORMAP_WINTER)
        return frame_winter

    def ocean(self):
        frame_ocean = cv2.applyColorMap(self.frame, cv2.COLORMAP_OCEAN)
        return frame_ocean

    def summer(self):
        frame_summer = cv2.applyColorMap(self.frame, cv2.COLORMAP_SUMMER)
        return frame_summer

    def spring(self):
        frame_spring = cv2.applyColorMap(self.frame, cv2.COLORMAP_SPRING)
        return frame_spring

    def cool(self):
        frame_cool = cv2.applyColorMap(self.frame, cv2.COLORMAP_COOL)
        return frame_cool

    def pink(self):
        frame_pink = cv2.applyColorMap(self.frame, cv2.COLORMAP_PINK)
        return frame_pink
