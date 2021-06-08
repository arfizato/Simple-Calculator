import tkinter as tk
from tkinter import Button, Menu, font
from tkinter.constants import DISABLED, NORMAL

    
def fitInScreen():
    global onScreenText,myFont, fontSize, screenText, firstInt, secondInt,disabledBySize
    #print("okay: "+str(len(onScreenText))+"\t"+str(fontSize))
    if (len(onScreenText)>=32 and fontSize==20):
        fontSize=15
        myFont=font.Font(family="emojione color", size=fontSize)
        screen["font"]=myFont
        
    if (len(onScreenText)>=49 and fontSize==15):
        fontSize=20
        myFont=font.Font(family="emojione color", size=fontSize)
        screen["font"]=myFont
        onScreenText="Error: integer overload"
        screenText.set(onScreenText)         
        plusButton["state"]=DISABLED
        minusButton["state"]=DISABLED
        divButton["state"]=DISABLED
        timesButton["state"]=DISABLED
        onScreenText=""
        secondInt=0
        firstInt=0
        disabledBySize=True
    
def numtapped(x,button):
    global screenText, onScreenText, lastIsNum, secondInt, justOperated, lastIsCalc, disabledBySize
    if False==lastIsNum:
        secondInt=secondInt*10+x
        if justOperated:
            onScreenText=onScreenText+globalOperator
            plusButton["state"]=DISABLED
            minusButton["state"]=DISABLED
            divButton["state"]=DISABLED
            timesButton["state"]=DISABLED
            justOperated=False
    elif lastIsCalc:
        onScreenText=""
        lastIsCalc=False
    
    if disabledBySize:
        plusButton["state"]=NORMAL
        minusButton["state"]=NORMAL
        divButton["state"]=NORMAL
        timesButton["state"]=NORMAL
        disabledBySize=False

    
    onScreenText=onScreenText+str(x)
    fitInScreen()
    screenText.set(onScreenText)

def operator(x):
    global screenText, onScreenText, lastIsNum, firstInt, globalOperator, justOperated, secondInt
    lastIsNum=False
    firstInt=int(onScreenText)
    screenText.set(onScreenText+x)
    globalOperator=x
    justOperated=True
    secondInt=0
    fitInScreen()

def equals():
    global firstInt, secondInt, screenText, onScreenText, lastIsNum, globalOperator, lastIsCalc

    if (globalOperator==" + " ):
        onScreenText=str(firstInt+secondInt)
        fitInScreen()
        screenText.set(onScreenText)
        firstInt+=secondInt
    elif (globalOperator== " - "):
        onScreenText=str(firstInt-secondInt)
        fitInScreen()
        screenText.set(onScreenText)
        firstInt-=secondInt
    elif (globalOperator== " x "):
        onScreenText=str(firstInt*secondInt)
        fitInScreen()
        screenText.set(onScreenText)
        firstInt*=secondInt
    elif (globalOperator== " / "):
        onScreenText=str(int(firstInt/secondInt))
        fitInScreen()
        screenText.set(onScreenText)
        firstInt/=secondInt
    
    plusButton["state"]=NORMAL
    minusButton["state"]=NORMAL
    divButton["state"]=NORMAL
    timesButton["state"]=NORMAL

    lastIsNum=True
    lastIsCalc=True

def changeTheme():
    root.config(bg=backgroundColor)
    screen["bg"]=bgColor
    screen["fg"]=fgColor

    num0["bg"]=bgColor
    num0["fg"]=fgColor
    num0["activebackground"]=bgColorActive
    num0["activeforeground"]=fgColor   

    num1["bg"]=bgColor
    num1["fg"]=fgColor
    num1["activebackground"]=bgColorActive
    num1["activeforeground"]=fgColor

    num2["bg"]=bgColor
    num2["fg"]=fgColor
    num2["activebackground"]=bgColorActive
    num2["activeforeground"]=fgColor

    num3["bg"]=bgColor
    num3["fg"]=fgColor
    num3["activebackground"]=bgColorActive
    num3["activeforeground"]=fgColor

    num4["bg"]=bgColor
    num4["fg"]=fgColor
    num4["activebackground"]=bgColorActive
    num4["activeforeground"]=fgColor

    num5["bg"]=bgColor
    num5["fg"]=fgColor
    num5["activebackground"]=bgColorActive
    num5["activeforeground"]=fgColor   
   
    num6["bg"]=bgColor
    num6["fg"]=fgColor
    num6["activebackground"]=bgColorActive
    num6["activeforeground"]=fgColor

    num7["bg"]=bgColor
    num7["fg"]=fgColor
    num7["activebackground"]=bgColorActive
    num7["activeforeground"]=fgColor

    num8["bg"]=bgColor
    num8["fg"]=fgColor
    num8["activebackground"]=bgColorActive
    num8["activeforeground"]=fgColor

    num9["bg"]=bgColor
    num9["fg"]=fgColor
    num9["activebackground"]=bgColorActive
    num9["activeforeground"]=fgColor


    plusButton["bg"]=bgColor
    plusButton["fg"]=fgColor
    plusButton["activebackground"]=bgColorActive
    plusButton["activeforeground"]=fgColor

    minusButton["bg"]=bgColor
    minusButton["fg"]=fgColor
    minusButton["activebackground"]=bgColorActive
    minusButton["activeforeground"]=fgColor

    equalButton["bg"]=bgColor
    equalButton["fg"]=fgColor
    equalButton["activebackground"]=bgColorActive
    equalButton["activeforeground"]=fgColor

    divButton["bg"]=bgColor
    divButton["fg"]=fgColor
    divButton["activebackground"]=bgColorActive
    divButton["activeforeground"]=fgColor

    timesButton["bg"]=bgColor
    timesButton["fg"]=fgColor
    timesButton["activebackground"]=bgColorActive
    timesButton["activeforeground"]=fgColor

def Dark():      
    global backgroundColor, bgColor, fgColor, bgColorActive, screen
    backgroundColor="#272727" 
    bgColor="#353535"
    bgColorActive="#515151"
    fgColor="#BAF9FF"
    changeTheme()

def Light():  
    global backgroundColor, bgColor, fgColor, bgColorActive   
    backgroundColor="#f5f5f5" 
    bgColor="#fff"
    bgColorActive="#fafafa"
    fgColor="#000"
    changeTheme()

def clrscr():
    global onScreenText, screenText, firstInt, secondInt
    firstInt, secondInt= 0,0
    onScreenText=""
    screenText.set("Tap an equation")

lastIsCalc=True
onScreenText=""
lastIsNum=True
firstInt, secondInt=0,0
globalOperator=""
justOperated=False
disabledBySize=False

if True:#declaring colors    
    backgroundColor="#f5f5f5" 
    bgColor="#fff"
    bgColorActive="#fafafa"
    fgColor="#000"

if True: #declaring Root, Font and Label
    root= tk.Tk()
    root.title("Calculator")
    root.geometry("400x500+0+0")
    root.config(bg=backgroundColor)
    root.iconbitmap("images/calculator.ico")
    fontSize=20
    myFont=font.Font(family="emojione color", size=fontSize)

    screenText=tk.StringVar()
    screenText.set("Tap an equation")
    screen= tk.Label(root,textvariable=screenText,bg=bgColor,fg=fgColor,font= myFont, justify='left', )#,width=300,height=400)
    screen.place(relx=0,rely=0,relheight=.2,relwidth=1)

if True:#declaring all the buttons
    num7 = Button(root, text="7", bg=bgColor, fg=fgColor,activebackground=bgColorActive, activeforeground=fgColor , bd=0, font=myFont, command= lambda : numtapped(7,num7) )
    num7.place(relx=0,rely=.21, relwidth=.25, relheight=.2)

    num8 = Button(root, text="8", bg=bgColor, fg=fgColor,activebackground=bgColorActive, activeforeground=fgColor , bd=0, font=myFont, command= lambda : numtapped(8,num8) )
    num8.place(relx=.26,rely=.21, relwidth=.25, relheight=.2)

    num9 = Button(root, text="9", bg=bgColor, fg=fgColor,activebackground=bgColorActive, activeforeground=fgColor , bd=0, font=myFont, command= lambda : numtapped(9,num9) )
    num9.place(relx=.52,rely=.21, relwidth=.25, relheight=.2)


    num4 = Button(root, text="4", bg=bgColor, fg=fgColor,activebackground=bgColorActive, activeforeground=fgColor , bd=0, font=myFont, command= lambda : numtapped(4,num4) )
    num4.place(relx=0,rely=.42, relwidth=.25, relheight=.2)

    num5 = Button(root, text="5", bg=bgColor, fg=fgColor,activebackground=bgColorActive, activeforeground=fgColor , bd=0, font=myFont, command= lambda : numtapped(5,num5) )
    num5.place(relx=.26,rely=.42, relwidth=.25, relheight=.2)

    num6 = Button(root, text="6", bg=bgColor, fg=fgColor,activebackground=bgColorActive, activeforeground=fgColor , bd=0, font=myFont, command= lambda : numtapped(6,num6) )
    num6.place(relx=.52,rely=.42, relwidth=.25, relheight=.2)


    num1 = Button(root, text="1", bg=bgColor, fg=fgColor,activebackground=bgColorActive, activeforeground=fgColor , bd=0, font=myFont, command= lambda : numtapped(1,num1) )
    num1.place(relx=0,rely=.63, relwidth=.25, relheight=.2)

    num2 = Button(root, text="2", bg=bgColor, fg=fgColor,activebackground=bgColorActive, activeforeground=fgColor , bd=0, font=myFont, command= lambda : numtapped(2,num2) )
    num2.place(relx=.26,rely=.63, relwidth=.25, relheight=.2)

    num3 = Button(root, text="3", bg=bgColor, fg=fgColor,activebackground=bgColorActive, activeforeground=fgColor , bd=0, font=myFont, command= lambda : numtapped(3,num3) )
    num3.place(relx=.52,rely=.63, relwidth=.25, relheight=.2)


    num0 = Button(root, text="0", bg=bgColor, fg=fgColor,activebackground=bgColorActive, activeforeground=fgColor , bd=0, font=myFont, command= lambda : numtapped(0,num0) )
    num0.place(relx=.0,rely=.84, relwidth=.25, relheight=.18)



    minusButton = Button(root, text="-", bg=bgColor, fg=fgColor,activebackground=bgColorActive, activeforeground=fgColor , bd=0, font=myFont, command= lambda : operator(" - ") )
    minusButton.place(relx=.52,rely=.84, relwidth=.25, relheight=.18)

    timesButton = Button(root, text="x", bg=bgColor, fg=fgColor,activebackground=bgColorActive, activeforeground=fgColor , bd=0, font=myFont, command= lambda : operator(" x ") )
    timesButton.place(relx=.78,rely=.42, relwidth=.25, relheight=.2)

    plusButton = Button(root, text="+", bg=bgColor, fg=fgColor,activebackground=bgColorActive, activeforeground=fgColor , bd=0, font=myFont, command= lambda : operator(" + ") )
    plusButton.place(relx=.26,rely=.84, relwidth=.25, relheight=.18)    

    equalButton = Button(root, text="=", bg=bgColor, fg=fgColor,activebackground=bgColorActive, activeforeground=fgColor , bd=0, font=myFont, command= lambda : equals() )
    equalButton.place(relx=.78,rely=.63, relwidth=.25, relheight=.41)

    divButton = Button(root, text="/", bg=bgColor, fg=fgColor,activebackground=bgColorActive, activeforeground=fgColor , bd=0, font=myFont, command= lambda : operator(" / ") )
    divButton.place(relx=.78,rely=.21, relwidth=.25, relheight=.2)

if True:#declaring Menu
    main = Menu(root, )
    root.config(menu=main, )
    App  = Menu(main)
    Theme= Menu(main)

    App.add_command(label="Clear Screen", command= clrscr)
    App.add_command(label="Exit Application", command= lambda : root.destroy())
    main.add_cascade(label="App", menu=App,)

    Theme.add_command(label="Dark Theme" , command= Dark )
    Theme.add_command(label="Light Theme", command= Light)
    main.add_cascade(label="Themes", menu=Theme)

root.mainloop()
"""Coded By 
                 █████╗ ██████╗ ███████╗██╗███████╗ █████╗ ████████╗ ██████╗ 
                ██╔══██╗██╔══██╗██╔════╝██║╚══███╔╝██╔══██╗╚══██╔══╝██╔═══██╗
                ███████║██████╔╝█████╗  ██║  ███╔╝ ███████║   ██║   ██║   ██║
                ██╔══██║██╔══██╗██╔══╝  ██║ ███╔╝  ██╔══██║   ██║   ██║   ██║
                ██║  ██║██║  ██║██║     ██║███████╗██║  ██║   ██║   ╚██████╔╝
                ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ 
"""
"""
dark theme
foreground #353535
background #272727
text       #BAF9FF
"""