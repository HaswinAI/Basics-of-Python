#upload file 
"""
import tkinter as tk
from tkinter import filedialog

def upload_action(event=None):
    file_path = filedialog.askopenfilename()
    

root = tk.Tk()
root.title("Upload Button Example")

upload_button = tk.Button(root, text="Upload", command=upload_action)
upload_button.pack(pady=20)

root.mainloop()
"""
#calender
'''
import calendar 
print("")
year = 2024
print(calendar.calendar(int(year)))
'''
#speaking project

"""
import pyttsx3
def say(text) :
    engine=pyttsx3.init()
    voice = engine.getProperty('voices')
    engine.setProperty('voice',voice[1].id)
    engine.say(text)
    engine.runAndWait()
say("  my lifeee iss in this townn and arent goingg down you thinkk that iam crazzyyy butt i dontt wanna crownnn   ")
"""

#project with format

text=input("what would you like the cat to say ?")
text_length=len(text)
print("             {}".format("_" * text_length))
print("            <{}>".format(text))
print("             {}".format("-" * text_length))
print("             /")
print("    /\_/\   /")
print("   ( o.o )")
print("    > ^ < ")
