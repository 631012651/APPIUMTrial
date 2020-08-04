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
        self.driver.implicitly_wait(1)

    def test_calculator(self, t=200, n=3):
        """计算器测试"""

        time.sleep(1)
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
            time.sleep(0)

        btn_xpath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout[3]/android.view.ViewGroup/android.widget.GridView/android.widget.FrameLayout[{p}]/android.widget.FrameLayout'
        self.driver.find_element_by_xpath(btn_xpath.format(p='7')).click()
        self.driver.find_element_by_xpath(btn_xpath.format(p='10')).click()
        self.driver.find_element_by_xpath(btn_xpath.format(p='8')).click()


        time.sleep(1)
        '''
        if result==56:
            print ("测试通过")
        else:
            print ("测试失败")
            '''
    # 测试结束后执行的方法
    def tearDown(self):
        self.driver.quit()

