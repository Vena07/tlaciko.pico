import machine
import time

led1 = machine.Pin(2,machine.Pin.OUT)
led2 = machine.Pin(3,machine.Pin.OUT)
led3 = machine.Pin(4,machine.Pin.OUT)
led4 = machine.Pin(5,machine.Pin.OUT)

buttton = machine.Pin(15,machine.Pin.IN,machine.Pin.PULL_UP)



led1.value(0)
led2.value(0)
led3.value(0)
led4.value(0)




while True:
    if buttton.value() == 0:
        ciklus = True
        time.sleep(0.5)
        while ciklus: 
            
            if buttton.value() == 0:
                time.sleep(0.5)
                if buttton.value() == 0:
                    konec = True
                    time.sleep(0.5)
                    while konec:
                        led1.value(1)
                        led2.value(1)
                        led3.value(1)
                        led4.value(1)
                        
                        if buttton.value() == 0:
                            konec = False 
                else:
                    led1.value(0)
                    led2.value(0)
                    led3.value(0)
                    led4.value(0)
                    time.sleep(0.5)
                    ciklus =False
                
            else:
                led2.value(0)
                led3.value(0)
                led4.value(0)
                led1.value(1)


         
    
    
