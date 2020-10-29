

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
# 使用headless无界面浏览器模式
#chrome_options.add_argument('--headless') #增加无界面选项
#chrome_options.add_argument('--disable-gpu') #如果不加这个选项，有时定位会出现问题
#chrome_options.add_argument('--user-data-dir= C:/Users/84265/AppData/Local/Google/Chrome/User Data/Default')

# 启动浏览器，获取网页源代码

for page in range(1,4):
    chrome_options =webdriver.ChromeOptions()
    chrome_options.add_argument("--mute-audio")  # 静音
    browser = webdriver.Chrome(options=chrome_options)
    mainUrl = f"http://pub.whut.edu.cn/yw/list.asp?classid=9&page={page}"
    browser.get(mainUrl)
    browser.implicitly_wait(20)
    for i in range(19):
        browser.find_element_by_xpath(f'//*[@class="label_ul_b"]/li[{i + 1}]/a').click()

    # 获取所有窗口
    allw = browser.window_handles
    for index in range(1, len(allw)):  # 注意这里不包括第一个元素
        browser.switch_to.window(allw[index])
        audio = browser.find_element_by_xpath('//*[@class="content_main"]/div[1]/audio')
        browser.execute_script("return arguments[0].play()", audio)  # 这里要调用javascript来播放h5元素
        # browser.find_element_by_tag_name('audio').click()
        time.sleep(300)#每个打卡页面的等待时间
        browser.find_element_by_xpath('//*[@class="contentbox col-sm-12"]/div[6]/span/a').click()b

        # 切换到ifame
        browser.switch_to.frame("layui-layer-iframe1")
        browser.find_element_by_xpath('//*[@class="layui-form"]/div[1]/div/input').send_keys("你的学号")
        time.sleep(2)
        browser.find_element_by_xpath('//*[@class="layui-form"]/div[2]/div/input').send_keys("你的名字")
        time.sleep(2)
        browser.find_element_by_xpath('//*[@class="layui-form"]/div[5]/div/button').click()
        time.sleep(2)
    browser.quit()


#browser.quit()