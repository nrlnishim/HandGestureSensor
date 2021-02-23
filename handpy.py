import serial #Serial imported for Serial communication
import time #Required to use delay functions
import pyautogui   #Required to to perform actions
import vlc

ArduinoSerial = serial.Serial('com2',9600) #Create Serial port object called arduinoSerialData
time.sleep(2) #wait for 2 seconds for the communication to get established



#player = vlc.MediaPlayer("C:\Users\Hanis Hashim\Videos\shinchan.mp4")
#player.play()
#player.pause()
#player.get_instance()
#player.stop

print('Python Ready')


while 1:


    #print(ArduinoSerial.name)
    incoming = str (ArduinoSerial.readline()) #read the serial data and print it as line
    print(incoming)

 
    
    if 'Play/Pause' in incoming:
        pyautogui.typewrite(['space'], 0.2)
        print('Playing')

    if 'Rewind' in incoming:
        pyautogui.hotkey('ctrl', 'left')  

    if 'Forward' in incoming:
        pyautogui.hotkey('ctrl', 'right') 

    if 'Volume Increased' in incoming:
        pyautogui.hotkey('ctrl', 'down')

    if 'Volume Decreased' in incoming:
        pyautogui.hotkey('ctrl', 'up')

    incoming = ""