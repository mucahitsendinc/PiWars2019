import PiWarsTurkiyeRobotKiti2019
import RPi.GPIO as GPIO
import time
motorlar = PiWarsTurkiyeRobotKiti2019.MotorKontrol() 
GPIO.setmode(GPIO.BCM)
O_TRIG = 19
O_ECHO = 26
Sag_TRIG = 21
Sag_ECHO = 20
Sol_TRIG = 27
Sol_ECHO = 17

OrtaCik = GPIO.setup(O_TRIG, GPIO.OUT)
OrtaGir = GPIO.setup(O_ECHO, GPIO.IN)

SagCik = GPIO.setup(Sag_TRIG, GPIO.OUT)
SagGir = GPIO.setup(Sag_ECHO, GPIO.IN)

SolCik = GPIO.setup(Sol_TRIG, GPIO.OUT)
SolGir = GPIO.setup(Sol_ECHO, GPIO.IN)
 
while True:
    time.sleep(1)
    #ORTA SENSÖR HESABI
    
    GPIO.output(O_TRIG, True)
    time.sleep(0.00001)
    GPIO.output(O_TRIG, False)
    StartTimeO = time.time()
    StopTimeO = time.time()
    while GPIO.input(O_ECHO) == 0:
        StartTimeO = time.time()
    while GPIO.input(O_ECHO) == 1:
        StopTimeO = time.time()
    OrtaTime = StopTimeO - StartTimeO
    Omesafe = (OrtaTime * 34300) / 2
    
    #Sag Sensör HESABI
    GPIO.output(Sag_TRIG, True)
    time.sleep(0.00001)
    GPIO.output(Sag_TRIG, False)
    StartTimeSag = time.time()
    StopTimeSag = time.time()
    while GPIO.input(Sag_ECHO) == 0:
        StartTimeSag = time.time()
    while GPIO.input(Sag_ECHO) == 1:
        StopTimeSag = time.time()
    SagTime = StopTimeSag - StartTimeSag
    Sagmesafe = (SagTime * 34300) / 2
       
    #SOL SENSÖR HESABI
    
    GPIO.output(Sol_TRIG, True)
    time.sleep(0.00001)
    GPIO.output(Sol_TRIG, False)
    StartTimeSol = time.time()
    StopTimeSol = time.time()
    while GPIO.input(Sol_ECHO) == 0:
        StartTimeSol = time.time()
    while GPIO.input(Sol_ECHO) == 1:
        StopTimeSol = time.time()
    SolTime = StopTimeSol - StartTimeSol
    Solmesafe = (SolTime * 34300) / 2
    if Omesafe > 15:
        print ("Düz Git - Öndeki Cisime Kalan = %.1f cm" % Omesafe)
        motorlar.hizlariAyarla(270,270)
    if Omesafe < 15:
        if Sagmesafe > 15:
                print ("Saga Git - Sagdaki Cisime Kalan = %.1f cm" % Sagmesafe)
                motorlar.hizlariAyarla(270,100)
        if Sagmesafe < 15:
            if Solmesafe > 15:
                print ("Sola Git - Soldaki Cisime Kalan = %.1f cm" % Solmesafe)
                motorlar.hizlariAyarla(100,270)     
            if Solmesafe < 15:
                print ("180 Derece Dön !")
                motorlar.hizlariAyarla(400,-400)