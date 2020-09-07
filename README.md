                                                PC端自动化测试
                                                              --Selenium实战


一、环境准备
安装selenium 
	Pip install selenium
安装selenium IDE
安装chromedriver

二、编写测试用例
 以百度测试为例
打开IDE录制脚本
在浏览器右上角，找到selenium IDE的图标，单击打开。如图所示：
 
　2、我们就选择第一种方式来讲，如图：
 
　输入要录制Web的地址，我这里输入的是百度，如图：
 
点击开始录制，插件会直接启动一个谷歌浏览器的页面，并且打开你输入的百度地址，如图
 
这样就录制完成了，点击右上角的红色圆点，然后输入测试用例名称，如图：
 
　右击测试用例，选择导出按钮，如图：
 
选择你喜欢的语言，单机导出按钮，如图：
 
断言
　　通过使用上下文菜单添加验证和断言。（Adding Verifications and Asserts With the Context Menu）
　　如何添加断言呢？在你录制脚本的时候（红色原点变成红色正方形），在页面上的任何地方单击鼠标右键。您将看到一个显示验证和/或断言命令的上下文菜单。
 
插入命令（Insert Command）
　　上面那种断言是在录制中的时候使用，你也可以录制后，手动添加断言，这样使用的插入命令方式进行，如图：
 



 
三、修改脚本
引入unittest、time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import unittest



class TestSearchForSelenium(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_baidu(self):
        url = 'https://www.baidu.com'
        self.driver.get(url)
        self.driver.set_window_size(1167, 692)
        #time.sleep(5)
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.ID, "kw").click()
        self.driver.find_element(By.ID, "kw").send_keys("selenium")
        self.driver.find_element(By.ID, "kw").send_keys(Keys.ENTER)
        time.sleep(3)
        assert self.driver.title == "selenium_百度搜索"

    def tearDown(self):
        time.sleep(5)
        self.driver.quit()

if __name__ == "__main__":

    unittest.main()






                                APPIUM实战
一、	环境准备：
	安装Python3
	安装Python3的Appium库
	安装Android SDK
	安装JDK
	安装Appium
	安装模拟器MUMU
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
