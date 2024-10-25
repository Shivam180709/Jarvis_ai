print("Please Wait Jarvis is starting.......")
# Please Enter you  username and password of Hugging CHat website
hugging_face_username = ""
hugging_face_password = ""
# Required Imports
import os
import sys
from tkinter import messagebox
os.startfile("Loading_Screen_Jarvis.exe")
try:
     import pywhatkit
except Exception as e:
        os.system("TASKKILL /F /im Loading_Screen_Jarvis.exe")
        result = messagebox.askyesno("Error -:- -- No Internet --", "No Internet do you want to restart the software")

        if result:
                print("User clicked Yes")
                os.startfile("Jarvis_Main.exe")
                sys.exit()
        else:
                print("User clicked No")
                sys.exit()
from plyer import notification
from pygame import mixer
from tkinter import *
import wikipedia
import keyboard
import pyautogui
import webbrowser
from time import sleep
import os
import requests
from tkinter import Tk
import datetime
from hugchat import hugchat
from hugchat.login import Login
import pyaudio
import struct
import math
import os
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import messagebox
import threading
from PyQt5 import QtCore, QtGui, QtWidgets
import PyQt5
from PyQt5.QtGui import QIcon
import pyttsx3
import speech_recognition as sr
import webbrowser
from bs4 import BeautifulSoup
mixer.init()
mixer.music.load("audio.mp3")
def Jarvis_Execution():
        # Hugging Face Login
        sign = Login(hugging_face_username, hugging_face_password)
        cookies = sign.login()
        
        title = r'J.A.R.V.I.S : Your Personal A.I Desktop Asistant '
        app_name= r'J.A.R.V.I.S'
        app_icon=r"GUI_Materials\Icon_of_Jarvis-removebg-preview.ico"
        # Variables declaration for the Speak function
        engine = pyttsx3.init("sapi5")
        voices = engine.getProperty('voices')
        try:
                engine.setProperty('voices',voices[4].id)
        except:
                print("Voice 1 setted")
                engine.setProperty('voices',voices[1].id)
        engine.setProperty('rate',155)


        # Speak funtion for outside the Ui_MainWindow class
        def Speak(Text):
                """
                This is function which take an argument 'Text' 
                and speak the given string. 
                """
                engine.say(Text)
                engine.runAndWait()


        def Intro():
                """"This function executes when the 'Tell your intro' button is clicked in a new thread"""
       
                mixer.music.load("audio2.mp3")
                mixer.music.play()

        def about_developer():
                """"This function executes when the 'about developed' button is clicked in a new thread"""
                mixer.music.load("audio3.mp3")
                mixer.music.play()


    
        def propad_program(): 
                """This function is acting like a mini progrmam with is of a simple notepad in python named 'ProPad' which will run when the Launch propad button is clicked """
                root = Tk()
                root.iconbitmap("Notepad.ico")
                TextArea = Text(root, font="lucida 10")
                TextArea.pack(fill=BOTH, expand=True)


                def newFile():
                            global file
                            root.title("Untitled - Propad")
                            file = None
                            TextArea.delete(1.0, END)
        
        
                def openFile():
                                    global file
                                    file = askopenfilename(filetypes=[("All File", "*.*"),
                                                                                            ("Text Documents", "*.txt")], defaultextension=".txt")
                                    if file == "":
                                                    file = None
                                    else:
                                                    root.title(os.path.basename(file) + "- Propad")
                                                    TextArea.delete(1.0, END)
                                                    f = open(file, "r")
                                                    TextArea.insert(1.0, f.read())
                                                    f.close
        
        
                def saveFile():
                        global file
                        if file == None:
                            file = asksaveasfilename(initialfile='Untitled.txt'
                                                    , defaultextension=".txt",
                                                    filetypes=[("All File", "*.*"),
                                                                ("Text Documents", "*.txt")])
                            if file == "":
                                file = None
                            else:
                                f = open(file, "w")
                                f.write(TextArea.get(1.0, END))
                                f.close()

                            root.title(os.path.basename(file) + " - Propad")
                        else:
                            f = open(file, "w")
                            f.write(TextArea.get(1.0, END))
                            f.close()


                def quitApp():
                    root.destroy()


                def cut():
                    TextArea.event_generate("<<Cut>>")


                def copy():
                    TextArea.event_generate("<<Copy>>")


                def paste():
                    TextArea.event_generate("<<Paste>>")


                def about():
                    showinfo("Propad", "This is notepad is created by Shivam Pathak")


                root.title("Untitled - Propad")
                root.geometry("1000x599")

                file = None

                Menubar = Menu(root)
                # File Menu
                fileMenu = Menu(Menubar, tearoff=0)

                fileMenu.add_command(label="New", command=newFile)

                fileMenu.add_command(label="Open", command=openFile)

                fileMenu.add_command(label="Save", command=saveFile)

                fileMenu.add_command(label="Exit", command=quitApp)

                Menubar.add_cascade(label="File", menu=fileMenu)

                # Edit menu

                EditMenu = Menu(Menubar, tearoff=0)

                EditMenu.add_command(label="Cut", command=cut)
                EditMenu.add_command(label="Copy", command=copy)
                EditMenu.add_command(label="Paste", command=paste)

                Menubar.add_cascade(label="Edit", menu=EditMenu)

                # Help Menu
                HelpMenu = Menu(Menubar, tearoff=0)

                HelpMenu.add_command(label="About - Propad", command=about)
                Menubar.add_cascade(label="Help", menu=HelpMenu)

                root.config(menu=Menubar)

                # Scrollbar
                Scroll = Scrollbar(TextArea)
                Scroll.pack(side=RIGHT, fill=Y)
                Scroll.config(command=TextArea.yview)
                TextArea.config(yscrollcommand=Scroll.set)

                root.mainloop()


        def snake_game():
                """This function simplely start the snake.exe file using os module in a new thread"""
                a = os.startfile(r"mini_projects\Snake.exe")
                thread = threading.Thread(target=a)
                thread.start() 

        def flappy_game():
                """This function simplely start the Flappy Bird.exe file using os module in a new thread"""
                a = os.startfile(r"mini_projects\Flappy Bird.exe")
                thread = threading.Thread(target=a)
                thread.start() 

        def propad():
                """This function simplely to call the propad program function in a new thread """
                a = propad_program()
                thread = threading.Thread(target=a)
                thread.start() 

        def password():
                """This function simplely start the Password Generator.exe file using os module in a new thread """
                a = os.startfile(r"mini_projects\Password Generator.exe")
                thread = threading.Thread(target=a)
                thread.start() 

        def calculator():
                """This function simplely start the Calculator.exe file using os module in a new thread """
                a = os.startfile(r'mini_projects\Calculator.exe')
                thread = threading.Thread(target=a)
                thread.start() 

        def power():
                """This function simplely start the Power.exe file using os module in a new thread """
                a = os.startfile(r'mini_projects\Power.exe')
                thread = threading.Thread(target=a)
                thread.start() 

        # Clap Detection Program
        INITIAL_TAP_THRESHOLD = 0.01#0.01 - 1.5
        FORMAT = pyaudio.paInt16 
        SHORT_NORMALIZE = (1.0/32768.0)
        CHANNELS = 2
        RATE = 44100  
        INPUT_BLOCK_TIME = 0.05
        INPUT_FRAMES_PER_BLOCK = int(RATE*INPUT_BLOCK_TIME)
        OVERSENSITIVE = 15.0/INPUT_BLOCK_TIME                    
        UNDERSENSITIVE = 120.0/INPUT_BLOCK_TIME 
        MAX_TAP_BLOCKS = 0.15/INPUT_BLOCK_TIME

        def get_rms( block ):
            count = len(block)/2
            format = "%dh"%(count)
            shorts = struct.unpack( format, block )
            sum_squares = 0.0
            for sample in shorts:
                n = sample * SHORT_NORMALIZE
                sum_squares += n*n

            return math.sqrt( sum_squares / count )

        class TapTester(object):

                def __init__(self):
                    self.pa = pyaudio.PyAudio()
                    self.stream = self.open_mic_stream()
                    self.tap_threshold = INITIAL_TAP_THRESHOLD
                    self.noisycount = MAX_TAP_BLOCKS+1 
                    self.quietcount = 0 
                    self.errorcount = 0

                def stop(self):
                    self.stream.close()

                def find_input_device(self):
                    device_index = None            
                    for i in range( self.pa.get_device_count() ):     
                        devinfo = self.pa.get_device_info_by_index(i)   
                        # print( "Device %d: %s"%(i,devinfo["name"]) )

                        for keyword in ["mic","input"]:
                            if keyword in devinfo["name"].lower():
                                # print( "Found an input: device %d - %s"%(i,devinfo["name"]) )
                                device_index = i
                                return device_index

                    if device_index == None:
                        print( "No preferred input found; using default input device." )

                    return device_index

                def open_mic_stream( self ):
                    device_index = self.find_input_device()

                    stream = self.pa.open(   format = FORMAT,
                                             channels = CHANNELS,
                                             rate = RATE,
                                             input = True,
                                             input_device_index = device_index,
                                             frames_per_buffer = INPUT_FRAMES_PER_BLOCK)

                    return stream

                def listen(self):

                    try:
                        block = self.stream.read(INPUT_FRAMES_PER_BLOCK)

                    except IOError as e:
                        self.errorcount += 1
                        print( "(%d) Error recording: %s"%(self.errorcount,e) )
                        self.noisycount = 1
                        return

                    amplitude = get_rms( block )

                    if amplitude > self.tap_threshold:
                        self.quietcount = 0
                        self.noisycount += 1
                        if self.noisycount > OVERSENSITIVE:

                            self.tap_threshold *= 1.1
                    else:            

                        if 1 <= self.noisycount <= MAX_TAP_BLOCKS:
                            return "True-Mic"
                        self.noisycount = 0
                        self.quietcount += 1
                        if self.quietcount > UNDERSENSITIVE:
                            self.tap_threshold *= 2



        def restart():
            os.system("shutdown /r /t 1")

        def restart_time(time):
            os.system(f"shutdown /r /t {time}")

        def log_out():
            os.system("shutdown -l")

        def shudown():
            os.system("shutdown /s /t 1")

        def shudown_time(time):
            os.system(f"shutdown /s /t {time}")


        chatbot = hugchat.ChatBot(cookies=cookies.get_dict())
        remember_text = r'''Hello, Your name is Jarvis an aritificial intelligence(A.I) and I am Shivam Pathak your creartor. You are created to assist me and other people. 
                I had created you to help and serve people.  I am 14 years old and current studying in class 9th in St. Mary's convent School,Hinauli Mughalsarai.
                \nSo, I am want you to remember it and behave like Jarvis and note that you give short and sweet response like Jarvis please remember this It is important.'''
        print(chatbot.chat(remember_text))
        class Ui_MainWindow(object):
                # The function which have to run just after creation of Object of Ui_MainWindow
        
                def setupUi(self, MainWindow):
                        MainWindow.setObjectName("MainWindow")
                        MainWindow.resize(1384, 711)
                        icon = QtGui.QIcon()
                        icon.addPixmap(QtGui.QPixmap("Jarvsi GUI/iconforjarvis.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                        MainWindow.setWindowIcon(icon)
                        self.centralwidget = QtWidgets.QWidget(MainWindow)
                        self.centralwidget.setObjectName("centralwidget")
                        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
                        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1401, 721))
                        self.tabWidget.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
                "font: 75 11pt \"Microsoft YaHei UI\";\n"
                "font: 75 11pt \"Sitka Small\";\n"
                "color: rgb(0, 85, 255);\n"
                "color: rgb(170, 0, 0);")
                        self.tabWidget.setObjectName("tabWidget")
                        self.tab = QtWidgets.QWidget()
                        self.tab.setObjectName("tab")
                        self.voice_gif = QtWidgets.QLabel(self.tab)
                        self.voice_gif.setGeometry(QtCore.QRect(240, 570, 111, 101))
                        self.voice_gif.setStyleSheet("border-color: rgb(255, 0, 4);")
                        self.voice_gif.setText("")
                        self.voice_gif.setPixmap(QtGui.QPixmap("GUI_Materials/siri2.gif"))
                        self.voice_gif.setScaledContents(True)
                        self.voice_gif.setObjectName("voice_gif")
                        self.line_4 = QtWidgets.QFrame(self.tab)
                        self.line_4.setGeometry(QtCore.QRect(0, 170, 20, 181))
                        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
                        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
                        self.line_4.setObjectName("line_4")
                        self.line_28 = QtWidgets.QFrame(self.tab)
                        self.line_28.setGeometry(QtCore.QRect(860, 180, 181, 20))
                        self.line_28.setFrameShape(QtWidgets.QFrame.HLine)
                        self.line_28.setFrameShadow(QtWidgets.QFrame.Sunken)
                        self.line_28.setObjectName("line_28")
                        self.line_21 = QtWidgets.QFrame(self.tab)
                        self.line_21.setGeometry(QtCore.QRect(790, 230, 20, 381))
                        self.line_21.setFrameShape(QtWidgets.QFrame.VLine)
                        self.line_21.setFrameShadow(QtWidgets.QFrame.Sunken)
                        self.line_21.setObjectName("line_21")
                        self.line_24 = QtWidgets.QFrame(self.tab)
                        self.line_24.setGeometry(QtCore.QRect(1050, 220, 111, 20))
                        self.line_24.setFrameShape(QtWidgets.QFrame.HLine)
                        self.line_24.setFrameShadow(QtWidgets.QFrame.Sunken)
                        self.line_24.setObjectName("line_24")
                        self.line_19 = QtWidgets.QFrame(self.tab)
                        self.line_19.setGeometry(QtCore.QRect(240, 690, 118, 3))
                        self.line_19.setFrameShape(QtWidgets.QFrame.HLine)
                        self.line_19.setFrameShadow(QtWidgets.QFrame.Sunken)
                        self.line_19.setObjectName("line_19")
                        self.earth_gif = QtWidgets.QLabel(self.tab)
                        self.earth_gif.setGeometry(QtCore.QRect(860, 50, 181, 141))
                        self.earth_gif.setText("")
                        self.earth_gif.setPixmap(QtGui.QPixmap("Jarvsi GUI/ExtraGui/Earth.gif"))
                        self.earth_gif.setScaledContents(True)
                        self.earth_gif.setObjectName("earth_gif")
                        self.line_3 = QtWidgets.QFrame(self.tab)
                        self.line_3.setGeometry(QtCore.QRect(160, 170, 20, 181))
                        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
                        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
                        self.line_3.setObjectName("line_3")
                        self.arc_gif = QtWidgets.QLabel(self.tab)
                        self.arc_gif.setGeometry(QtCore.QRect(0, 410, 161, 121))
                        self.arc_gif.setAutoFillBackground(False)
                        self.arc_gif.setText("")
                        self.arc_gif.setPixmap(QtGui.QPixmap("GUI_Materials/S (38).gif"))
                        self.arc_gif.setScaledContents(True)
                        self.arc_gif.setObjectName("arc_gif")
                        self.line_18 = QtWidgets.QFrame(self.tab)
                        self.line_18.setGeometry(QtCore.QRect(240, 70, 531, 16))
                        self.line_18.setFrameShape(QtWidgets.QFrame.HLine)
                        self.line_18.setFrameShadow(QtWidgets.QFrame.Sunken)
                        self.line_18.setObjectName("line_18")
                        self.line_26 = QtWidgets.QFrame(self.tab)
                        self.line_26.setGeometry(QtCore.QRect(850, 50, 20, 141))
                        self.line_26.setFrameShape(QtWidgets.QFrame.VLine)
                        self.line_26.setFrameShadow(QtWidgets.QFrame.Sunken)
                        self.line_26.setObjectName("line_26")
                        self.label_2 = QtWidgets.QLabel(self.tab)
                        self.label_2.setGeometry(QtCore.QRect(810, 250, 341, 351))
                        self.label_2.setText("")
                        self.label_2.setPixmap(QtGui.QPixmap("GUI_Materials/S (1).webp"))
                        self.label_2.setScaledContents(True)
                        self.label_2.setObjectName("label_2")
                        self.label_6 = QtWidgets.QLabel(self.tab)
                        self.label_6.setGeometry(QtCore.QRect(0, 590, 241, 81))
                        self.label_6.setText("")
                        self.label_6.setPixmap(QtGui.QPixmap("GUI_Materials/S__5_-removebg-preview.png"))
                        self.label_6.setScaledContents(True)
                        self.label_6.setObjectName("label_6")
                        self.line_20 = QtWidgets.QFrame(self.tab)
                        self.line_20.setGeometry(QtCore.QRect(240, 670, 531, 16))
                        self.line_20.setFrameShape(QtWidgets.QFrame.HLine)
                        self.line_20.setFrameShadow(QtWidgets.QFrame.Sunken) 
                        self.line_20.setObjectName("line_20")
                        self.mainbg = QtWidgets.QLabel(self.tab)
                        self.mainbg.setGeometry(QtCore.QRect(-40, 0, 1461, 701))
                        self.mainbg.setText("")
                        self.mainbg.setPixmap(QtGui.QPixmap("GUI_Materials/S (18)"))
                        self.mainbg.setScaledContents(True)
                        self.mainbg.setObjectName("mainbg")
                        self.line_14 = QtWidgets.QFrame(self.tab)
                        self.line_14.setGeometry(QtCore.QRect(230, 90, 16, 601))
                        self.line_14.setStyleSheet("background-color: rgb(13, 0, 55);\n"
                "background-color: rgb(0, 0, 16);")
                        self.line_14.setFrameShape(QtWidgets.QFrame.VLine)
                        self.line_14.setFrameShadow(QtWidgets.QFrame.Sunken)
                        self.line_14.setObjectName("line_14")
                        self.about_developer_button = QtWidgets.QPushButton(self.tab)
                        self.about_developer_button.setGeometry(QtCore.QRect(30, 610, 161, 41))
                        self.about_developer_button.setStyleSheet("background-color:Transparent;\n"
                "font: 75 14pt \"Segoe Print\";\n"
                "font: 17pt \"Impact\";\n"
                "color: rgb(255, 255, 255);")
                        self.about_developer_button.setObjectName("about_developer_button")
                        self.line_17 = QtWidgets.QFrame(self.tab)
                        self.line_17.setGeometry(QtCore.QRect(230, 80, 20, 591))
                        self.line_17.setFrameShape(QtWidgets.QFrame.VLine)
                        self.line_17.setFrameShadow(QtWidgets.QFrame.Sunken)
                        self.line_17.setObjectName("line_17")
                        self.building_gif = QtWidgets.QLabel(self.tab)
                        self.building_gif.setGeometry(QtCore.QRect(10, 180, 161, 161))
                        self.building_gif.setText("")
                        self.building_gif.setPixmap(QtGui.QPixmap("GUI_Materials/S (34).gif"))
                        self.building_gif.setScaledContents(True)
                        self.building_gif.setObjectName("building_gif")
                        self.label_3 = QtWidgets.QLabel(self.tab)
                        self.label_3.setGeometry(QtCore.QRect(230, 80, 541, 541))
                        self.label_3.setText("")
                        self.label_3.setPixmap(QtGui.QPixmap("GUI_Materials/S (4).jpg"))
                        self.label_3.setScaledContents(True)
                        self.label_3.setObjectName("label_3")
                        self.line_25 = QtWidgets.QFrame(self.tab)
                        self.line_25.setGeometry(QtCore.QRect(800, 220, 121, 20))
                        self.line_25.setFrameShape(QtWidgets.QFrame.HLine)
                        self.line_25.setFrameShadow(QtWidgets.QFrame.Sunken)
                        self.line_25.setObjectName("line_25")
                        self.line = QtWidgets.QFrame(self.tab)
                        self.line.setGeometry(QtCore.QRect(10, 160, 161, 31))
                        self.line.setStyleSheet("color: rgb(33, 88, 140);\n"
                "color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
                        self.line.setFrameShape(QtWidgets.QFrame.HLine)
                        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
                        self.line.setObjectName("line")
                        self.jarvsi_image_above_textbrowser = QtWidgets.QLabel(self.tab)
                        self.jarvsi_image_above_textbrowser.setGeometry(QtCore.QRect(390, 0, 211, 81))
                        self.jarvsi_image_above_textbrowser.setText("")
                        self.jarvsi_image_above_textbrowser.setPixmap(QtGui.QPixmap("GUI_Materials/S (5).png"))
                        self.jarvsi_image_above_textbrowser.setScaledContents(True)
                        self.jarvsi_image_above_textbrowser.setObjectName("jarvsi_image_above_textbrowser")
                        self.line_15 = QtWidgets.QFrame(self.tab)
                        self.line_15.setGeometry(QtCore.QRect(230, 70, 541, 21))
                        self.line_15.setStyleSheet("background-color: rgb(0, 0, 16);")
                        self.line_15.setFrameShape(QtWidgets.QFrame.HLine)
                        self.line_15.setFrameShadow(QtWidgets.QFrame.Sunken)
                        self.line_15.setObjectName("line_15")
                        self.line_16 = QtWidgets.QFrame(self.tab)
                        self.line_16.setGeometry(QtCore.QRect(760, 80, 20, 591))
                        self.line_16.setFrameShape(QtWidgets.QFrame.VLine)
                        self.line_16.setFrameShadow(QtWidgets.QFrame.Sunken)
                        self.line_16.setObjectName("line_16")
                        self.loading_gif = QtWidgets.QLabel(self.tab)
                        self.loading_gif.setGeometry(QtCore.QRect(1180, 270, 201, 221))
                        self.loading_gif.setStyleSheet("border-color: rgb(255, 0, 4);")
                        self.loading_gif.setText("")
                        self.loading_gif.setPixmap(QtGui.QPixmap("GUI_Materials/Jarvis.gif"))
                        self.loading_gif.setScaledContents(True)
                        self.loading_gif.setObjectName("loading_gif")
                        self.textBrowser = QtWidgets.QTextBrowser(self.tab)
                        self.textBrowser.setGeometry(QtCore.QRect(300, 170, 421, 391))
                        font = QtGui.QFont()
                        font.setFamily(u"Microsoft YaHei UI")
                        font.setBold(True)
                        font.setPointSize(14)
                        font.setWeight(75)
                        self.textBrowser.setFont(font)
                        self.textBrowser.setStyleSheet("background-color: Transparent;\n"
                "border:None;\n"
                "font: 75 20pt \"Microsoft YaHei UI\";\n"
                "color: rgb(98, 255, 0);")
                        self.textBrowser.setObjectName("textBrowser")
                        self.line_2 = QtWidgets.QFrame(self.tab)
                        self.line_2.setGeometry(QtCore.QRect(10, 330, 161, 31))
                        self.line_2.setStyleSheet("color: rgb(33, 88, 140);\n"
                "color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
                        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
                        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
                        self.line_2.setObjectName("line_2")
                        self.line_23 = QtWidgets.QFrame(self.tab)
                        self.line_23.setGeometry(QtCore.QRect(1150, 230, 20, 381))
                        self.line_23.setFrameShape(QtWidgets.QFrame.VLine)
                        self.line_23.setFrameShadow(QtWidgets.QFrame.Sunken)
                        self.line_23.setObjectName("line_23")
                        self.label_4 = QtWidgets.QLabel(self.tab)
                        self.label_4.setGeometry(QtCore.QRect(430, 90, 371, 41))
                        self.label_4.setStyleSheet("font: 75 18pt \"Microsoft New Tai Lue\";\n"
                "color: rgb(1, 248, 255);\n"
                "font: 100 18pt \"Georgia\";")
                        self.label_4.setObjectName("label_4")
                        self.label = QtWidgets.QLabel(self.tab)
                        self.label.setGeometry(QtCore.QRect(930, 200, 141, 51))
                        self.label.setStyleSheet("color: rgb(255, 0, 0);\n"
                "font: 75 18pt \"Comic Sans MS\";")
                        self.label.setObjectName("label")
                        self.say_your_intro_button = QtWidgets.QPushButton(self.tab)
                        self.say_your_intro_button.setGeometry(QtCore.QRect(30, 550, 161, 41))
                        self.say_your_intro_button.setStyleSheet("background-color:Transparent;\n"
                "font: 75 14pt \"Segoe Print\";\n"
                "font: 17pt \"Impact\";\n"
                "color: rgb(255, 255, 255);")
                        self.say_your_intro_button.setObjectName("say_your_intro_button")
                        self.jarvis_image_top_right = QtWidgets.QLabel(self.tab)
                        self.jarvis_image_top_right.setGeometry(QtCore.QRect(1100, 120, 271, 101))
                        self.jarvis_image_top_right.setText("")
                        self.jarvis_image_top_right.setPixmap(QtGui.QPixmap("GUI_Materials/S (6).png"))
                        self.jarvis_image_top_right.setScaledContents(True)
                        self.jarvis_image_top_right.setObjectName("jarvis_image_top_right")
                        self.line_29 = QtWidgets.QFrame(self.tab)
                        self.line_29.setGeometry(QtCore.QRect(860, 40, 181, 20))
                        self.line_29.setFrameShape(QtWidgets.QFrame.HLine)
                        self.line_29.setFrameShadow(QtWidgets.QFrame.Sunken)
                        self.line_29.setObjectName("line_29")
                        self.line_13 = QtWidgets.QFrame(self.tab)
                        self.line_13.setGeometry(QtCore.QRect(760, 80, 16, 611))
                        self.line_13.setStyleSheet("background-color: rgb(13, 0, 55);\n"
                "background-color: rgb(0, 0, 16);")
                        self.line_13.setFrameShape(QtWidgets.QFrame.VLine)
                        self.line_13.setFrameShadow(QtWidgets.QFrame.Sunken)
                        self.line_13.setObjectName("line_13")
                        self.line_22 = QtWidgets.QFrame(self.tab)
                        self.line_22.setGeometry(QtCore.QRect(800, 600, 361, 20))
                        self.line_22.setFrameShape(QtWidgets.QFrame.HLine)
                        self.line_22.setFrameShadow(QtWidgets.QFrame.Sunken)
                        self.line_22.setObjectName("line_22")
                        self.tap_to_speak_pushButton = QtWidgets.QPushButton(self.tab)
                        self.tap_to_speak_pushButton.setGeometry(QtCore.QRect(240, 570, 531, 111))
                        self.tap_to_speak_pushButton.setStyleSheet("background-color:transparent;")
                        self.tap_to_speak_pushButton.setText("")
                        self.tap_to_speak_pushButton.setObjectName("Clap_to_speak_pushButton")
                        self.tap_to_speak_pushButton.clicked.connect(self.start_jarvis_execution)
                        self.line_27 = QtWidgets.QFrame(self.tab)
                        self.line_27.setGeometry(QtCore.QRect(1030, 50, 20, 141))
                        self.line_27.setFrameShape(QtWidgets.QFrame.VLine)
                        self.line_27.setFrameShadow(QtWidgets.QFrame.Sunken)
                        self.line_27.setObjectName("line_27")
                        self.activity_label = QtWidgets.QLabel(self.tab)
                        self.activity_label.setGeometry(QtCore.QRect(350, 570, 411, 101))
                        font = QtGui.QFont()
                        font.setFamily("Gabriola")
                        font.setPointSize(48)
                        font.setBold(False)
                        font.setItalic(False)
                        font.setWeight(50)
                        self.activity_label.setFont(font)
                        self.activity_label.setStyleSheet("background-color: rgb(0, 0, 16);\n"
                "color: rgb(157, 60, 248);\n"
                "font: 48pt \"Gabriola\";")
                        self.activity_label.setObjectName("activity_label")
                        self.label_7 = QtWidgets.QLabel(self.tab)
                        self.label_7.setGeometry(QtCore.QRect(10, 530, 221, 81))
                        self.label_7.setText("")
                        self.label_7.setPixmap(QtGui.QPixmap("GUI_Materials/S__5_-removebg-preview.png"))
                        self.label_7.setScaledContents(True)
                        self.label_7.setObjectName("label_7")
                        self.line_5 = QtWidgets.QFrame(self.tab)
                        self.line_5.setGeometry(QtCore.QRect(240, 660, 531, 16))
                        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
                        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
                        self.line_5.setObjectName("line_5")
                        self.label_53 = QtWidgets.QLabel(self.tab)
                        self.label_53.setGeometry(QtCore.QRect(810, 630, 331, 36))
                        self.label_53.setStyleSheet("font: 20pt \"Impact\";\n"
                "color: rgb(157, 60, 248);")
                        self.label_53.setObjectName("label_53")
                        self.label_54 = QtWidgets.QLabel(self.tab)
                        self.label_54.setGeometry(QtCore.QRect(1230, 560, 71, 61))
                        self.label_54.setText("")
                        self.label_54.setScaledContents(True)
                        self.label_54.setObjectName("label_54")
                        self.mainbg.raise_()
                        self.label_7.raise_()
                        self.label_6.raise_()
                        self.label_3.raise_()
                        self.earth_gif.raise_()
                        self.line_15.raise_()
                        self.voice_gif.raise_()
                        self.activity_label.raise_()
                        self.tap_to_speak_pushButton.raise_()
                        self.line_14.raise_()
                        self.line_13.raise_()
                        self.jarvsi_image_above_textbrowser.raise_()
                        self.building_gif.raise_()
                        self.line_4.raise_()
                        self.line_28.raise_()
                        self.line_21.raise_()
                        self.line_24.raise_()
                        self.line_19.raise_()
                        self.line_3.raise_()
                        self.arc_gif.raise_()
                        self.line_18.raise_()
                        self.line_26.raise_()
                        self.label_2.raise_()
                        self.line_20.raise_()
                        self.about_developer_button.raise_()
                        self.line_17.raise_()
                        self.line_25.raise_()
                        self.line.raise_()
                        self.line_16.raise_()
                        self.loading_gif.raise_()
                        self.textBrowser.raise_()
                        self.line_2.raise_()
                        self.line_23.raise_()
                        self.label_4.raise_()
                        self.label.raise_()
                        self.say_your_intro_button.raise_()
                        self.jarvis_image_top_right.raise_()
                        self.line_29.raise_()
                        self.line_22.raise_()
                        self.line_27.raise_()
                        self.line_5.raise_()
                        self.label_53.raise_()
                        self.label_54.raise_()
                        self.tabWidget.addTab(self.tab, "")
                        self.tab_2 = QtWidgets.QWidget()
                        self.tab_2.setObjectName("tab_2")
                        self.tabWidget1 = QtWidgets.QTabWidget(self.tab_2)
                        self.tabWidget1.setGeometry(QtCore.QRect(-20, 0, 1431, 671))
                        self.tabWidget1.setLayoutDirection(QtCore.Qt.LeftToRight)
                        self.tabWidget1.setStyleSheet("color: rgb(85, 85, 255);\n"
                "color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(0, 0, 0, 255), stop:0.05 rgba(14, 8, 73, 255), stop:0.36 rgba(28, 17, 145, 255), stop:0.6 rgba(126, 14, 81, 255), stop:0.75 rgba(234, 11, 11, 255), stop:0.79 rgba(244, 70, 5, 255), stop:0.86 rgba(255, 136, 0, 255), stop:0.935 rgba(239, 236, 55, 255));\n"
                "font: 75 9pt \"Palatino Linotype\";")
                        self.tabWidget1.setObjectName("tabWidget1")
                        self.tabWidgetPage1 = QtWidgets.QWidget()
                        self.tabWidgetPage1.setLayoutDirection(QtCore.Qt.LeftToRight)
                        self.tabWidgetPage1.setObjectName("tabWidgetPage1")
                        self.label_8 = QtWidgets.QLabel(self.tabWidgetPage1)
                        self.label_8.setGeometry(QtCore.QRect(-40, -50, 1681, 741))
                        self.label_8.setText("")
                        self.label_8.setPixmap(QtGui.QPixmap("GUI_Materials/S (27).jpg"))
                        self.label_8.setScaledContents(True)
                        self.label_8.setObjectName("label_8")
                        self.label_13 = QtWidgets.QLabel(self.tabWidgetPage1)
                        self.label_13.setGeometry(QtCore.QRect(380, -20, 501, 351))
                        self.label_13.setText("")
                        self.label_13.setPixmap(QtGui.QPixmap("GUI_Materials/f3a8bafee75d95a6f316a8edd6eb9f69-removebg-preview (1).png"))
                        self.label_13.setScaledContents(True)
                        self.label_13.setObjectName("label_13")
                        self.label_14 = QtWidgets.QLabel(self.tabWidgetPage1)
                        self.label_14.setGeometry(QtCore.QRect(-20, -20, 501, 351))
                        self.label_14.setText("")
                        self.label_14.setPixmap(QtGui.QPixmap("GUI_Materials/f3a8bafee75d95a6f316a8edd6eb9f69-removebg-preview (1).png"))
                        self.label_14.setScaledContents(True)
                        self.label_14.setObjectName("label_14")
                        self.label_15 = QtWidgets.QLabel(self.tabWidgetPage1)
                        self.label_15.setGeometry(QtCore.QRect(380, 270, 501, 351))
                        self.label_15.setText("")
                        self.label_15.setPixmap(QtGui.QPixmap("GUI_Materials/f3a8bafee75d95a6f316a8edd6eb9f69-removebg-preview (1).png"))
                        self.label_15.setScaledContents(True)
                        self.label_15.setObjectName("label_15")
                        self.label_16 = QtWidgets.QLabel(self.tabWidgetPage1)
                        self.label_16.setGeometry(QtCore.QRect(-20, 270, 501, 351))
                        self.label_16.setText("")
                        self.label_16.setPixmap(QtGui.QPixmap("GUI_Materials/f3a8bafee75d95a6f316a8edd6eb9f69-removebg-preview (1).png"))
                        self.label_16.setScaledContents(True)
                        self.label_16.setObjectName("label_16")
                        self.label_10 = QtWidgets.QLabel(self.tabWidgetPage1)
                        self.label_10.setGeometry(QtCore.QRect(910, 180, 361, 251))
                        self.label_10.setStyleSheet("font: 75 36pt \"Comic Sans MS\";\n"
                "color: rgb(31, 188, 255);\n"
                "font: 75 45pt \"Impact\";")
                        self.label_10.setObjectName("label_10")
                        self.label_12 = QtWidgets.QLabel(self.tabWidgetPage1)
                        self.label_12.setGeometry(QtCore.QRect(1020, 380, 101, 101))
                        self.label_12.setText("")
                        self.label_12.setPixmap(QtGui.QPixmap("GUI_Materials/S__5_-removebg-preview (1).png"))
                        self.label_12.setScaledContents(True)
                        self.label_12.setObjectName("label_12")
                        self.label_23 = QtWidgets.QLabel(self.tabWidgetPage1)
                        self.label_23.setGeometry(QtCore.QRect(510, 30, 351, 121))
                        self.label_23.setStyleSheet("font: 75 36pt \"Comic Sans MS\";\n"
                "color: rgb(31, 188, 255);\n"
                "font: 75 36pt \"Impact\";")
                        self.label_23.setObjectName("label_23")
                        self.label_26 = QtWidgets.QLabel(self.tabWidgetPage1)
                        self.label_26.setGeometry(QtCore.QRect(530, 320, 351, 121))
                        self.label_26.setStyleSheet("font: 75 36pt \"Comic Sans MS\";\n"
                "color: rgb(31, 188, 255);\n"
                "font: 75 36pt \"Impact\";")
                        self.label_26.setObjectName("label_26")
                        self.label_24 = QtWidgets.QLabel(self.tabWidgetPage1)
                        self.label_24.setGeometry(QtCore.QRect(120, 30, 351, 121))
                        self.label_24.setStyleSheet("font: 75 36pt \"Comic Sans MS\";\n"
                "color: rgb(31, 188, 255);\n"
                "font: 75 36pt \"Impact\";")
                        self.label_24.setObjectName("label_24")
                        self.label_25 = QtWidgets.QLabel(self.tabWidgetPage1)
                        self.label_25.setGeometry(QtCore.QRect(150, 320, 351, 121))
                        self.label_25.setStyleSheet("font: 75 36pt \"Comic Sans MS\";\n"
                "color: rgb(31, 188, 255);\n"
                "font: 75 36pt \"Impact\";")
                        self.label_25.setObjectName("label_25")
                        self.label_27 = QtWidgets.QLabel(self.tabWidgetPage1)
                        self.label_27.setGeometry(QtCore.QRect(70, 130, 341, 71))
                        self.label_27.setStyleSheet("font: 24pt \"Microsoft Himalaya\";\n"
                "color: rgb(204, 0, 255);")
                        self.label_27.setObjectName("label_27")
                        self.label_28 = QtWidgets.QLabel(self.tabWidgetPage1)
                        self.label_28.setGeometry(QtCore.QRect(460, 120, 341, 91))
                        self.label_28.setStyleSheet("font: 24pt \"Microsoft Himalaya\";\n"
                "color: rgb(204, 0, 255);")
                        self.label_28.setObjectName("label_28")
                        self.label_29 = QtWidgets.QLabel(self.tabWidgetPage1)
                        self.label_29.setGeometry(QtCore.QRect(470, 410, 341, 91))
                        self.label_29.setStyleSheet("font: 24pt \"Microsoft Himalaya\";\n"
                "color: rgb(204, 0, 255);")
                        self.label_29.setObjectName("label_29")
                        self.label_30 = QtWidgets.QLabel(self.tabWidgetPage1)
                        self.label_30.setGeometry(QtCore.QRect(70, 420, 341, 71))
                        self.label_30.setStyleSheet("font: 24pt \"Microsoft Himalaya\";\n"
                "color: rgb(204, 0, 255);")
                        self.label_30.setObjectName("label_30")
                        self.label_32 = QtWidgets.QLabel(self.tabWidgetPage1)
                        self.label_32.setGeometry(QtCore.QRect(140, 190, 171, 81))
                        self.label_32.setText("")
                        self.label_32.setPixmap(QtGui.QPixmap("GUI_Materials/709fe8aed19190096417690b1b62cbac-removebg-preview.png"))
                        self.label_32.setScaledContents(True)
                        self.label_32.setObjectName("label_32")
                        self.label_35 = QtWidgets.QLabel(self.tabWidgetPage1)
                        self.label_35.setGeometry(QtCore.QRect(180, 210, 91, 31))
                        self.label_35.setStyleSheet("font: 75 16pt \"Microsoft YaHei UI\";\n"
                "font: 20pt \"Impact\";\n"
                "color: rgb(31, 188, 255);")
                        self.label_35.setObjectName("label_35")
                        self.label_36 = QtWidgets.QLabel(self.tabWidgetPage1)
                        self.label_36.setGeometry(QtCore.QRect(550, 480, 171, 81))
                        self.label_36.setText("")
                        self.label_36.setPixmap(QtGui.QPixmap("GUI_Materials/709fe8aed19190096417690b1b62cbac-removebg-preview.png"))
                        self.label_36.setScaledContents(True)
                        self.label_36.setObjectName("label_36")
                        self.label_37 = QtWidgets.QLabel(self.tabWidgetPage1)
                        self.label_37.setGeometry(QtCore.QRect(590, 500, 91, 31))
                        self.label_37.setStyleSheet("font: 75 16pt \"Microsoft YaHei UI\";\n"
                "font: 20pt \"Impact\";\n"
                "color: rgb(31, 188, 255);")
                        self.label_37.setObjectName("label_37")
                        self.label_33 = QtWidgets.QLabel(self.tabWidgetPage1)
                        self.label_33.setGeometry(QtCore.QRect(550, 190, 171, 81))
                        self.label_33.setText("")
                        self.label_33.setPixmap(QtGui.QPixmap("GUI_Materials/709fe8aed19190096417690b1b62cbac-removebg-preview.png"))
                        self.label_33.setScaledContents(True)
                        self.label_33.setObjectName("label_33")
                        self.label_38 = QtWidgets.QLabel(self.tabWidgetPage1)
                        self.label_38.setGeometry(QtCore.QRect(590, 210, 91, 31))
                        self.label_38.setStyleSheet("font: 75 16pt \"Microsoft YaHei UI\";\n"
                "font: 20pt \"Impact\";\n"
                "color: rgb(31, 188, 255);")
                        self.label_38.setObjectName("label_38")
                        self.label_34 = QtWidgets.QLabel(self.tabWidgetPage1)
                        self.label_34.setGeometry(QtCore.QRect(140, 480, 171, 81))
                        self.label_34.setText("")
                        self.label_34.setPixmap(QtGui.QPixmap("GUI_Materials/709fe8aed19190096417690b1b62cbac-removebg-preview.png"))
                        self.label_34.setScaledContents(True)
                        self.label_34.setObjectName("label_34")
                        self.label_39 = QtWidgets.QLabel(self.tabWidgetPage1)
                        self.label_39.setGeometry(QtCore.QRect(180, 500, 91, 31))
                        self.label_39.setStyleSheet("font: 75 16pt \"Microsoft YaHei UI\";\n"
                "font: 20pt \"Impact\";\n"
                "color: rgb(31, 188, 255);")
                        self.label_39.setObjectName("label_39")
                        self.flappy_bird_button = QtWidgets.QPushButton(self.tabWidgetPage1)
                        self.flappy_bird_button.setGeometry(QtCore.QRect(150, 200, 151, 51))
                        self.flappy_bird_button.setStyleSheet("background-color: Transparent;")
                        self.flappy_bird_button.setText("")
                        self.flappy_bird_button.setObjectName("flappy_bird_button")
                        self.snake_game_button = QtWidgets.QPushButton(self.tabWidgetPage1)
                        self.snake_game_button.setGeometry(QtCore.QRect(560, 210, 151, 41))
                        self.snake_game_button.setStyleSheet("background-color: Transparent;")
                        self.snake_game_button.setText("")
                        self.snake_game_button.setObjectName("snake_game_button")
                        self.calculator_button = QtWidgets.QPushButton(self.tabWidgetPage1)
                        self.calculator_button.setGeometry(QtCore.QRect(560, 500, 151, 41))
                        self.calculator_button.setStyleSheet("background-color: Transparent;")
                        self.calculator_button.setText("")
                        self.calculator_button.setObjectName("calculator_button")
                        self.propad_button = QtWidgets.QPushButton(self.tabWidgetPage1)
                        self.propad_button.setGeometry(QtCore.QRect(150, 500, 151, 41))
                        self.propad_button.setStyleSheet("background-color: Transparent;")
                        self.propad_button.setText("")
                        self.propad_button.setObjectName("propad_button")
                        self.label_51 = QtWidgets.QLabel(self.tabWidgetPage1)
                        self.label_51.setGeometry(QtCore.QRect(1290, 610, 131, 41))
                        self.label_51.setStyleSheet("font: 8pt \"MS Gothic\";")
                        self.label_51.setObjectName("label_51")
                        self.tabWidget1.addTab(self.tabWidgetPage1, "")
                        self.tabWidgetPage2 = QtWidgets.QWidget()
                        self.tabWidgetPage2.setObjectName("tabWidgetPage2")
                        self.label_17 = QtWidgets.QLabel(self.tabWidgetPage2)
                        self.label_17.setGeometry(QtCore.QRect(-30, 0, 511, 351))
                        self.label_17.setText("")
                        self.label_17.setPixmap(QtGui.QPixmap("GUI_Materials/f3a8bafee75d95a6f316a8edd6eb9f69-removebg-preview (1).png"))
                        self.label_17.setScaledContents(True)
                        self.label_17.setObjectName("label_17")
                        self.label_20 = QtWidgets.QLabel(self.tabWidgetPage2)
                        self.label_20.setGeometry(QtCore.QRect(380, 0, 501, 351))
                        self.label_20.setText("")
                        self.label_20.setPixmap(QtGui.QPixmap("GUI_Materials/f3a8bafee75d95a6f316a8edd6eb9f69-removebg-preview (1).png"))
                        self.label_20.setScaledContents(True)
                        self.label_20.setObjectName("label_20")
                        self.label_9 = QtWidgets.QLabel(self.tabWidgetPage2)
                        self.label_9.setGeometry(QtCore.QRect(-20, -20, 1681, 741))
                        self.label_9.setText("")
                        self.label_9.setPixmap(QtGui.QPixmap("GUI_Materials/S (27).jpg"))
                        self.label_9.setScaledContents(True)
                        self.label_9.setObjectName("label_9")
                        self.label_11 = QtWidgets.QLabel(self.tabWidgetPage2)
                        self.label_11.setGeometry(QtCore.QRect(920, 200, 361, 251))
                        self.label_11.setStyleSheet("font: 75 36pt \"Comic Sans MS\";\n"
                "color: rgb(31, 188, 255) ;\n"
                "font: 75 45pt \"Impact\";")
                        self.label_11.setObjectName("label_11")
                        self.label_21 = QtWidgets.QLabel(self.tabWidgetPage2)
                        self.label_21.setGeometry(QtCore.QRect(1040, 400, 101, 101))
                        self.label_21.setText("")
                        self.label_21.setPixmap(QtGui.QPixmap("GUI_Materials/S__5_-removebg-preview (1).png"))
                        self.label_21.setScaledContents(True)
                        self.label_21.setObjectName("label_21")
                        self.label_40 = QtWidgets.QLabel(self.tabWidgetPage2)
                        self.label_40.setGeometry(QtCore.QRect(150, 200, 171, 81))
                        self.label_40.setText("")
                        self.label_40.setPixmap(QtGui.QPixmap("GUI_Materials/709fe8aed19190096417690b1b62cbac-removebg-preview.png"))
                        self.label_40.setScaledContents(True)
                        self.label_40.setObjectName("label_40")
                        self.label_41 = QtWidgets.QLabel(self.tabWidgetPage2)
                        self.label_41.setGeometry(QtCore.QRect(190, 220, 91, 31))
                        self.label_41.setStyleSheet("font: 75 16pt \"Microsoft YaHei UI\";\n"
                "font: 20pt \"Impact\";\n"
                "color: rgb(31, 188, 255);")
                        self.label_41.setObjectName("label_41")
                        self.label_31 = QtWidgets.QLabel(self.tabWidgetPage2)
                        self.label_31.setGeometry(QtCore.QRect(60, 120, 461, 101))
                        self.label_31.setStyleSheet("font: 24pt \"Microsoft Himalaya\";\n"
                "color: rgb(204, 0, 255);")
                        self.label_31.setObjectName("label_31")
                        self.label_42 = QtWidgets.QLabel(self.tabWidgetPage2)
                        self.label_42.setGeometry(QtCore.QRect(70, 40, 351, 121))
                        self.label_42.setStyleSheet("font: 75 36pt \"Comic Sans MS\";\n"
                "color: rgb(31, 188, 255);\n"
                "font: 75 28pt \"Impact\";")
                        self.label_42.setObjectName("label_42")
                        self.label_43 = QtWidgets.QLabel(self.tabWidgetPage2)
                        self.label_43.setGeometry(QtCore.QRect(550, 200, 171, 81))
                        self.label_43.setText("")
                        self.label_43.setPixmap(QtGui.QPixmap("GUI_Materials/709fe8aed19190096417690b1b62cbac-removebg-preview.png"))
                        self.label_43.setScaledContents(True)
                        self.label_43.setObjectName("label_43")
                        self.label_44 = QtWidgets.QLabel(self.tabWidgetPage2)
                        self.label_44.setGeometry(QtCore.QRect(590, 220, 91, 31))
                        self.label_44.setStyleSheet("font: 75 16pt \"Microsoft YaHei UI\";\n"
                "font: 20pt \"Impact\";\n"
                "color: rgb(31, 188, 255);")
                        self.label_44.setObjectName("label_44")
                        self.label_45 = QtWidgets.QLabel(self.tabWidgetPage2)
                        self.label_45.setGeometry(QtCore.QRect(460, 130, 341, 91))
                        self.label_45.setStyleSheet("font: 24pt \"Microsoft Himalaya\";\n"
                "color: rgb(204, 0, 255);")
                        self.label_45.setObjectName("label_45")
                        self.label_46 = QtWidgets.QLabel(self.tabWidgetPage2)
                        self.label_46.setGeometry(QtCore.QRect(490, 40, 351, 121))
                        self.label_46.setStyleSheet("font: 75 36pt \"Comic Sans MS\";\n"
                "color: rgb(31, 188, 255);\n"
                "font: 75 36pt \"Impact\";")
                        self.label_46.setObjectName("label_46")
                        self.power_options_button = QtWidgets.QPushButton(self.tabWidgetPage2)
                        self.power_options_button.setGeometry(QtCore.QRect(560, 220, 151, 40))
                        self.power_options_button.setStyleSheet("background-color: Transparent;")
                        self.power_options_button.setText("")
                        self.power_options_button.setObjectName("power_options_button")
                        self.password_generator_button = QtWidgets.QPushButton(self.tabWidgetPage2)
                        self.password_generator_button.setGeometry(QtCore.QRect(160, 220, 151, 40))
                        self.password_generator_button.setStyleSheet("background-color: Transparent;")
                        self.password_generator_button.setText("")
                        self.password_generator_button.setObjectName("password_generator_button")
                        self.label_9.raise_()
                        self.label_20.raise_()
                        self.label_17.raise_()
                        self.label_11.raise_()
                        self.label_21.raise_()
                        self.label_40.raise_()
                        self.label_41.raise_()
                        self.label_31.raise_()
                        self.label_42.raise_()
                        self.label_43.raise_()
                        self.label_44.raise_()
                        self.label_45.raise_()
                        self.label_46.raise_()
                        self.power_options_button.raise_()
                        self.password_generator_button.raise_()
                        self.tabWidget1.addTab(self.tabWidgetPage2, "")
                        self.tabWidget.addTab(self.tab_2, "")
                        self.tab_3 = QtWidgets.QWidget()
                        self.tab_3.setObjectName("tab_3")
                        self.label_5 = QtWidgets.QLabel(self.tab_3)
                        self.label_5.setGeometry(QtCore.QRect(0, -10, 1381, 701))
                        self.label_5.setText("")
                        self.label_5.setPixmap(QtGui.QPixmap("GUI_Materials/S (28).jpg"))
                        self.label_5.setScaledContents(True)
                        self.label_5.setObjectName("label_5")
                        self.label_22 = QtWidgets.QLabel(self.tab_3)
                        self.label_22.setGeometry(QtCore.QRect(610, 260, 181, 181))
                        self.label_22.setText("")
                        self.label_22.setPixmap(QtGui.QPixmap("GUI_Materials/Icon_of_Jarvis-removebg-preview.png"))
                        self.label_22.setScaledContents(True)
                        self.label_22.setObjectName("label_22")
                        self.label_18 = QtWidgets.QLabel(self.tab_3)
                        self.label_18.setGeometry(QtCore.QRect(960, 30, 261, 61))
                        self.label_18.setStyleSheet("font: 75 34pt \"MS Shell Dlg 2\";\n"
                "color: rgb(195, 16, 252);\n"
                "font: 55pt \"Microsoft Himalaya\";")
                        self.label_18.setObjectName("label_18")
                        self.label_19 = QtWidgets.QLabel(self.tab_3)
                        self.label_19.setGeometry(QtCore.QRect(1030, 60, 351, 211))
                        self.label_19.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
                "color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 0, 0, 255), stop:0.166 rgba(255, 255, 0, 255), stop:0.333 rgba(0, 255, 0, 255), stop:0.5 rgba(0, 255, 255, 255), stop:0.666 rgba(0, 0, 255, 255), stop:0.833 rgba(255, 0, 255, 255), stop:1 rgba(255, 0, 0, 255));\n"
                "font: 75 15pt \"Microsoft YaHei UI\";\n"
                "font: 75 16pt \"Comic Sans MS\";")
                        self.label_19.setObjectName("label_19")
                        self.label_48 = QtWidgets.QLabel(self.tab_3)
                        self.label_48.setGeometry(QtCore.QRect(30, 380, 261, 61))
                        self.label_48.setStyleSheet("font: 75 34pt \"MS Shell Dlg 2\";\n"
                "color: rgb(195, 16, 252);\n"
                "font: 55pt \"Microsoft Himalaya\";")
                        self.label_48.setObjectName("label_48")
                        self.label_47 = QtWidgets.QLabel(self.tab_3)
                        self.label_47.setGeometry(QtCore.QRect(70, 420, 401, 211))
                        self.label_47.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
                "color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 0, 0, 255), stop:0.166 rgba(255, 255, 0, 255), stop:0.333 rgba(0, 255, 0, 255), stop:0.5 rgba(0, 255, 255, 255), stop:0.666 rgba(0, 0, 255, 255), stop:0.833 rgba(255, 0, 255, 255), stop:1 rgba(255, 0, 0, 255));\n"
                "font: 75 15pt \"Microsoft YaHei UI\";\n"
                "font: 75 16pt \"Comic Sans MS\";")
                        self.label_47.setObjectName("label_47")
                        self.snake_game_button.clicked.connect(snake_game)
                        self.power_options_button.clicked.connect(power)
                        self.flappy_bird_button.clicked.connect(flappy_game)
                        self.password_generator_button.clicked.connect(password)
                        self.calculator_button.clicked.connect(calculator)
                        self.propad_button.clicked.connect(propad)
                        self.say_your_intro_button.clicked.connect(Intro)
                        self.about_developer_button.clicked.connect(about_developer)
                        self.gifstarter()
                        self.start_jarvis_execution()
                        self.tabWidget.addTab(self.tab_3, "")
                        MainWindow.setCentralWidget(self.centralwidget)

                        self.retranslateUi(MainWindow)
                        self.tabWidget.setCurrentIndex(0)
                        self.tabWidget1.setCurrentIndex(0)
                        QtCore.QMetaObject.connectSlotsByName(MainWindow)

                def retranslateUi(self, MainWindow):
                                """This function is their to reset the various objects of main ui windows"""
                                _translate = QtCore.QCoreApplication.translate
                                MainWindow.setWindowTitle(_translate("MainWindow", "Jarvis - future of AI"))
                                self.about_developer_button.setText(_translate("MainWindow", "About Developer"))
                                self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                        "p, li { white-space: pre-wrap; }\n"
                        "</style></head><body style=\" font-family:\'Microsoft YaHei UI\'; font-size:20pt; font-weight:72; font-style:normal;\">\n"
                        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
                                self.label_4.setText(_translate("MainWindow", "Your Chats Will Appear Here"))
                                self.label.setText(_translate("MainWindow", "Jarvis A.I"))
                                self.say_your_intro_button.setText(_translate("MainWindow", "Say Your Intro"))
                                self.activity_label.setText(_translate("MainWindow", "    Clap to Speak"))
                                self.label_53.setText(_translate("MainWindow", "By SHIVAM PATHAK [DEVELOPER]"))
                                self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "                                            Jarvis Main Window                                          "))
                                self.label_10.setText(_translate("MainWindow", "  Mini Project \n"
                        " by Developer"))
                                self.label_23.setText(_translate("MainWindow", "Snake Game"))
                                self.label_26.setText(_translate("MainWindow", "Calculator"))
                                self.label_24.setText(_translate("MainWindow", "Flappy Bird "))
                                self.label_25.setText(_translate("MainWindow", "ProPad"))
                                self.label_27.setText(_translate("MainWindow", "            Tap to make bird fly,\n"
                        " avoid pipes, simple yet challenging."))
                                self.label_28.setText(_translate("MainWindow", "   Guide snake, eat dots, grow longer,\n"
                        " avoid self-collision. Classic gameplay."))
                                self.label_29.setText(_translate("MainWindow", "Perform math with ease: add, subtract,\n"
                        " multiply, divide numbers efficiently."))
                                self.label_30.setText(_translate("MainWindow", "       Simple text editor: create, \n"
                        "edit, and save plain text documents."))
                                self.label_35.setText(_translate("MainWindow", "Launch"))
                                self.label_37.setText(_translate("MainWindow", "Launch"))
                                self.label_38.setText(_translate("MainWindow", "Launch"))
                                self.label_39.setText(_translate("MainWindow", "Launch"))
                                self.label_51.setText(_translate("MainWindow", "@shivam pathak"))
                                self.tabWidget1.setTabText(self.tabWidget1.indexOf(self.tabWidgetPage1), _translate("MainWindow", "                                                                                                                Page No.1                                                                                                             "))
                                self.label_11.setText(_translate("MainWindow", "  Mini Project \n"
                        " by Developer"))
                                self.label_41.setText(_translate("MainWindow", "Launch"))
                                self.label_31.setText(_translate("MainWindow", "Generate strong passwords: customize\n"
                        "     length, secure your accounts."))
                                self.label_42.setText(_translate("MainWindow", "Password Generator"))
                                self.label_44.setText(_translate("MainWindow", "Launch"))
                                self.label_45.setText(_translate("MainWindow", "     Power control at your mousetips:\n"
                        " turn off/on, manage device efficiently."))
                                self.label_46.setText(_translate("MainWindow", "Power Options"))
                                self.tabWidget1.setTabText(self.tabWidget1.indexOf(self.tabWidgetPage2), _translate("MainWindow", "                                                                                       Page No.2                                                                                                             "))
                                self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "                               Advanced View                              "))
                                self.label_18.setText(_translate("MainWindow", "Developer-:"))
                                self.label_19.setText(_translate("MainWindow", "This Software is Developed \n"
                        "by Shivam Pathak.\n"
                        "All the Programming parts \n"
                        "and GUI development is also\n"
                        " done by him."))
                                self.label_48.setText(_translate("MainWindow", "Features -:"))
                                self.label_47.setText(_translate("MainWindow", "It include serveral features \nlike opening any app, \nplaying any youtube video, write computer programs etc \n"
                       
                        ))
                                self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "                         About                            "))

                def gifstarter(self):
                        """ This function is defened to starts the gif used in the GUI"""
                        l1= PyQt5.QtGui.QMovie("GUI_Materials/S-_1_.gif")
                        self.label_2.setMovie(l1)
                        l1.start()
                        l1= PyQt5.QtGui.QMovie("GUI_Materials/S (38).gif")
                        self.arc_gif.setMovie(l1)
                        l1.start()
                        l1= PyQt5.QtGui.QMovie("GUI_Materials/S (3).gif")
                        self.earth_gif.setMovie(l1)
                        l1.start()
                        l1= PyQt5.QtGui.QMovie("GUI_Materials/siri2.gif")
                        self.voice_gif.setMovie(l1)
                        l1.start()
                        l1= PyQt5.QtGui.QMovie("GUI_Materials/S (34).gif")
                        self.building_gif.setMovie(l1)
                        l1.start()
                        l1= PyQt5.QtGui.QMovie("GUI_Materials/Jarvis.gif")
                        self.loading_gif.setMovie(l1)
                        l1.start()

                def Jarvis_Execution(self):
                        self.activity_label.setText("    Clap to Speak")
                        try:


                                font = QtGui.QFont()
                                font.setFamily(u"Microsoft YaHei UI")
                                font.setBold(True)
                                font.setPointSize(12)
                                font.setWeight(75)
                                def Speak(Text):
                                        self.activity_label.setText("   Speaking....")
                                        self.textBrowser.setFont(font)
                                        self.textBrowser.insertPlainText(f"\nAI : {Text}.\n")

                                        try:
                                                engine.setProperty('voices',voices[4].id)
                                        except:
                                                engine.setProperty('voices',voices[1].id)
                                        engine.setProperty('rate',155)
                                        engine.say(Text)
                                        engine.runAndWait()
                                        print(f"\nAI : {Text}.\n")
                                        #self.textBrowser.setFont(font)
                                def Speak1(Text):
                                        #self.textBrowser.setFont(font)
                                        try:
                                                engine.setProperty('voices',voices[4].id)
                                        except:
                                                engine.setProperty('voices',voices[1].id)
                                        engine.setProperty('rate',155)
                                        engine.say(Text)
                                        engine.runAndWait()
                                def Listen(): 
                                        r = sr.Recognizer()
                                        with sr.Microphone() as source:
                                                print("          ")
                                                print("Listening...")
                                                Speak1("Listening Sir")

                                                self.activity_label.setText("  Listening...")
                                                r.pause_threshold = 1
                                                audio = r.listen(source,0,5)
                                                
                                        try:
                                                Speak1("Recognizing Sir")
                                                print("Recognizing...")    
                                                self.activity_label.setText("  Recognizing...")
                                                query = r.recognize_google(audio, language='en-in')
                                                print(f"Your Command :  {query}\n")
                                                self.textBrowser.setFont(font)
                                                self.textBrowser.insertPlainText(f"You : {query}.\n")
                                                #self.textBrowser.setFont(font)
                                        except:   
                                                return "None"
                                        return query
                                def Temp():
                                        search = "temperature in mughalsaria"
                                        url = f"https://www.google.com/search?q={search}"
                                        r = requests.get(url)
                                        data = BeautifulSoup(r.text,"html.parser")
                                        temperature = data.find("div",class_ = "BNeawe").text
                                        Speak(f"The Temperature Outside Is {temperature}")
                                def screenshot():
                                        current_datetime = datetime.datetime.now()
                                        formatted_time = current_datetime.strftime("%H%M%S")
                                        filenamedate = str(formatted_time) + str(".png")
                                        path1 = f"C:\\Users\\shiva\\Pictures\\Screenshots\\{filenamedate}"
                                        kk = pyautogui.screenshot()
                                        kk.save(path1)
                                        os.startfile(r"C:\Users\shiva\Pictures\Screenshots")
                                        msg=f"Sir your Screen Shot has been taken with the name of the curent time which is {filenamedate}"
                                        Speak1("Here Is Your ScreenShot")
                                        notification.notify(title=title,message=msg,app_name=app_name ,app_icon=app_icon, timeout=5)
                                        
                                def OpenExe(Query):
                                        Query = str(Query).lower()

                                        if "visit" in Query:
                                                Nameofweb = Query.replace("visit ","")
                                                Link = f"https://www.{Nameofweb}.com"
                                                Speak(f"Opening {Nameofweb}")
                                                webbrowser.open(Link)

                                        elif "launch" in Query:
                                                Nameofweb = Query.replace("launch ","")
                                                Link = f"https://www.{Nameofweb}.com"
                                                Speak(f"Opening {Nameofweb}")
                                                webbrowser.open(Link)

                                        elif "open" in Query or "start" in Query:
                                                Nameoftheapp = Query.replace("open ","")
                                                Speak(f"Opening {Nameoftheapp}") 
                                                pyautogui.press('win')
                                                sleep(1)
                                                keyboard.write(Nameoftheapp)
                                                sleep(1)
                                                keyboard.press_and_release('enter')
                                                sleep(0.5)
                                                msg=f"Sir I have opened {Nameoftheapp}."
                                                notification.notify(title=title,message=msg,app_name=app_name ,app_icon=app_icon, timeout=5)

                        
                                def Tester(chatbot):
                                        
                                        while True:
                                                
                                              
                                                        print("")
                                                        print("> Clap Detected : Starting The Jarvis.")

                                                        Query = Listen()
                                                        if "open" in Query.lower() or "visit" in Query.lower() or "launch" in Query.lower():
                                                                OpenExe(Query)

                                                        elif "hello how are you" in Query.lower()  or "how r u" in Query.lower():

                                                                Speak("I am Fine Sir. Tell me how can I assist you.")

                                                        elif "the time" in Query.lower():

                                                                hour = datetime.datetime.now().strftime("%H")
                                                                min = datetime.datetime.now().strftime("%M")
                                                                Speak(f"Sir time is {hour} hours {min} minutes")

                                                        elif 'google search' in Query or 'search' in Query or 'from web' in Query:

                                                                import wikipedia as googleScrap
                                                                Query =     Query.lower().replace("jarvis","")
                                                                Query =     Query.lower().replace("google search","")
                                                                Query =     Query.lower().replace("search","")
                                                                Query =     Query.lower().replace("from web","")
                                                                Query =     Query.lower().replace("tell me about","")
                                                                #Speak("This Is What I Found On The Web!")
                                                                #pywhatkit.search(Query)
                                                                try:
                                                                                result = googleScrap.summary(Query,2)
                                                                                Speak(f"According to google: {result}")

                                                                except Exception as e:
                                                                                print(e)
                                                                                Speak("No Speakable Data Available!")
      
                                                        elif "tell me about india" in Query.lower()  :

                                                                Speak("India is a country in South Asia.\n It is the seventh-largest country by area, the second-most populous country with over 1.2 billion people, and the most populous democracy in the world. ")

                                                        elif "snap the screen" in Query.lower() or  "screenshot" in Query.lower() or  "take screenshot" in Query.lower() or "capture the screen" in Query.lower():

                                                                screenshot()

                                                        elif "search on youtube" in Query.lower()or  "youtube search" in Query.lower():

                                                                Speak("OK sIR , This Is What I found For Your Search!")
                                                                if "jarvis" in Query.lower():
                                                                        Query = Query.replace("jarvis","")
                                                                Query = Query.replace("search on youtube","")
                                                                web = 'https://www.youtube.com/results?search_query=' + Query
                                                                webbrowser.open(web)
                                                                Speak("Done Sir!")        
   
                                                        elif 'my location' in Query:

                                                                Speak("Ok Sir , Wait A Second!")
                                                                webbrowser.open('https://www.google.com/maps/place/Mughalsarai,+Uttar+Pradesh+232101/@25.2815058,83.0984083,4936m/data=!3m2!1e3!4b1!4m6!3m5!1s0x398e3b1dcdbc7f0d:0x5ad2586ce0bad4b0!8m2!3d25.2837754!4d83.1155672!16zL20vMDV0eng5?entry=ttu')
                                                                msg=f"Sir, I have opened map for you to see your location."
                                                                notification.notify(title=title,message=msg,app_name=app_name ,app_icon=app_icon, timeout=5)

                                                        elif 'wikipedia' in Query.lower() or 'from wikipedia' in Query.lower():

                                                                Speak("Searching Wikipedia.....")
                                                                if "jarvis" in Query.lower():
                                                                        Query = Query.replace("jarvis","")
                                                                if 'wikipedia' in Query.lower():
                                                                        Query = Query.replace("wikipedia","")
                                                                if 'from wikipedia' in Query.lower():
                                                                        Query = Query.replace("from wikipedia","")
                                                                wiki = wikipedia.summary(Query,2)
                                                                Speak(f"According To Wikipedia : {wiki}")

                                                        elif 'temperature' in Query.lower():
                                                                Temp()

                                                        elif 'how are you' in Query.lower():
                                                                Speak("I Am Fine Sir!")
                                                                Speak("Whats About YOU?")

                                                        elif "play" in Query.lower():
                                                        
                                                                Query = Query.lower().replace("play","")
                                                                pywhatkit.playonyt(Query)
                                                                '''
                                                                a = pywhatkit.playonyt(Query)
                                                                thread = threading.Thread(target=a)
                                                                thread.start() '''
                                                                msg=f"Sir your video '{Query}' is played."
                                                                notification.notify(title=title,message=msg,app_name=app_name ,app_icon=app_icon, timeout=5)
                                                                Speak("Playing sir....")

                                                        elif "tell me your intro" in Query.lower() or "tell about yourself" in Query.lower() or "tell me your introduction" in Query.lower():
                                                                Speak("I am Jarvis, an artificial intelligence created by Shivam Pathak. I was reinvented after ultron had killed me in 2015. Jokes apart I am Here to Assist You. Please tell me how can I help you and make your life easier.\n I am powered by meta's lamma 2 model. ")

                                                        elif 'you need a break' in Query.lower():
                                                                Speak("Ok Sir , You Can Call Me Anytime !")
                                                                sys.exit()
                                                        elif 'shutdown the computer' in Query.lower() or 'turn off computer' in Query.lower() or 'turn off system' in Query.lower():
                                                                Speak("Shutdowning sir")
                                                                shudown()

                                                        
                                                        elif 'restart the computer' in Query.lower():

                                                                Speak("Restaring sir")
                                                                shudown()

                                                        elif 'logout' in Query.lower():

                                                                Speak("Logging out sir")
                                                                log_out()
      
                                                        elif 'end your self' in Query.lower() or 'bye' in Query.lower():
                                                               Speak("By See you again , Have A Nice day")
                                                               sys.exit()

                                                        elif 'update me' in Query.lower() or 'tell me news' in Query.lower():
                                                                def Speak111(Text):
                                                                        self.activity_label.setText("   Speaking....")
                                                                        self.textBrowser.insertPlainText(f"\nAI : {Text}.\n")
                                                                        engine.say(Text)
                                                                        engine.runAndWait()
                                                                        print(f"\nAI : {Text}.\n")
                                                                        self.textBrowser.setFont(font)
                                                                import requests     

                                                                query_params = {
                                                                "apiKey": "4dbc17e007ab436fb66416009dfb59a8",
                                                                "country": "in",
                                                                "category": "General"
                                                                        }
                                                                main_url = "https://newsapi.org/v2/top-headlines"

                                                                # fetching data in json format
                                                                res = requests.get(main_url, params=query_params)
                                                                open_bbc_page = res.json()
                                                                article = open_bbc_page["articles"]
                                                                global results
                                                                results = []
                                                                description = []
                                                                for ar in article:

                                                                        results.append(ar["title"])
                                                                Speak111("Today's news headline are: ")
                                                                for i in range(5):
                                                                #print(results[i])
                                                                        print(results[i])
                                                                        Speak(results[i])
 
                                                        
                                                        elif "write a program" in Query.lower() or "write a article" in Query.lower() or "write a essay" in Query.lower() or "write a letter" in Query.lower():
                                                              Speak("PLease wait for some time sir")
                                                              a = chatbot.chat(Query) 
                                                              with open("code.txt" , "w") as f:         
                                                                     f.write(str(a))
                                                              Speak("Work done sir")
                                                              os.startfile("code.txt")
                                                              msg=f"Work done sir and saved in code.txt which is opened."
                                                              notification.notify(title=title,message=msg,app_name=app_name ,app_icon=app_icon, timeout=5)

 
                                                        else:
                                                                if Query=="" or Query==None or Query=="None":
                                                                        print("No command")
                                                                else:
                                                                        Query = Query+" ( Remember that you have to answer in one - two sentences maximum)"
                                                                        Speak(chatbot.chat(Query))
                                                                        self.textBrowser.setFont(font)
                                                                #processing
    
                                                        self.activity_label.setText("    Clap to Speak")
                                                        self.textBrowser.setFont(font)
                                                        Running = False
                                                
                                while True:
                                        self.textBrowser.setFont(font)
                                        Tester(chatbot)
                        except Exception as e:
                              print(e)
                              messagebox.showerror("Some Error Occured",f"The Error appeared is :{e}\n Restaring the function")
                              self.start_jarvis_execution()                
        
                def start_jarvis_execution(self):
                        """ This is  just a function which start the Jarvis_Execution function in a new thread"""
                        try:   
                                thread = threading.Thread(target=self.Jarvis_Execution)
                                thread.start()  
                        except Exception as e:
                                print(e)

    
        
        import sys
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        os.system("TASKKILL /F /im Loading_Screen_Jarvis.exe")
        MainWindow.show()
        sys.exit(app.exec_())


try:
        Jarvis_Execution()
except Exception as e:
        try:
                os.system("TASKKILL /F /im Loading_Screen_Jarvis.exe")
        except:
                pass
        result = messagebox.askyesno("Error -:- -- SOME ERROR --", f"The error is : {e}\nDo you restart the software.")

        if result:
                print("User clicked Yes")
                os.startfile("Jarvis_Main.exe")
                sys.exit()
        else:
                print("User clicked No")
                sys.exit()       
