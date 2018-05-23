# -*- encoding: utf-8 -*-

import tkinter as tk
from adb_util import *


class CWnd:
    def __init__(self):
        self.adb = AdbUtil()

        self.root = tk.Tk()
        # self.root.geometry('800x800')

        self.device_list = tk.Listbox(self.root, selectmode=tk.SINGLE)
        self.device_list.pack(side='left')

        self.refresh_device = tk.Button(self.root, text='刷新设备列表', command=self.on_refresh_device)
        self.refresh_device.pack()

        self.show_virtual_keys = tk.Button(self.root, text='显示虚拟按键', command=self.on_show_virtual_keys)
        self.show_virtual_keys.pack()

        self.screencap = tk.Button(self.root, text='截屏', command=self.on_screencap)
        self.screencap.pack()

        # self.screencap_image = tk.Label(self.root, text='截屏图片')
        # self.screencap_image.pack()

        self.press_home = tk.Button(self.root, text='HOME', command=self.on_press_home)
        self.press_home.pack()

        self.press_back = tk.Button(self.root, text='BACK', command=self.on_press_back)
        self.press_back.pack()

    def loop(self):
        self.root.mainloop()

    def on_refresh_device(self):
        self.device_list.delete(0, self.device_list.size() - 1)
        lst = self.adb.get_device_list()
        if lst is not None:
            for device in lst:
                self.device_list.insert(0, device)
        if len(lst) > 0:
            self.device_list.select_set(0)

    def on_show_virtual_keys(self):
        if not self.set_current_device():
            return

        self.adb.show_virtual_keys()

    def on_screencap(self):
        if not self.set_current_device():
            return

        image_name = 'sc.png'
        if self.adb.screencap(image_name):
            # screen_image = tk.PhotoImage(file=image_name)
            # self.screencap_image.config(image=screen_image)
            pass

    def on_press_home(self):
        if not self.set_current_device():
            return

        self.adb.press_home()

    def on_press_back(self):
        if not self.set_current_device():
            return

        self.adb.press_back()

    def set_current_device(self):
        index = self.device_list.curselection()
        if index == ():
            print('no device selected')
            return False
        current_device = self.device_list.get(index)
        self.adb.set_device(current_device)
        return True


def main():
    wnd = CWnd()
    wnd.loop()


if __name__ == '__main__':
    main()
