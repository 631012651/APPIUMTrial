from threading import Thread
from selenium import webdriver
from time import ctime
from selenium.webdriver.common.keys import Keys
import time


#测试用例
def test_baidu(host, browser):
    print('start: %s' %ctime())
    print(host, browser)
    dc = {'browserName': browser}
    driver = webdriver.Remote(command_executor=host, desired_capabilities=dc)
    driver.get('http://www.baidu.com')
    time.sleep(2)
    driver.find_element_by_id( "kw").click()
    driver.find_element_by_id( "kw").send_keys("selenium")
    driver.find_element_by_id("kw").send_keys(Keys.ENTER)
    time.sleep(2)
    driver.quit()


if __name__ == '__main__':
        # 启动参数（指定运行主机与浏览器）
    lists = {'http://127.0.0.1:8888/wd/hub': 'chrome',
            'http://127.0.0.1:9999/wd/hub': 'firefox',
            }
    threads = []
    files = range(len(lists))

    for host, browser in lists.items():
        t = Thread(target=test_baidu,args=(host, browser))
        threads.append(t)
    for i in files:
        threads[i].start()
    for j in files:
        threads[j].join()

    print('end: %s:' %ctime())
