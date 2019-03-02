#!/bin/python3

# Developer : Hamdy Abou El Anein

from datetime import date
from datetime import datetime
from easygui import *
import os
import sys

# Image files
green = "./pictures/green-light.jpg"
red = "./pictures/red-light.jpg"
floppy = "./pictures/floppy.png"

# Save the user input
def record():
    image = floppy
    msg = "The program recorded that you took your medicine today..\n\nClick on Exit to close."
    choices = ["Exit"]
    reply = buttonbox(msg, image=image, choices=choices)
    if reply == "Exit":
        sys.exit(0)
        
# Write the date of the day in a file. The software take the system date and time.
def writing():
    today1 = str(date.today())
    f=open("data", "a+")
    f.write((today1)+str("\r\n"))
    f.close()
    t=open("time", "w+")
    t.write(datetime.now().strftime('%Y-%m-%d %H:%M:%S')+str("\r\n"))
    t.close()
    record()

# Start of the software. Look if the file exist or no. Create if if not.
def start():
    if os.path.isfile("data") == True:
        if os.stat("data").st_size > 0:
            if str(date.today()) in open("data").read():
                   t1 =open("time", "r+")
                   datat1 = t1.read()
                   t1.close()
                   image = red
                   msg = "You already took your medicine today.\n\nThe date and time was "+str(datat1)
                   choices = ["Exit"]
                   reply = buttonbox(msg, image=image, choices=choices)
                   t1.close()
                   if reply == "Exit":
                       sys.exit(0)
            else:
                 image = green
                 msg = "You have not taken your medicine today\n\nClick on the button: << Take my medication >> to record your daily medication intake."
                 choices = ["Take my medication", "Exit"]
                 reply = buttonbox(msg, image=image, choices=choices)
                 if reply == "Take my medication":
                     writing()
                 else:
                    sys.exit(0)

        elif os.stat("data").st_size == 0:
            open("data", "a").close()
            image = green
            msg = "You have not taken your medicine today\n\nClick on the button: << Take my medication >> to record your daily medication intake."
            choices = ["Take my medication", "Exit"]
            reply = buttonbox(msg, image=image, choices=choices)
            if reply == "Take my medication":
                writing()
            else:
                sys.exit(0)

    # Create an empty file
    elif os.path.isfile("data") == False:
        open("data","a").close()
        image = green
        msg = "You have not taken your medicine today\n\nClick on the button: << Take my medication >> to record your daily medication intake."
        choices = ["Take my medication", "Exit"]
        reply = buttonbox(msg, image=image, choices=choices)
        if reply == "Take my medication":
            writing()
        else:
            sys.exit(0)
    else:
        print("Error 1")

start()