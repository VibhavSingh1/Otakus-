
from tkinter import *
import random
from PIL import Image, ImageTk
from boott import *
import winsound

rand_indexes = []

index = 0  # variable to keep track of the index of rand_indexes list.

x1 = 0     # variable to get value placed in rand_indexes list.

score = 0

questions = [
        '1.png',
        '2.png',
        '3.png',
        '4.png',
        '5.png',
        '6.png',
        '7.png',
        '8.png',
        '9.png',
        '10.png',
        '11.png',
        '12.png',
        '13.png',
        '14.png',
        '15.png',
        '16.png',
        '17.png',
        '18.png',
        '19.png',
        '20.png',
        '21.png',
        '22.png',
        '23.png',
        '24.png',
        '25.png',
        '26.png',
        '27.png',
        '28.png',
        '29.png',
        '30.png',
        '31.png',
        '32.png',
        '33.png',
        '34.png',
        '35.png',
        '36.png',
        '37.png',
        '38.png',
        '39.png',
        '40.png',
        '41.png',

    ]
answer_list = [
        'jin',
        'light yagami',
        'hinata',
        'zoro',
        'eren',
        'mikasa',
        'luffy',
        'levi',
        'kirito',
        'gon',
        'hisoka',
        'tanziro',
        'killua',
        'inosuke',
        'yuno gasai',
        'bam',
        'erza scarlet',
        'natsu dragneel',
        'mob',
        'deku',
        'bakugo',
        'saitama',
        'all might',
        'ichigo kurosaki',
        'ban',
        'genos',
        'meliodas',
        'kise',
        'kuroko',
        'soma yukihira',
        'zero',
        'ken kaneki',
        'shoto todoroki',
        'blank',
        'yahiko',
        'madara uchiha',
        'frieza',
        'l',
        'aizen',
        'kid buu',
        'cell',
               ]


# ---------------------------------------------------------------------------------------
# INITIAL WINDOW..


root = Tk()
root.title("Anime Quiz")
root.geometry("1200x600")
root.resizable(0, 0)
winsound.PlaySound('fairy222', winsound.SND_ASYNC | winsound.SND_ALIAS )
startmusic = PhotoImage(file = 'start_music.png')
stopmusic = PhotoImage(file='stop_music.png')
counter=0
def start_music():
    global counter
    if counter %2 == 1:
        # startmusic = PhotoImage(file = 'start_music.png')
        start_music.config(image = stopmusic,border=0)
        winsound.PlaySound('fairy222', winsound.SND_ASYNC | winsound.SND_ALIAS )
    elif counter %2 == 0:
        # stopmusic = PhotoImage(file='stop_music.png')
        start_music.config(image=startmusic,border=0)

        winsound.PlaySound(None, winsound.SND_ASYNC)
    else:
        print("Error")
    counter = counter + 1


def gen():  # generates the random sequence of numbers.
    global rand_indexes
    while True:
        x = random.randint(0, 40)

        if len(rand_indexes) == 10:
            break
        elif x not in rand_indexes:
            rand_indexes.append(x)
        else:
            continue


def evaluation():  # Checking answers and updating score.

    global score, answer_list, x1

    a = str(e1.get())
    if answer_list[x1] == a.lower():
        score += 2
    elif answer_list[x1] != a.lower():
        score -= 1


def show_result():  # To show the final result.
    global score

    # cleaning the window to show result.
    remove_game_window()

    # placing the result on window.
    score_label.config(text='You Scored: ' + str(score) + ' of 20')
    score_label.place(y=260, x=430, height=70, width=500)
    restart_button.place(y=420, x=690, height=40, width=100)
    exit_button.place(y=420, x=560, height=40, width=100)


def hint_used():
    global score
    var = str(e.get())
    var = var.lower()
    if var.strip() == "hint":
        score -= 0.5
    return score


def remove_main_menu():   # Removing extras from window.
    btnStart.place(y=1200)
    label_text.place(y=1230)


def place_main_menu():   # Undoing the remove_main_menu for restarting the game.
    label_text.place(x=500, y=20)
    btnStart.place(x=430, y=450, height=60, width=400)


def remove_game_window():  # Removing extras from window.

    q_label.place(y=1300)
    q_tag.place(y=1320)
    e1.place(y=1340)
    next1.place(y=1360)
    f1.place(y=1380)
    f_bot.place(y=1400)


def place_game_window():

    q_label.place(x=0, y=0, height=450, width=740)
    q_tag.place(x=250, y=0)
    q_num.place(x=0, y=0)
    e1.place(x=50, y=500, width=550, height=40)
    next1.place(x=660, y=500, height=40, width=100)
    f_bot.place(x=775, y=10, height=530, width=410)  # placing the bot.


def nullifying():   # initializing the global data for use.
    global rand_indexes, index, x1, score
    rand_indexes.clear()
    index, x1, score = 0, 0, 0
    e1.delete(0, END)
    m.config(state='normal')
    m.delete(1.0, END)
    m.config(state="disable")


def restart():

    global rand_indexes, index, x1, score
    nullifying()

    # Removing the items from the result window.
    score_label.place(y=1300, x=430, height=70, width=500)
    restart_button.place(y=1420, x=690, height=40, width=100)
    exit_button.place(y=1420, x=560, height=40, width=100)

    # Placing the main menu.
    place_main_menu()


def move_next():  # Move to next question and calling necessary functions.

    global rand_indexes, index, x1, score

    a = str(e1.get())

    if a.strip() != "" and index < 9:
        evaluation()
    elif a.strip() != "" and index == 9:
        evaluation()
        show_result()
        return 0
    elif a.strip() == "" and index == 9:
        show_result()
        return 0

    if index < 9:
        index += 1

    e1.delete(0, END)  # clearing the entry box

    if index < 10:
        x1 = rand_indexes[index]
    else:
        exit(102)

    if x1 < 41:
        img3_1 = ImageTk.PhotoImage(Image.open(questions[x1]))
        q_label.config(image=img3_1)
        q_num.config(text="Q.no: " + str(index + 1))
    else:
        exit(101)  # just for checking the index out of scope error.

    f1.mainloop()


def start():        # starting the game.
    global questions, x1, rand_indexes, index

    remove_main_menu()

    # -----------------------------------------------------------------
    gen()  # called to generate random sequence of questions

    # frame for question images.
    f1.place(x=20, y=10, height=450, width=740)

    if index == 0:          # for correct evaluation of first question.
        x1 = rand_indexes[0]
        q_num.config(text="Q.no: " + str(index + 1))

    img3 = ImageTk.PhotoImage(Image.open(questions[rand_indexes[0]]))

    q_label.config(image=img3)

    place_game_window()

    f1.mainloop()

# ----------------------------------------------------------------------------------
# Main menu Window defining.


img = Image.open('bg1.jpg')  # Opening an image for background.
img = ImageTk.PhotoImage(img)

f_ini = Frame(root)
f_ini.place(height="600", width="1200")

label_image = Label(f_ini, image=img)
label_image.place(x=0, y=0)

label_text = Label(         # Label containing the game title.
    f_ini,
    text="Prototype 0.2. ",
    font=("Comic sans MS", 24, "bold"),
    bg="grey10", fg="white"
)
label_text.place(x=500, y=20)

btnStart = Button(          # Button to start the Game.
    f_ini,
    text="START", font="ariel 20",
    fg="white", bg="grey10",
    activeforeground="black", activebackground="white",
    command=start,
)
btnStart.place(x=430, y=450, height=60, width=400)
# ---------------------------------------------------------------------------------------------------------------
# _____________________________________
#                                                ---- HINT BOT code ----

f_bot = Frame(f_ini)  # Frame to contain the Chat Bot.


def bot_respond():    # Taking the bot's response and inserting in textbox.
    global x1
    var = str(e.get())
    var = var.lower()
    if var.strip() == "hint" or var.strip() == "hint please" or var.strip() == "give hint" or var.strip() == "hint me":
        response = bot.get_response("QCODE" + str(1 + x1))
        m.insert(INSERT, "BOT : " + str(response) + "\n")
    else:
        response = bot.get_response(var)
        m.insert(INSERT, "BOT : " + str(response) + "\n")


def ins():            # Inserting the user's input and bot response in text box (m).

    var = e.get()
    if var.strip() == "":
        return
    m.config(state="normal")
    m.insert(INSERT, "You : " + var + "\n")
    bot_respond()
    m.config(state="disable")
    hint_used()
    e.delete(0, len(var))


def clr():           # To clear the Text box(m).

    m.config(state="normal")
    m.delete(1.0, END)
    m.config(state="disable")


top_frame = Frame(f_bot, bg="black")     # Frame to contain textbox(m).
top_frame.place(height=350, width=410, x=0, y=0)
bot_frame = Frame(f_bot, bg="black")     # Frame to contain entry box(e) and send button(b).
bot_frame.place(height=185, width=410, x=0, y=350)

m = Text(top_frame, fg="white", bg="grey10", bd=3)  # Text box to show the chat.
m.place(height=340, width=392, x=3, y=3)

scroll = Scrollbar(top_frame)            # scrollbar for top frame containing textbox(m).
scroll.place(x=392, y=4, height=340)
scroll.config(command=m.yview)

# Entry box for user's input for Chat bot.
e = Entry(bot_frame, fg="white", bg="grey10", insertbackground="white", font="Ariel", bd=3)
e.place(height=70, width=274, x=5, y=10)

# Button to send the message to bot.

def aut(eve):
    b.invoke()
root.bind('<Return>',aut)

b = Button(bot_frame, text="SEND", font=20,
           bg="red2", activebackground="VioletRed1",
           fg="black", activeforeground="red",
           bd=5, command=ins)
b.place(height=80, width=128, x=279, y=5)



#                                      ----- HINT BOT Code END ----
# -----------------------------------------------------------------------------------------------------------------
# Contents to be placed in show_result window.
# --------------------------------------------------------------------------
score_label = Label(f_ini, text='You Scored: ' + str(score) + ' of 20',
                    font="Ariel 30", fg="white",
                    bg='grey10')

restart_button = Button(f_ini, text="Play Again", font="16", fg="white",
                        bg="grey10", activeforeground="black",
                        activebackground="white",
                        command=restart)

exit_button = Button(f_ini, text="Quit", font="16", fg="white",
                     bg="grey10", activeforeground="black",
                     activebackground="white",
                     command=quit)
# --------------------------------------------------------------------------
# Contents to be placed in start()
# --------------------------------------------------------------------------
f1 = Frame(f_ini)

q_label = Label(f1)

q_tag = Label(f1, text="-:: Identify  The  Character ::-",
              font='Ariel 12', bg='grey10', fg='white')

q_num = Label(f1, text="Q.no: " + str(index + 1),
              font='Ariel 12', bg='grey10',
              fg='white')

e1 = Entry(f_ini, font="Ariel 14", fg="white",
           bg="grey10", insertbackground="white")

next1 = Button(f_ini, text="NEXT", font="Ariel 20",
               fg="white", bg="grey10", activeforeground="black",
               activebackground="white", command=move_next)

start_music = Button(bot_frame,image = stopmusic,border=0,bg="grey10",command=start_music )
start_music.place(x=10,y=105)


root.mainloop()

