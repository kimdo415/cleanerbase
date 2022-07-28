from pyrsistent import b
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyperclip
import clipboard

# 한개만 지워짐 알아서 개조하셈 구조는 매우 베이직하게만 맞췄음 

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
browser = webdriver.Chrome(options=options)
browser.get("https://www.dcinside.com/")


# 로그인 창에 아이디/비밀번호 입력
loginID = "입력해서 바꾸기"
clipboard.copy(loginID)
browser.find_element_by_xpath('//*[@id="user_id"]').send_keys(Keys.CONTROL, 'v')

loginPW = "입력해서 바꾸기"
clipboard.copy(loginPW)
browser.find_element_by_xpath('//*[@id="pw"]').send_keys(Keys.CONTROL, 'v')
time.sleep(1)

# 로그인 버튼 클릭
browser.find_element_by_xpath('//*[@id="login_ok"]').click()

browser.get("https://gallog.dcinside.com/"+loginID)
try:
   loginID==None
except Nonelogin as Nl:
    print("아이디 없음")    

browser.find_element_by_xpath('//*[@id="container"]/article/div/div[1]/ul/li[3]/a').click()

browser.find_element_by_xpath('//*[@id="container"]/article/div/div[1]/ul/li[3]/a').click()

# 이부분만 좀 개조하세용
for i in range(5):
    browser.find_element_by_xpath('//*[@id="container"]/article/div/div[3]/section/div[1]/div/ul/li[1]/div/div/button').click()
    time.sleep(3)
    browser.switch_to.alert.accept()
# browser.find_element_by_xpath('//*[@id="container"]/article/div/div[3]/section/div[1]/div/ul/li[1]/div/div/button').click()

# time.sleep(4)
# browser.switch_to.alert.accept()
