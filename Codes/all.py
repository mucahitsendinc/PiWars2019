import PiWarsTurkiyeRobotKiti2019
from time import sleep
import RPi.GPIO as GPIO
import RPi.GPIO as IO

import time
motorlar = PiWarsTurkiyeRobotKiti2019.MotorKontrol()  #motorlar = PiWarsTurkiyeRobotKiti2019.MotorKontrol()  
joystik = PiWarsTurkiyeRobotKiti2019.Kumanda()  
joystik.dinlemeyeBasla()  
hizsag=0 #Sağ taraf tekerlerinin hızları
hizsol=0 #Sol taraf tekerlerinin hızları
verilcekhiz1=0
verilcekhiz2=0
hizver=False
donus="yok"
oyunmod="bos"
GPIO.setwarnings(False)
#Select GPIO mode
GPIO.setmode(GPIO.BCM)
#Set buzzer - pin 23 as output
gaz=10
TRIG = 15
ECHO = 14
buzzer = 26
m = 480
mod = 0
Rhiz = 0
Lhiz = 0
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
def bulamadim():
    if onceki=="sol":
        motorlar.hizlariAyarla(140,-140)
    else:
        motorlar.hizlariAyarla(-140,140)
    
def cik():
    tuslar = joystik.butonlariOku()
    if tuslar==[7]:
        return True
    
while True:
    tuslar = joystik.butonlariOku()
    if tuslar==[0]:
        oyunmod="kumanda"
    elif tuslar==[1]:
        oyunmod="duvar"
    elif tuslar==[2]:
        oyunmod="cizgi"
    else:
        oyunmod="bos"
        
    motorlar.hizlariAyarla(0,0)
        
    #print(oyunmod)
    
    if oyunmod=="kumanda":
        while True:
            if cik():
                oyunmod = "bos"
                break
            
            Lsag, Lyukari = joystik.solVerileriOku() #Lsg = joystick sağ sola çevirilmesi
            Rsag, Ryukari = joystik.sagVerileriOku() #LYukari ise yukarı aşağı
            if (Lyukari>= -1 ) or (Lyukari<= 1 ):
                gaz = min(gaz + 1, 30)
            else:
                gaz=10
                
            hiz = (Lyukari * m) * (gaz / 30)
            
            tuslar = joystik.butonlariOku() #Analog dışı tuşlar
            
            if tuslar == [4]:
                mod = 0
            elif tuslar == [5]:
                mod = 1
                
            if Rsag > 0:
                Rhiz = mod==0 and hiz * 0.125 or -hiz
                Lhiz = hiz
                
            elif Rsag < 0:
                Rhiz = hiz
                Lhiz = mod==0 and hiz * 0.125 or -hiz
            else:
                Rhiz = hiz
                Lhiz = hiz
            
            print(round(Lhiz), " - ", round(Rhiz))
            
            if hiz > 0:
                motorlar.hizlariAyarla(round(Lhiz), round(Rhiz))
            else:
                motorlar.hizlariAyarla(round(Rhiz), round(Lhiz))
                
            sleep(0.1)
    elif oyunmod=="duvar":
        while True:
            try:
                if cik():
                    break
                
                GPIO.output(TRIG, False)
                time.sleep(0.01)

                GPIO.output(TRIG, True)
                time.sleep(0.00001)
                GPIO.output(TRIG, False)

                while GPIO.input(ECHO)==0:
                    pulse_start = time.time()

                while GPIO.input(ECHO)==1:
                    pulse_end = time.time()

                pulse_duration = pulse_end - pulse_start

                distance = pulse_duration * 17150
                distance = round(distance, 2)

                print ("Mesafe:",distance,"cm")
                if distance <= 7:
                    motorlar.hizlariAyarla(0, 0)
                    oyunmod = "bos"
                    break
                else:
                    motorlar.hizlariAyarla(-150, -150)
            except:
                motorlar.hizlariAyarla(0, 0)
                oyunmod = "bos"
                break
            
            time.sleep(0.04)
            
    elif oyunmod=="cizgi":
        IO.setwarnings(False)
        IO.setmode(IO.BCM)
        onceki="yok"
        IO.setup(16,IO.IN) #19 sağ
        IO.setup(19,IO.IN) #21
        IO.setup(20,IO.IN) #26
        IO.setup(21,IO.IN) #20
        while 1:
            if cik():
                break
            
            if (IO.input(19) == 1 or IO.input(20) == 1 ) :
                print("düz gidiyor...")
                motorlar.hizlariAyarla(-145,-145)
                
            elif (IO.input(16) == 0 and IO.input(21) == 1 ) :
                print("sağa gidiyor...")
                motorlar.hizlariAyarla(-240,-52)
                onceki="sag"
            elif (IO.input(16) == 1 and IO.input(21) == 0 ) :
                print("sola gidiyor...")
                motorlar.hizlariAyarla(-52,-240)
                onceki="sol"
            else :
                print("duruyor...")
                bulamadim()
                
   
        

