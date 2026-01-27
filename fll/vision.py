#!/usr/bin/env python3
import time, math
from DRV8825 import DRV8825
import pygame
import pygame.camera

pic_count = 0
pygame.camera.init()
Motor1 = DRV8825(dir_pin=13, step_pin=19, enable_pin=12, mode_pins=(16, 17, 20))
Motor2 = DRV8825(dir_pin=24, step_pin=18, enable_pin=4, mode_pins=(21, 22, 27))
Motor1.SetMicroStep('softward','fullstep')
Motor2.SetMicroStep('hardward' ,'halfstep')

def Motor1_Turn(degrees, direction):
    steps = int(math.floor((degrees  / 360) * 2400)* 5)  
    Motor1.TurnStep(Dir=direction, steps=steps, stepdelay = 0.00002)
    Motor1.Stop()


def Motor2_Turn(degrees, direction):
    steps = int(math.floor((degrees /360) * 4800)* 15)  
    Motor2.TurnStep(Dir=direction, steps=steps, stepdelay = 0.00001)
    Motor2.Stop()
cams = pygame.camera.list_cameras()
print('Available cameras:', cams)

if cams:
    cam = pygame.camera.Camera(cams[0], (640, 480))  
    cam.start()                                                
else:
    print("No camera found.")

def take_picture():
    global pic_count
    pic_count = pic_count + 1
    image = cam.get_image()                                  
    pygame.image.save(image, "images/captured_img" + str(pic_count) + ".jpg")          
    print("Picture taken and saved at images/captured_img" + str(pic_count) + ".jpg'.")

for i in range(1):
    take_picture()
    Motor2_Turn(160, 'forward')
    take_picture()
    Motor2_Turn(160, 'backward')
    take_picture()
    Motor2_Turn(160, 'backward')
    take_picture()
    Motor1_Turn(75, 'forward')
    take_picture()
    Motor2_Turn(160, 'forward')
    take_picture()
    Motor2_Turn(160, 'forward')
    take_picture()
    Motor1_Turn(150, 'backward')
    take_picture()
    Motor2_Turn(160, 'backward')
    take_picture()
    Motor2_Turn(160, 'backward')
    take_picture()
    Motor2_Turn(160, 'forward')
    Motor1_Turn(75, 'forward')
    take_picture()
    Motor1.Stop()
    Motor2.Stop()
    time.sleep(2)

cam.stop()                                      