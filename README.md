# Android Controller

在电脑上控制手机的控制器，基于 Python3 + PyQt5。

**目录**

<!-- vim-markdown-toc GFM -->

* [截图](#截图)
* [用法](#用法)
* [需求 list](#需求-list)
* [开发](#开发)
* [注意事项](#注意事项)

<!-- vim-markdown-toc -->

## 截图

<div align="center"><img width="640" src="./screenshots/main.png" /></div>

## 用法

> 请确保已经安装 adb 且已添加到 PATH 环境变量中，手机已经开启「USB调试」。

1. 安装 Python3；

2. 安装依赖库；

    ```sh
    pip3 install -r requirements.txt
    ```
3. 运行

    ```sh
    python3 main.py
    ```

## 需求 list

- [X] 截图
- [X] 拖拽 APK 文件安装应用
- [ ] 卸载应用
- [X] 覆盖安装
- [ ] 清除数据
- [ ] 录屏
- [ ] 打开 WiFi
- [ ] 关闭 WiFi
- [ ] 屏幕点击事件
- [ ] 屏幕滑动事件

## 开发

新版基于 PyQt5，main-window.ui 文件使用 Qt Designer 编辑，从 .ui 文件生成 MainWindow.py 文件：

```sh
pyuic5 main-window.ui MainWindow.py
```

## 注意事项

* 模拟按键的功能在部分机型（比如小米）需要在「开发者选项」里打开允许通过 USB 调试修改权限或模拟点击的开关。
