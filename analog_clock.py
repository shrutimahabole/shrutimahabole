import tkinter as ui
import time
import math

window=ui.Tk()    # For Ui screen
window.geometry("400x400")


def update_clock():
    hours=int(time.strftime("%I"))
    minutes=int(time.strftime("%M"))
    seconds=int(time.strftime("%S"))
    
    #update seconds hand per seconds
    seconds_x=seconds_hand_len * math.sin(math.radians(seconds * 6)) + center_x
    seconds_y= -1 * seconds_hand_len * math.cos(math.radians(seconds * 6)) + center_y
    canvas.coords(seconds_hand,center_x,center_y,seconds_x,seconds_y)
    
    
     #update minutes hand per minute
    minutes_x=minutes_hand_len * math.sin(math.radians(minutes * 6)) + center_x
    minutes_y= -1 * minutes_hand_len * math.cos(math.radians(minutes * 6)) + center_y
    canvas.coords(minutes_hand,center_x,center_y,minutes_x,minutes_y)
    
     #update hours hand per seconds
    hours_x=hours_hand_len * math.sin(math.radians(hours * 30)) + center_x
    hours_y= -1 * hours_hand_len * math.cos(math.radians(hours * 30)) + center_y
    canvas.coords(hours_hand,center_x,center_y,hours_x,hours_y)
    
    
    
    window.after(1000, update_clock)     # loop after every 1 sec
    
   
canvas = ui.Canvas(window,width=500, height=500, bg="black")
canvas.pack(expand=True, fill='both')

#create background
bg = ui.PhotoImage(file='Ss.png')
canvas.create_image(200,200,image=bg)

 
# digital_clock_lbl=ui.Label(window,text="00:00:00",font="Helvetica 72 bold")  #create Lablel
# digital_clock_lbl.pack()    #to display Label on screen

#Create clock hands
center_x=200
center_y=200
seconds_hand_len=72
minutes_hand_len=80
hours_hand_len=60

#Drawing clock hands
#seconds hand
seconds_hand = canvas.create_line(200,200,200 + seconds_hand_len, 200 + seconds_hand_len, width=1.5, fill='red')

#minutes hand
minutes_hand = canvas.create_line(200,200,200 + minutes_hand_len, 200 + minutes_hand_len, width=2, fill='black')

#hours hand
hours_hand = canvas.create_line(200,200,200 + hours_hand_len , 200 + hours_hand_len, width=4, fill='black')


update_clock()

window.mainloop()