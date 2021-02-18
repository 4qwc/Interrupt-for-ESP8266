from machine import Pin
import time

# setup Pin OUTPUT
led_red = Pin(16, Pin.OUT)
led_green = Pin(5, Pin.OUT)
led_red.value(0)
led_green.value(0)

button_red = Pin(4, Pin.IN)

def STOP(pin):
    button_red.irq(handler=None)
    print('Interrupt Detected!')
    led_red.on()
    led_green.off()
    time.sleep(5)
    led_red.off()
    button_red.irq(handler=STOP)
    
# เรียกใช้อินเตอร์รับ
button_red.irq(trigger=Pin.IRQ_RISING, handler=STOP)
# เมื่อกดปุ่มจะเกิดอินเตอร์หรับ ช่วงขอบขาขึ้น และจะทำงานที่ฟังก์ชัั่น int_handler


# ส่วนที่ทำงานหลัก เมื่อเกิดอินเตอร์รับ จะหยุดทำงานและกลับมาทำต่อจากอินเตอร์หรับขัดจังหวะ
S = 0
M = 0
H = 0
while True:
    if S < 60:
        S+=1
        if S == 60:
            S = 0
            M += 1
            if M == 60:
                M = 0
                H += 1
                if H ==24:
                    H = 0
        
    print('Time: {}:{}:{}'.format( H, M, S))
    time.sleep(1)
    T1="time.time(): %f " %  time.time()
    T2=time.localtime( time.time())
    #T3=time.asctime( time.localtime(time.time()))
    print(T1)
    print(T2)
    #print(T3) 
        
# การทำงาน                
               
               
               
           


