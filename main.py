from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.1
SHORT_BREAK_MIN = 0.1
LONG_BREAK_MIN = 0.1
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
	global reps
	window.after_cancel(timer)
	canvas.itemconfig(timer_text, text="00:00")
	header.config(text="Timer")
	check_label.config(text="")
	reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
	global reps
	reps += 1
	if reps % 2 != 0:
		count_down(WORK_MIN * 60)
		header.config(text="WORK", fg=GREEN)
	elif reps < 8:
		count_down(SHORT_BREAK_MIN * 60)
		header.config(text="SHORT BRK", fg=PINK)
	else:
		count_down(LONG_BREAK_MIN * 60)
		header.config(text="LONG BRK", fg=RED)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
	global timer
	count_min = math.floor(count / 60)
	count_sec = count % 60

	#dynamic typing
	if count_sec < 10:
		count_sec = f"0{count_sec}"

	if count > 0:
		canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
		timer = window.after(1000, count_down, count - 1)
	else:
		if reps <= 8:
			start_timer()
			marks = ""
			for _ in range(math.floor(reps/2)):
				marks += "✓"

			check_label.config(text=marks)
		else:
			reset_timer()





# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img) #x,y
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=2)

header = Label(window, text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 24))
header.grid(column=1, row=1)

start_btn = Button(text="Start", highlightthickness=0, command=start_timer)
start_btn.grid(column=0, row=3)

reset_btn = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_btn.grid(column=2, row=3)

check_label = Label(text="",highlightthickness=0, bg=YELLOW, fg=GREEN)
check_label.grid(column=1, row=3)


window.mainloop()