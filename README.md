APPIUMʵս
һ��	����׼����
?	��װPython3
?	��װPython3��Appium��
?	��װAndroid SDK
?	��װJDK
?	��װAppium
?	��װģ����MUMU
����	ģ��������
����ģ������
adb connect 127.0.0.1:7555
��д���蹦�ܣ�
platformName ��������ios����Androidϵͳ
platformVersion�� Android�ں˰汾�ţ���ͨ������adb shell getprop ro.build.version.release�鿴
deviceName �����ӵ��豸���ƣ�ͨ������adb devices -l��model�鿴
 
appPackage��apk�İ���
appActivity��apk��launcherActivity��ͨ������adb shell dumpsys activity | findstr ��mResume���鿴�����ȴ��ֻ�Ӧ�ã�
 
ע�⣺���automationName��UiAutomator1
�����Ự
�Ҳ� Selected Element/ѡ����Ԫ�� ������������ť
TAP/�����ִ��ѡ��Ԫ�صĵ���¼�
Send Keys/������Կ��Ϊ�ı���ȶ���ֵ
������ı�����Ԫ�أ�������ı�

 
��д�ű�
����testcaseĿ¼������test_app.py

import time
import unittest

from appium import webdriver


class MyTests(unittest.TestCase):
    # ���Կ�ʼǰִ�еķ���
    def setUp(self):
        desired_caps = {'platformName': 'Android', # ƽ̨����
                        'platformVersion': '6.0.1',  # ϵͳ�汾��
                        'deviceName': 'MuMu',  # �豸���ơ�������������'����->�����ֻ�->�豸����'��鿴
                        'appPackage': 'com.youdao.calculator',  # apk�İ���
                        'appActivity': '.activities.MainActivity', # activity ����
                        'automationName':'UiAutomator1'
                        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)  # ����Appium
        self.driver.implicitly_wait(8)

    def test_calculator(self, t=500, n=4):
        """����������"""
        time.sleep(3)
        window = self.driver.get_window_size()
        x0 = window['width'] * 0.8  # ��ʼx����
        x1 = window['width'] * 0.2  # ��ֹx����
        y = window['height'] * 0.5  # y����
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

    # ���Խ�����ִ�еķ���
    def tearDown(self):
        self.driver.quit()
����run.py
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
        runner = HTMLTestRunner(stream=f, title="���Ա���", description="�����Ա������ݰ��������������ļ򵥲���")
        runner.run(discover)


ע�⣺HTMLTestRunner��python3��������Ҫ�޸ģ��������ɲ��Ա���
