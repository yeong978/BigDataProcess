#!/usr/bin/python3
#Q1
class Camera:
    def __init__(self,pixel,zoom):
        self.pixel = pixel
        self.zoom = zoom
    def takepicture(self):
        print("찰칵")
        print("사진이 저장되었습니다.(화소: %d만, 배율 :  %.1fx)" % (self.pixel,self.zoom))
           
if __name__ == "__q2__":
    nikon = q1.Camera(2000, 2.5)
    nikon.takepicture()
    
    
'''
canon = Camera(2430, 1.0)
canon.takepicture()
sony = Camera(2410, 3.0)
sony.takepicture()'''
