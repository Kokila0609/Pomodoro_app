from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
  global reps
  reps = 0
  timer_label.config(text = "Timer", font=(FONT_NAME, 50, "bold"), fg = GREEN)
  canvas.itemconfig(timer_text, text="00:00")
  checkmark_label.config(text="")
  window.after_cancel(timer)
  




# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
  global reps
  reps+=1
  work_sec = WORK_MIN*60
  short_break_sec = SHORT_BREAK_MIN*60
  long_break_sec = LONG_BREAK_MIN*60

  #if it is 8th rep
  if reps%8 == 0:
    count_down(long_break_sec)
    timer_label.configure(text = "Long Break", font=(FONT_NAME, 50, "bold"), fg = RED)

  # if it is 2nd/4th/6th reps
  elif reps%2 ==0:
    count_down(short_break_sec)
    timer_label.configure(text = "Short Break", font=(FONT_NAME, 50, "bold"), fg = PINK)

    #if it is 1st/3rd/5th/7th reps
  else:
    count_down(work_sec)  
    timer_label.configure(text = "Work", font=(FONT_NAME, 50, "bold"), fg = GREEN)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):

  count_min = math.floor(count / 60)
  count_sec = count % 60

  if count_sec < 10:
    count_sec = f"0{count_sec}"

  # if count_sec == 0:
  #   count_sec = "00"


  canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
  
     
  if count > 0:
    global timer
    timer = window.after(1000, count_down, count-1)
  else:
     start_timer()
     mark = ""
     work_session = math.floor(reps/2)
     for _ in range(work_session):
       mark+= "✔"
       checkmark_label.config(text=mark)
     


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()

window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img )
timer_text= canvas.create_text(100,130, text ="00:00", fill="white", font=(FONT_NAME, 35, "bold") )
canvas.grid(row=1, column=1)


timer_label = Label(text = "Timer", font=(FONT_NAME, 50, "bold"), fg = GREEN, bg=YELLOW, highlightthickness=0 )
timer_label.grid(row=0, column=1)

start_button = Button(text="Start", command = start_timer)

start_button.grid(row=2, column=0)

stop_button = Button(text="Reset", command = reset_timer)
stop_button.grid(row=2, column=2)

checkmark_label = Label( fg = GREEN, bg=YELLOW, highlightthickness=0, font=(FONT_NAME, 15, "bold"))
checkmark_label.grid(row=3, column=1)





window.mainloop()