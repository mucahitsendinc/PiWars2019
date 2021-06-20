import RPi.GPIO as IO
import time
import PiWarsTurkiyeRobotKiti2019
from time import sleep

motorlar = PiWarsTurkiyeRobotKiti2019.MotorKontrol()  ##motorlar = PiWarsTurkiyeRobotKiti2019.MotorKontrol()  

IO.setwarnings(False)
IO.setmode(IO.BCM)
onceki="yok"
IO.setup(16,IO.IN) #19 sağ
IO.setup(19,IO.IN) #21
IO.setup(20,IO.IN) #26
IO.setup(21,IO.IN) #20
#1 0 
def bulamadim():
    if onceki=="sol":
        motorlar.hizlariAyarla(100,-100)
    else:
        motorlar.hizlariAyarla(-100,100)
while 1:
   
    
    if (IO.input(19) == 1 or IO.input(20) == 1 ) :
        print("düz gidiyor...")
        motorlar.hizlariAyarla(-100,-100)
        
    elif (IO.input(16) == 0 and IO.input(21) == 1 ) :
        print("sağa gidiyor...")
        motorlar.hizlariAyarla(-150,-42)
        onceki="sag"
    elif (IO.input(16) == 1 and IO.input(21) == 0 ) :
        print("sola gidiyor...")
        motorlar.hizlariAyarla(-42,-150)
        onceki="sol"
    else :
        print("duruyor...")
        bulamadim()
        
    
