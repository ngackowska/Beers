from tkinter import *
import clips_management

def btn_clicked(btn, action):
    if action == "start":
        if btn == "yes":
            clips_management.start()
            questioning()
            
        if btn =="no":
            print("A TO CHUJ BOBER NIE CHCE")
            exit()

    elif action == "quest":
        

def questioning():
    question = clips_management.get_question()
    question_txt.config(text = question)
    btn_yes.config(command= lambda:btn_clicked("yes", "quest"))
    btn_no.config(command= lambda:btn_clicked("no", "quest"))


root = Tk()
root.title("What should you drink? Beer Edition")
root.geometry("600x400")

question_txt = Label(root, text="Start the program?")
question_txt.pack()


btn_yes = Button(root, text="yes", command= lambda:btn_clicked("yes", "start"))
btn_no = Button(root, text="no", command= lambda:btn_clicked("no", "start"))

btn_no.pack()
btn_yes.pack()

mainloop()