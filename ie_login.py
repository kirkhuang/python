from selenium import webdriver
import time

# driver = webdriver.Ie()
# url = 'http://byxoa.byx-its.com:88/byxoa'
# driver.get(url)
# print(driver.title)
# # driver.quit()

# # 找到用户名的框框
# name_input = driver.find_element_by_id('namefield')
# # 找到输入密码的框框
# pass_input = driver.find_element_by_id('pwdfield')
# # 找到登录按钮
# login_button = driver.find_element_by_xpath('//*[@id="loginArea"]/div[3]/a/img')

# # name_input.clear()
# # 填写用户名
# name_input.send_keys('a')
# time.sleep(0.2)
# # pass_input.clear()
# # 填写密码
# pass_input.send_keys('1')
# time.sleep(0.2)
# login_button.click()


driver = webdriver.Ie()
url = 'http://32.91.106.12'
driver.get(url)
print(driver.title)

# 找到用户名的框框
name_input = driver.find_element_by_id('UserName')
# 找到输入密码的框框
pass_input = driver.find_element_by_id('Password')
# 找到登录按钮
login_button = driver.find_element_by_xpath('/html/body/div/d')

# name_input.clear()
# 填写用户名
name_input.send_keys('admin')
time.sleep(0.2)
# pass_input.clear()
# 填写密码
pass_input.send_keys('12345')
time.sleep(0.2)
login_button.click()
