import PiWarsTurkiyeRobotKiti2019
from time import sleep
import RPi.GPIO as GPIO
import RPi.GPIO as IO
import time
joystik = PiWarsTurkiyeRobotKiti2019.Kumanda()  
joystik.dinlemeyeBasla()
bitis=2.5
baslangic=7.5
IO.setwarnings(False)

servo_pin=3
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin,GPIO.OUT)

p=GPIO.PWM(servo_pin,50)
p.start(baslangic)
while True:
    tuslar = joystik.butonlariOku()
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(2, GPIO.OUT) 
    GPIO.output(2, GPIO.HIGH)
    
    if tuslar == [4]:
        try:
            p.ChangeDutyCycle(2.5)
            sleep(0.5)
            p.ChangeDutyCycle(7.5)
            sleep(0.5)
            GPIO.output(2, GPIO.LOW)
            print("Hedefe kenetlendi")
            time.sleep(0.01);
            
            print("Boom. HEAD SHOT!")
        except KeyboardInterrupt:
            print("Cikis")
            GPIO.cleanup()
  
        
#Lsag, Lyukari = joystik.solVerileriOku() #Lsag = joystick sağ sola çevirilmesi
#Rsag, Ryukari = joystik.sagVerileriOku() #LYukari ise yukarı aşağı
