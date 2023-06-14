from tkinter import *
import win32clipboard as cb

window = Tk()

window.title("Easy Copy Program")
window.geometry("300x120")
window.resizable(False, False)

ipt_label = Label(window, text="복사할 텍스트를 입력하세요.")
ipt_label.pack(pady=10)


def copy_input():
    text = ipt.get()
    cb.OpenClipboard()
    cb.EmptyClipboard()
    cb.SetClipboardText(text)
    cb.CloseClipboard()


ipt = Entry(window, bg="white")
ipt.pack()

copy_btn = Button(window, text="복사하기", command=copy_input)
copy_btn.pack(pady=10, ipady=5)

window.mainloop()