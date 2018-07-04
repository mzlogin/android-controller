# -*- encoding: utf-8 -*-

import os
import sys
import getopt
import re
import math


class AdbUtil(object):

    def __init__(self, device=''):
        self.device = ''
        self.cmd_prefix = ''
        self.set_device(device)

    def set_device(self, device):
        self.device = device
        if self.device == '' or self.device is None:
            self.cmd_prefix = 'adb'
        else:
            self.cmd_prefix = 'adb -s %s' % self.device

    def touch(self, coordinate):
        self.run_device_cmd('shell input tap %d %d' % (coordinate[0], coordinate[1]))

    def get_resolution(self):
        pattern = re.compile(r'.* (\d+)x(\d+).*')
        output = self.run_device_cmd('shell wm size')
        rematch = pattern.match(output)
        if rematch is not None:
            resolution = [int(rematch.group(1)), int(rematch.group(2))]
            return resolution
        else:
            return None

    def get_density(self):
        pattern = re.compile(r'Physical density: (\d+)')
        output = self.run_device_cmd('shell wm density')
        rematch = pattern.match(output)
        if rematch is not None:
            density = int(rematch.group(1))
            return density
        else:
            return None

    def get_screen_size(self):
        """
        notice: not exactly
        """
        resolution = self.get_resolution()
        if resolution is None:
            return None

        density = self.get_density()
        if density is None:
            return None

        return math.sqrt(math.pow(resolution[0], 2) + math.pow(resolution[1], 2)) / density

    def get_ip(self):
        pattern = re.compile(r'wlan0: ip ([\d\.]+) mask.*')
        output = self.run_device_cmd('shell ifconfig wlan0')
        rematch = pattern.match(output)
        if rematch is None:
            rematch = re.search(r'.*inet addr:([\d\.]+)  Bcast:.*', output)

        if rematch is not None:
            ip = rematch.group(1)
            return ip
        else:
            return None

    def listen(self, port):
        pattern = re.compile(r'restarting in TCP mode port.*')
        output = self.run_device_cmd('tcpip %d' % port)

        if len(output) == 0:  # special case for Nexus 5
            return True

        rematch = pattern.match(output)
        if rematch is not None:
            return True
        else:
            return False

    def connect_wireless(self):
        ip = self.get_ip()
        if ip is None:
            return False

        if not self.listen(5555):
            return False

        pattern = re.compile(r'connected to .*')
        output = self.run_device_cmd('connect %s' % ip)
        rematch = pattern.match(output)
        if rematch is not None:
            return True
        else:
            return False

    def screencap(self, filename):
        sdfile = '/sdcard/%s' % filename
        self.run_device_cmd('shell screencap -p %s' % sdfile)
        self.run_device_cmd('pull %s' % sdfile)
        return os.path.exists(filename)

    def get_device_list(self):
        output = self.run_cmd('adb devices')
        rematch = re.findall(r'\n(.*)\tdevice', output)
        return rematch

    def keyevent(self, keycode):
        self.run_device_cmd('shell input keyevent %d' % keycode)

    def press_menu(self):
        self.keyevent(82)

    def press_home(self):
        self.keyevent(3)

    def press_back(self):
        self.keyevent(4)

    def press_power(self):
        self.keyevent(26)

    def volume_up(self):
        self.keyevent(24)

    def volume_down(self):
        self.keyevent(25)

    def mute(self):
        self.keyevent(164)

    def show_virtual_keys(self):
        output = self.run_device_cmd('shell am startservice -n com.android.systemui/.SystemUIService')
        if output.find('Starting service') is not None:
            return True
        else:
            return False

    def get_current_focused_activity(self):
        output = self.run_device_cmd('shell dumpsys activity activities | grep mFocusedActivity')

        pattern = re.compile(r'.* ([^ ]*/[^ ]*) .*')
        rematch = pattern.match(output)
        if rematch is not None:
            output = rematch.group(1)
        return output

    def run_device_cmd(self, cmd):
        command = '%s %s' % (self.cmd_prefix, cmd)
        return self.run_cmd(command)

    @staticmethod
    def run_cmd(cmd):
        proc = os.popen(cmd)
        output = ''.join(proc.readlines())
        proc.close()
        return output


def usage():
    print("""
          usage: python adb_util.py [options]

          Available options:

          -s | --size       get screen size in Inch
          -r | --resolution get resolution
          -d | --density    get density
          -w | --wireless   connect device wireless
          -i | --ip         get ip
          -p | --screencap  save screencap to file
          """)


def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'srdwip:',
                                   ['size', 'resolution', 'density', 'wireless', 'ip', 'screepcap='])
    except getopt.GetoptError as err:
        opts = []

    if len(opts) == 0:
        usage()
        opts = [('-s', '')]

    adb = AdbUtil()

    for o, a in opts:
        if o in ('-s', '--size'):
            size = adb.get_screen_size()
            if size is None:
                print('get screen size failed')
            else:
                print('screen size is %f inch' % size)
        elif o in ('-r', '--resolution'):
            resolution = adb.get_resolution()
            if resolution is None:
                print('get resolution failed')
            else:
                print('resolution is %dx%d' % (resolution[0], resolution[1]))
        elif o in ('-d', '--density'):
            density = adb.get_density()
            if density is None:
                print('get density failed')
            else:
                print('density is %d' % density)
        elif o in ('-w', '--wireless'):
            ret = adb.connect_wireless()
            if ret:
                print('connect wireless succeed')
            else:
                print('connect wireless failed')
        elif o in ('-i', '--ip'):
            ip = adb.get_ip()
            if ip is None:
                print('get ip failed')
            else:
                print('ip is %s' % ip)
        elif o in ('-p', '--screencap'):
            ret = adb.screencap(a)
            if ret:
                print('save screencap to %s' % a)
            else:
                print('screencap failed')


if __name__ == '__main__':
    main()
