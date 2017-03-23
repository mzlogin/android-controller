#-*- encoding: utf-8 -*-

import Tkinter as tk

class CWnd:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('300x200')
        self.text = tk.Text(self.root, background='black', foreground='white')
        self.text.pack()
        self.root.bind('<KeyPress>', self.onKeyPress)

    def onKeyPress(self, event):
        self.text.delete(1.0, tk.END)
        self.text.insert(tk.END, 'You pressed %d\n' % event.keycode)

    def loop(self):
        self.root.mainloop()

def main():
    wnd = CWnd()
    wnd.loop()

if __name__ == '__main__':
    main()
