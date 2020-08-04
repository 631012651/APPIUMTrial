APPIUM实战
一、	环境准备：
?	安装Python3
?	安装Python3的Appium库
?	安装Android SDK
?	安装JDK
?	安装Appium
?	安装模拟器MUMU
二、	模拟器测试
连接模拟器：
adb connect 127.0.0.1:7555
填写所需功能：
platformName ：声明是ios还是Android系统
platformVersion： Android内核版本号，可通过命令adb shell getprop ro.build.version.release查看
deviceName ：连接的设备名称，通过命令adb devices -l中model查看
 
appPackage：apk的包名
appActivity：apk的launcherActivity，通过命令adb shell dumpsys activity | findstr “mResume”查看（需先打开手机应用）
 
注意：添加automationName：UiAutomator1
启动会话
右侧 Selected Element/选定的元素 区域有三个按钮
TAP/点击：执行选中元素的点击事件
Send Keys/发送密钥：为文本框等对象传值
如果是文本输入元素，就清除文本

 
编写脚本
创建testcase目录，创建test_app.py

import time
import unittest

from appium import webdriver


class MyTests(unittest.TestCase):
    # 测试开始前执行的方法
    def setUp(self):
        desired_caps = {'platformName': 'Android', # 平台名称
                        'platformVersion': '6.0.1',  # 系统版本号
                        'deviceName': 'MuMu',  # 设备名称。如果是真机，在'设置->关于手机->设备名称'里查看
                        'appPackage': 'com.youdao.calculator',  # apk的包名
                        'appActivity': '.activities.MainActivity', # activity 名称
                        'automationName':'UiAutomator1'
                        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)  # 连接Appium
        self.driver.implicitly_wait(8)

    def test_calculator(self, t=500, n=4):
        """计算器测试"""
        time.sleep(3)
        window = self.driver.get_window_size()
        x0 = window['width'] * 0.8  # 起始x坐标
        x1 = window['width'] * 0.2  # 终止x坐标
        y = window['height'] * 0.5  # y坐标
        for i in range(n):
            self.driver.swipe(x0, y, x1, y, t)
            time.sleep(1)
        self.driver.find_element_by_id('com.youdao.calculator:id/guide_button').click()
        for i in range(5):
            self.driver.find_element_by_accessibility_id('Mathbot Editor').click()
            time.sleep(1)

        btn_xpath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout[3]/android.view.ViewGroup/android.widget.GridView/android.widget.FrameLayout[{p}]/android.widget.FrameLayout'
        self.driver.find_element_by_xpath(btn_xpath.format(p='7')).click()
        self.driver.find_element_by_xpath(btn_xpath.format(p='10')).click()
        self.driver.find_element_by_xpath(btn_xpath.format(p='8')).click()
        time.sleep(3)

    # 测试结束后执行的方法
    def tearDown(self):
        self.driver.quit()
创建run.py
import os
import time
import unittest

from HTMLTestRunner import HTMLTestRunner

test_dir = ''
discover = unittest.defaultTestLoader.discover(start_dir='./testcase', pattern="test*.py")

if __name__ == "__main__":
    report_dir = './test_report'
    os.makedirs(report_dir, exist_ok=True)
    now = time.strftime("%Y-%m-%d %H-%M-%S")
    report_name = '{0}/{1}.html'.format(report_dir, now)

    with open(report_name, 'wb')as f:
        runner = HTMLTestRunner(stream=f, title="测试报告", description="本测试报告内容包含超级计算器的简单测试")
        runner.run(discover)


注意：HTMLTestRunner与python3不兼容需要修改，方能生成测试报告
