# -*- encoding: utf-8 -*-

import tkinter as tk
from adb_util import *


class CWnd(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master, width=400, height=300)
        self.pack()

        self.adb = AdbUtil()

        self.screen_image = None
        self.screencap_image = tk.Label(self, text='截屏图片')
        self.screencap_image.pack(side='left')

        self.device_list = tk.Listbox(self, selectmode=tk.SINGLE)
        self.device_list.pack()

        self.refresh_device = tk.Button(self, text='刷新设备列表', command=self.on_refresh_device)
        self.refresh_device.pack(fill=tk.X)

        self.show_virtual_keys = tk.Button(self, text='显示虚拟按键', command=self.on_show_virtual_keys)
        self.show_virtual_keys.pack(fill=tk.X)

        self.screencap = tk.Button(self, text='截屏', command=self.on_screencap)
        self.screencap.pack(fill=tk.X)

        self.press_menu = tk.Button(self, text='MENU', command=self.on_press_menu)
        self.press_menu.pack(fill=tk.X)

        self.press_home = tk.Button(self, text='HOME', command=self.on_press_home)
        self.press_home.pack(fill=tk.X)

        self.press_back = tk.Button(self, text='BACK', command=self.on_press_back)
        self.press_back.pack(fill=tk.X)

        self.press_power = tk.Button(self, text='电源键', command=self.on_press_power)
        self.press_power.pack(fill=tk.X)

        self.volume_up = tk.Button(self, text='音量+', command=self.on_volume_up)
        self.volume_up.pack(fill=tk.X)

        self.volume_down = tk.Button(self, text='音量-', command=self.on_volume_down)
        self.volume_down.pack(fill=tk.X)

        self.mute = tk.Button(self, text='静音', command=self.on_mute)
        self.mute.pack(fill=tk.X)

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
            self.screen_image = tk.PhotoImage(file=image_name)
            self.screen_image = self.screen_image.subsample(3)
            self.screencap_image.config(image=self.screen_image)
            pass

    def on_press_menu(self):
        if not self.set_current_device():
            return

        self.adb.press_menu()

    def on_press_home(self):
        if not self.set_current_device():
            return

        self.adb.press_home()

    def on_press_back(self):
        if not self.set_current_device():
            return

        self.adb.press_back()

    def on_press_power(self):
        if not self.set_current_device():
            return

        self.adb.press_power()

    def on_volume_up(self):
        if not self.set_current_device():
            return

        self.adb.volume_up()

    def on_volume_down(self):
        if not self.set_current_device():
            return

        self.adb.volume_down()

    def on_mute(self):
        if not self.set_current_device():
            return

        self.adb.mute()

    def set_current_device(self):
        index = self.device_list.curselection()
        if index == ():
            print('no device selected')
            return False
        current_device = self.device_list.get(index)
        self.adb.set_device(current_device)
        return True


def main():
    root = tk.Tk()
    wnd = CWnd(root)
    root.mainloop()


if __name__ == '__main__':
    main()
