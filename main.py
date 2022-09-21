
from threading import Thread
from tkinter.ttk import *
from tkinter import *

from PIL import ImageTk, Image
from pygame import mixer

from datetime import datetime
from time import sleep

# Colors
bg_color = '#fff'  # alb
color_1 = '#ffc0cb'  # pink pal
color_2 = '#000'  # black

# window
window = Tk()
window.title('PyLarm')
window.geometry('450x150')
window.configure(bg=bg_color)

# frames
frame_line = Frame(window, width=4000, height=5, bg=color_1)
frame_line.grid(row=0, column=0)

frame_body = Frame(window, width=4000, height=4000, bg=bg_color)
frame_body.grid(row=1, column=0)

# configure frame body

img = Image.open('pylarm.png')
img.resize((150, 150))
img = ImageTk.PhotoImage(img)

app_image = Label(frame_body, height=100, image=img, bg=bg_color)
app_image.place(x=10, y=10)

name = Label(frame_body, text='PyLarm', height=1,
             font=('Ivy 18 bold'), bg=bg_color)
name.place(x=125, y=10)

#hour
hour = Label(frame_body, text='hour', height=1, font=(
    'Ivy 10 bold'), bg=bg_color, fg=color_1)
hour.place(x=127, y=40)
c_hour = Combobox(frame_body, width=2, font=('arial 15'))
c_hour['values'] = ('00', '01', '02', '03', '04', '05',
                    '06', '07', '08', '09', '10', '11', '12')
c_hour.current(0)
c_hour.place(x=130, y=58)

#minutes
minutes = Label(frame_body, text='min', height=1, font=(
    'Ivy 10 bold'), bg=bg_color, fg=color_1)
minutes.place(x=177, y=40)
c_minutes = Combobox(frame_body, width=2, font=('arial 15'))
c_minutes['values'] = ('00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27',
                       '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59')
c_minutes.current(0)
c_minutes.place(x=180, y=58)

# second 
second  = Label(frame_body, text='sec', height=1, font=(
    'Ivy 10 bold'), bg=bg_color, fg=color_1)
second .place(x=227, y=40)
c_second  = Combobox(frame_body, width=2, font=('arial 15'))
c_second ['values'] = ('00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27',
                       '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59')
c_second .current(0)
c_second .place(x=230, y=58)

#period
period = Label(frame_body, text='period', height=1, font=(
    'Ivy 10 bold'), bg=bg_color, fg=color_1)
period.place(x=277, y=40)
c_period = Combobox(frame_body, width=3, font=('arial 15'))
c_period['values'] = ('AM', 'PM')
c_period.current(0)
c_period.place(x=280, y=58)

#function for activated button
def activate_alarm():
    t = Thread(target=alarm)
    t.start()

#function for deactivate button
def deactivate_alarm():
    print('deactivated alarm: ', selected.get())
    mixer.music.stop()


#variable for selected
selected = IntVar()

#button for activate
rad1 = Radiobutton(frame_body, font=('arial 10 bold '), value=1, text = 'Activate', bg=bg_color, command=activate_alarm, variable=selected)
rad1.place(x = 125, y=95)

#button for deactivate
rad2 = Radiobutton(frame_body, font=('arial 10 bold '), value=2, text = 'Deactivate', bg=bg_color, command=deactivate_alarm, variable=selected)
rad2.place(x = 220, y=95)


#logic script

def sound_alarm():
    mixer.music.load('grateful.mp3')
    mixer.music.play()
    selected.set(0)


def alarm():
    while True:
        control = selected.get()
        print(control)
        alarm_hour = c_hour.get()
        alarm_minute = c_minutes.get()
        alarm_second = c_second.get()
        alarm_period = c_period.get()
        alarm_period = str(alarm_period).upper()

        now = datetime.now()

        hour = now.strftime('%I')
        minute = now.strftime('%M')
        second = now.strftime('%S')
        period = now.strftime('%p')

        if control == 1:
            if alarm_period == period:
                if alarm_hour == hour:
                    if alarm_minute == minute:
                        if alarm_second == second:
                            print('Timpul pentru trezire somnorici')
                            sound_alarm()
                            
        sleep(1)

mixer.init()

window.mainloop()
