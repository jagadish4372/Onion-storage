from tkinter import Toplevel, Button, Tk, Menu, Label 
import os
from tkinter import StringVar
import serial
import time
import os
import selenium
#from selenium.webdriver.common.by import By
import webbrowser
#from selenium import webdriver
from tkinter import ttk
import webview
import urllib.request  
#from selenium.webdriver.chrome.service import Service
#from webdriver_manager.chrome import ChromeDriverManager

top = Tk()
top.geometry('1920x1080')
top.configure(bg='#7d2ae8')

def contact():
    toplevel = Toplevel(top)
    toplevel.title("CONTACT DETAILS")
    l9=Label(toplevel,text="Contact details",font=("bold",20))
    l9.grid(row=0, column=0)
    l10=Label(toplevel,text="Mobile: +919361813434",font=("bold",15))
    l10.grid(row=1, column=0)
    l12=Label(toplevel,text="Mobile: +916374337604",font=("bold",15))
    l12.grid(row=2, column=0)
    l11=Label(toplevel,text="E-mail: technologykryo@gmail.com",font=("bold",15))
    l11.grid(row=3, column=0)
def about():
    toplevel = Toplevel(top)
    toplevel.title("KRYO TECH")
    l9=Label(toplevel,text="KRYO TECH",font=("Arial",25))
    l9.grid(row=0, column=0)
    l10=Label(toplevel,text="Experts in Onion cold storage solutions",font=("bold",20))
    l10.grid(row=1, column=0)
    l11=Label(toplevel,text="Mentor:",font=("Arial",15))
    l11.grid(row=2, column=0)
    l11=Label(toplevel,text='                                     '"Dr.Vignesh Kumar",font=("Arial",15))
    l11.grid(row=3, column=0)
    l13=Label(toplevel,text="Team members:",font=("Arial",15))
    l13.grid(row=4, column=0)
    l12=Label(toplevel,text='                                       '"1) Vishaal R",font=("Arial",15))
    l12.grid(row=5, column=0)
    l14=Label(toplevel,text='                                                  '"2) Suraj Narayanan",font=("Arial",15))
    l14.grid(row=6, column=0)
    l15=Label(toplevel,text='                                           '"3) Karthikeyan",font=("Arial",15))
    l15.grid(row=7, column=0)
    l16=Label(toplevel,text='                                       '"4) Jagadish",font=("Arial",15))
    l16.grid(row=8, column=0)
    l17=Label(toplevel,text='                                         '"5) Sudarshan",font=("Arial",15))
    l17.grid(row=9, column=0)
    l18=Label(toplevel,text='                                       '"6) Kumaran",font=("Arial",15))
    l18.grid(row=10, column=0)
    l19=Label(toplevel,text='                                     '"7) Jessica",font=("Arial",15))
    l19.grid(row=11, column=0)
    l20=Label(toplevel,text='                                                '"8) Gnana Varshini",font=("Arial",15))
    l20.grid(row=12, column=0)
    l21=Label(toplevel,text='                                     '"9) Kirthika",font=("Arial",15))
    l21.grid(row=13, column=0)
    
def sensorrrr():
    ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
    ser.reset_input_buffer()
    c=0
    a='C'
    b='Kg'
    while(1):
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            line.split()
            for i in range(len(line)):
                if line[i] in a:
                    
                    temp=line
                    temperature()
                elif line[i] in b:
                    
                    load=line
                    weight3()
                c+=1
            time.sleep(0.3)
def ML():
    os.popen("edge-impulse-linux")
    url = "https://studio.edgeimpulse.com/studio/138801/classification"
    webbrowser.open(url)
def temperature():
    global temp1
    temp1.configure(text=temp)
def weight3():
    global load
    weight1.configure(text=load)
menubar = Menu(top)  
file = Menu(menubar, tearoff=0)
ras=Menu(menubar,tearoff=0)
temp1 = Label(top, text ='',font=("Rockwell extra bold",80)).place(x = 140,y = 460)
weight1 = Label(top, text = '',font=("Rockwell extra bold",80)).place(x = 1500,y = 460)
title=Label(top,text="KRYO TECH",font=("Courier New",100),bg='#7d2ae8',fg="white").place(x=600,y=100)
temp = Label(top, text = "TEMPERATURE",font=("Cooper black",40),bg='#7d2ae8').place(x = 140,y = 400)
hum = Label(top, text = "RELATIVE HUMIDITY",font=("Cooper black",40),bg='#7d2ae8').place(x = 750, y = 400)
hum1 = Label(top, text = "60%",font=("Rockwell extra bold",80),bg='#7d2ae8').place(x = 750, y = 460)
weight = Label(top, text = "WEIGHT",font=("Cooper black",40),bg='#7d2ae8').place(x = 1500,y = 400)
menubar.add_cascade(label="Home", menu=file)  
edit = Menu(menubar, tearoff=0)   
edit.add_command(label="AHT10 Temperature",command=sensorrrr)  
edit.add_command(label="AHT10 Humidity")  
edit.add_command(label="Weight")  
menubar.add_cascade(label="SensorCM", menu=edit)
menubar.add_cascade(label="R&S Detector",menu=ras)
ras.add_command(label="Deploy ML",command=ML)
help = Menu(menubar, tearoff=0)  
help.add_command(label="About",command=about)
help.add_command(label="Contact us",command=contact)
menubar.add_cascade(label="Help", menu=help)
top.config(menu=menubar)  
top.mainloop()
