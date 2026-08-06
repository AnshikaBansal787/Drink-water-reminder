import tkinter 
from tkinter import messagebox
import win32com.client
import time

# Hides the main blank Tkinter application window
root = tkinter.Tk()
root.withdraw()
speaker= win32com.client.Dispatch("SAPI.SpVoice")
def speak_reminder():
    for i in range(5):
        speaker.Speak("Hey Anshika , Drink water!")
        messagebox.showinfo("Drink Water", "You should drink water now! Stay hydrated for better health.")  # Call the function to speak the reminder
        time.sleep(3600) # Wait for 1 hour before reminding again
        

speak_reminder()
