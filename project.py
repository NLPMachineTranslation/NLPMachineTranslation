from tkinter import *

def main():
    root = Tk()
    root.configure(background="white")
    
    root.title("Machine Translation")
    root.minsize(width=680, height=300)
    root.maxsize(width=680, height=300)

    #Button English to Filipino
    def EngFil():
        pass
    
    #Button Filipino to English
    def FilEng():
        pass
    
    #Label
    Label(root, text="English", bg="white", fg="black", font="MicrosoftYaHeiUILight 12").grid(row=0, column=0, sticky=W)
    #Text Area
    EngTA = Text(root, width=75, height=6, wrap=WORD, background="white", font="MicrosoftYaHeiUILight 12")
    EngTA.grid(row=1, column=0, columnspan=2, sticky=W)
    #Label
    Label(root, text="Filipino", bg="white", fg="black", font="MicrosoftYaHeiUILight 12").grid(row=2, column=0, sticky=W)
    #Text Area
    FilTA = Text(root, width=75, height=6, wrap=WORD, background="white", font="MicrosoftYaHeiUILight 12")
    FilTA.grid(row=3, column=0, columnspan=2, sticky=W)
    #Button
    Button(root, text="English to Filipino", width=15, command=EngFil()).grid(row=4, column=0, sticky=W)
    Button(root, text="Filipino to English", width=15, command=FilEng()).grid(row=4, column=1, sticky=W)
    
    root.mainloop()

if __name__ == "__main__":
    main()
