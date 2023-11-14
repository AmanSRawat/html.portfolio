from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk #write pip install pilow in order to download PIL library



class ChatBot:
    def __init__(self, root):
        self.root = root
        self.root.title("GEHU Chat Bot")
        self.root.geometry("730x620+0+0")

        main_frame = Frame(self.root, bd=10, bg='black', width=610)
        main_frame.pack()

        img_chat = Image.open('chatbot/logo.jpg')
        img_chat = img_chat.resize((150, 100), Image.BICUBIC)

        self.photoimg = ImageTk.PhotoImage(img_chat)

        Title_label = Label(main_frame, bd=3, relief=RAISED, anchor='nw', width=730, image=self.photoimg,
                            text='CHAT ME', font=('arial', 20, 'bold'), fg='white', bg='black', compound='left')
        Title_label.pack(side=TOP)

        self.scroll_y = ttk.Scrollbar(main_frame,orient=VERTICAL)
        self.text = Text(main_frame,width=50,height=20,bd=3,relief=RAISED,font=('arial',15),yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT,fill=Y)
        self.text.pack()

        btn_frame = Frame(self.root,bd=4,bg = 'black',width=730)
        btn_frame.pack()
        label_1= Label(btn_frame,text="Chat",font=('arial', 10, 'bold'), fg='white', bg='black', compound='left')
        label_1.grid(row=0,column=0,padx=5,sticky=W)




if __name__ == '__main__':
    root = Tk()
    obj = ChatBot(root)
    root.mainloop()
