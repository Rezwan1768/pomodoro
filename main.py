import tkinter
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 20
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 25
timer = None
reps = 0
is_break_time = False
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps, is_break_time
    window.after_cancel(timer)
    heading.configure(text="Timer", fg=GREEN)
    canvas.itemconfig(time_text, text="00:00")
    check_mark.configure(text="")
    reps = 0
    is_break_time = False
# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps, is_break_time

    # convert the minutes to seconds
    work_sec = int(WORK_MIN * 60)
    short_break_sec = int(SHORT_BREAK_MIN * 60)
    long_break_sec = int(LONG_BREAK_MIN * 60)

    if reps <= 4 and not is_break_time:
        is_break_time = True
        reps += 1
        count_down(work_sec)
        heading.configure(text="Work", fg=GREEN)

    elif reps < 4 and is_break_time:
        is_break_time = False
        count_down(short_break_sec)
        heading.configure(text="Break", fg=PINK)
    else:
        reps = 0
        is_break_time = False
        count_down(long_break_sec)
        heading.configure(text="Break", fg=RED)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    min_count = count // 60
    sec_count = count % 60

    # Change sec_count / min_count to string to display the prefix '0'
    # if sec_count == 0:
    #     sec_count = "00"
    if 0 <= int(sec_count) < 10:
        sec_count = "0" + str(sec_count)
    if 0 <= min_count < 10:
        min_count = "0" + str(min_count)
    if count >= 0:
        global timer
        canvas.itemconfig(time_text, text=f"{min_count}:{sec_count}")
        timer = window.after(1000, count_down, count - 1)
    else:
        check = ""
        for _ in range(reps):
            print(_)
            check += "✓"
        print()
        # check = "✓" * reps
        check_mark.configure(text=check)

        start_timer()
# ---------------------------- UI SETUP ------------------------------- #

# ------- Window -----------
window = tkinter.Tk()
window.title("Pomodoro")
window.config( padx=100, pady=50, bg=YELLOW)


# Heading
heading = tkinter.Label(text="Timer", font=(FONT_NAME, 40, "bold"), bg=YELLOW, fg=GREEN)
heading.grid(row=0, column=1)

# ----------canvas------------------
canvas = tkinter.Canvas(width=201, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 100, image=tomato_img)

# Assign the time text to a variable
time_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)


# -----------Buttons-------------
# when clicked start the timer
start_btn = tkinter.Button(text="Start", highlightthickness=0, command=start_timer)
start_btn.grid(row=2, column=0)

reset_btn = tkinter.Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_btn.grid(row=2, column=2)

# check marks
check_mark = tkinter.Label(font=(FONT_NAME, 15), fg=GREEN, bg=YELLOW)
check_mark.grid(row=3, column=1)
window.mainloop()
