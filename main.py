# -*- encoding: utf-8 -*-

import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from adb_util import *


class CWnd(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master, width=400, height=300)
        self.pack()

        self.adb = AdbUtil()

        self.screen_image = None
        self.screencap_image = ttk.Label(self, text='截屏图片')
        self.screencap_image.pack(side='left')

        self.current_device = tk.StringVar()
        self.device_list = ttk.Combobox(self, textvariable=self.current_device)
        self.device_list.pack()

        self.refresh_device = ttk.Button(self, text='刷新设备列表', command=self.on_refresh_device)
        self.refresh_device.pack(fill=tk.X)

        self.show_virtual_keys = ttk.Button(self, text='显示虚拟按键', command=self.on_show_virtual_keys)
        self.show_virtual_keys.pack(fill=tk.X)

        self.screencap = ttk.Button(self, text='截屏', command=self.on_screencap)
        self.screencap.pack(fill=tk.X)

        self.press_menu = ttk.Button(self, text='MENU', command=self.on_press_menu)
        self.press_menu.pack(fill=tk.X)

        self.press_home = ttk.Button(self, text='HOME', command=self.on_press_home)
        self.press_home.pack(fill=tk.X)

        self.press_back = ttk.Button(self, text='BACK', command=self.on_press_back)
        self.press_back.pack(fill=tk.X)

        self.press_power = ttk.Button(self, text='电源键', command=self.on_press_power)
        self.press_power.pack(fill=tk.X)

        self.volume_up = ttk.Button(self, text='音量+', command=self.on_volume_up)
        self.volume_up.pack(fill=tk.X)

        self.volume_down = ttk.Button(self, text='音量-', command=self.on_volume_down)
        self.volume_down.pack(fill=tk.X)

        self.mute = ttk.Button(self, text='静音', command=self.on_mute)
        self.mute.pack(fill=tk.X)

        self.get_foreground_activity = ttk.Button(self, text='当前 Activity', command=self.on_get_foreground_activity)
        self.get_foreground_activity.pack(fill=tk.X)

        self.output = tk.Text(self, height=5, width=10)
        self.output.pack(fill=tk.X)
        self.set_output('输出')

    def set_output(self, content):
        self.clear_output()
        self.output.insert(tk.END, content)

    def clear_output(self):
        self.output.delete(0.0, tk.END)

    def on_refresh_device(self):
        self.device_list['values'] = []
        self.current_device.set('')
        lst = self.adb.get_device_list()
        if lst is not None:
            self.device_list['values'] = lst
        if len(lst) > 0:
            self.device_list.set(lst[0])

    def on_show_virtual_keys(self):
        if not self.set_current_device():
            return

        self.adb.show_virtual_keys()

    def on_screencap(self):
        if not self.set_current_device():
            return

        image_name = 'sc.png'
        if self.adb.screencap(image_name):
            image = Image.open(image_name)
            resized_image = image.resize(tuple(map(lambda x: int(x / 3), image.size)))
            self.screen_image = ImageTk.PhotoImage(image=resized_image)
            # self.screen_image = tk.PhotoImage(file=image_name)
            # self.screen_image = self.screen_image.subsample(3)
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

    def on_get_foreground_activity(self):
        if not self.set_current_device():
            return

        output = self.adb.get_current_focused_activity()
        self.set_output(output)

    def set_current_device(self):
        if self.current_device.get() == '':
            self.set_output('no device selected')
            return False
        self.adb.set_device(self.current_device.get())
        return True


def main():
    root = tk.Tk()
    root.title('Android Controller')
    wnd = CWnd(root)
    root.mainloop()


if __name__ == '__main__':
    main()
