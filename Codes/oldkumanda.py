import PiWarsTurkiyeRobotKiti2019
from time import sleep
joystik = PiWarsTurkiyeRobotKiti2019.Kumanda()  
joystik.dinlemeyeBasla()
motorlar = PiWarsTurkiyeRobotKiti2019.MotorKontrol()  #motorlar = PiWarsTurkiyeRobotKiti2019.MotorKontrol()  
m = 900
mod = 0

Rhiz = 0
Lhiz = 0

while True:
    Lsag, Lyukari = joystik.solVerileriOku() #Lsag = joystick sağ sola çevirilmesi
    Rsag, Ryukari = joystik.sagVerileriOku() #LYukari ise yukarı aşağı
    
    hiz = Lyukari * m
    
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