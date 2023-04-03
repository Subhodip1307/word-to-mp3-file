import os,sys
from tkinter import *
import tkinter.messagebox as masgbox
import pyttsx3
from gtts import gTTS
import webbrowser
path=os.getcwd()
class W2mp3(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("840x400")
        self.title("Word₂mp3")

    def CButton(self):
        pass
    def converter(self):
        val=Values.get("1.0","end-1c")
        if not val:
            masgbox.showwarning("The Entry box is empty","It sames that the Entry box is empty kindly fill it and then try ")
        else:
            try:
                if clicked.get() =="Male Voice" :
                    self.male(Values.get(1.0,END))
                elif clicked.get()=="Female Voice":
                    self.female(Values.get(1.0,END))
                else:
                    self.femalepart2(Values.get(1.0,END))
            except Exception as error:
                if clicked.get()=="Female(Google voice)":
                    masgbox.showinfo("kindly turn on your internet","The google only runs on internet")
                else:
                    masgbox.showinfo("Some error has been occur","Kindly contact your developer")
            Values.delete(1.0,END)
            masgbox.showinfo("Word₂mp₃",f"Converting to {clicked.get()}  has been in path({path})")
            self.quit()
    def pitch(self):
        masgbox.showinfo("This mode is not ready to use","we are happy to hear that you are exited to use our program, so kindly wait we are working on this program")
    #     advance_window=Tk()
    #     advance_window.geometry("500x250")
    #     advance_window.maxsize(width=500,height=250)
    #     advance_window.title("ADVANCE VOICE SETTINGS")
    #     # Label(advance_window,text="Choose the number's of pitch for your voice",font="time 16 bold").grid(row=1,column=1)
    #     # self.pitchrateings(advance_window)
    #     v1 = ["Male Voice", "Female Voice","Female(Google voice)"]
    #     clicked1 = tkinter.StringVar()
    #     clicked1.set(v1[2])
    #     # Label(advance_window,text="Choose the voice type").grid(row=3,column=1)
    #     dropdown=OptionMenu(advance_window, clicked1, *v1)
    #     dropdown.pack()
    #     # self.dropdown(v1,clicked1,"Male voice",advance_window)
    #     advance_window.mainloop()
    def support(self):
        masgbox.showinfo("Support","for support you can visit to git hub profile")
    def Github(self):
       ask=masgbox.askquestion("Redirect to Github","You are going to redirect to our github profile",icon="info")
       if ask=="yes" or ask =="Yes":
            webbrowser.open("https://github.com/Subhodip1307")
       else:
           pass
    def help(self):
        masgbox.showinfo("Sorry","we are still working on it")
    def policy(self):
        masgbox.showinfo("Our Policy","It's a free tool for video editing")
    def out(self):
        self.quit()
    @staticmethod
    def male(letter):
        male_v = pyttsx3.init()
        male_v.setProperty("rate", 184)
        male_v.say(letter)
        # os.chdir(path)
        male_v.save_to_file(letter, f"{path}/male_voice.mp3")
        male_v.runAndWait()
    @staticmethod
    def female(letter):
        female_v = pyttsx3.init()
        voice = female_v.getProperty("voices")
        female_v.setProperty("voice", voice[1].id)
        female_v.setProperty("rate", 184)
        female_v.say(letter)
        os.chdir(path)
        female_v.save_to_file(letter, f"{path}/female_voice.mp3")
        female_v.runAndWait()
    @staticmethod
    def femalepart2(letter):
        os.chdir(path)
        ts=gTTS(letter,lang="en",slow=False)
        ts.save(f'{path}/female_speech.mp3')
    @staticmethod
    def pitchrateings(window):
        rateing=Scale(window,from_=1,to=255,orient=HORIZONTAL)
        rateing.grid(row=2,column=1)
    @staticmethod
    def dropdown(values,varible,set_value,window_name):
        varible.set(set_value)
        OptionMenu(window_name,varible,*values).pack()
if __name__ == '__main__':
    window=W2mp3()
    window.wm_iconbitmap("w2mp3pic.ico")
    #Menu bar
    menubar = Menu(window)
    #File Menu
    File = Menu(menubar, tearoff=0)
    File.add_command(label="Voice Settings",command=window.pitch)
    # File.add_command(label="Setting",command=)
    File.add_command(label="Exit",command=window.out)
    menubar.add_cascade(label="ADVANCE",menu=File)
    #About Menu
    About=Menu(menubar,tearoff=0)
    About.add_command(label="GITHUB",command=window.Github)
    About.add_separator()
    About.add_command(label="Support")
    About.add_command(label="HELP",command=window.help)
    About.add_separator()
    About.add_command(label="Privacy policy",command=window.policy)
    menubar.add_cascade(label="ABOUT",menu=About)
    window.config(menu=menubar)
    Label(window,text="Which voice you Do you want to select ?",pady=20).pack(anchor="nw")
    v = ["Male Voice", "Female Voice","Female(Google voice)"]
    clicked=StringVar()
    # clicked.set("Male Voice")
    # OptionMenu(window,clicked,*v).pack(anchor="nw")
    window.dropdown(v,clicked,"Male Voice",window)
    reciver=StringVar()
    h_ruler = Scrollbar(window)
    h_ruler.pack(side=RIGHT, fill=Y)
    submit = Button(text="Convert",font="time 10 bold", command=window.converter,foreground="black",bg="green").pack(side=BOTTOM, pady=20)
    Label(text="Type what do you want to convert").pack()
    Values=Text(window,font="lucida 20 italic",relief=SUNKEN,bg="grey",foreground="green",yscrollcommand=h_ruler.set)
    Values.pack(anchor="nw",fill=BOTH,pady=20,padx=10)
    h_ruler.config(command=Values.yview,orient=VERTICAL)
    window.mainloop()
