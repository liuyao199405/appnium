"""
from appium import webdriver
import time



desired_caps = dict()
desired_caps['platformName'] = 'ios'
desired_caps['platforVersion'] = '13.1.3'
desired_caps['deviceName'] = 'iphone Xs Max'
desired_caps['app'] = ''

driver = webdriver.Remote('https://localhost:4723/wd/hub',desired_caps)

time.sleep(5)

# 滑动 7-8不能识别手势识别
# driver.execute_script("mobile:swipe",{"direction":"up"})
driver.swipe(100,200,100,50)


driver.quit()
"""