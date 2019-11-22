from selenium import webdriver
import time

driver = webdriver.Chrome()
url = 'http://32.9.106.12 '
driver.get(url)
print(driver.title)
# driver.quit()

# 找到用户名的框框
name_input = driver.find_element_by_id('UserName')
# 找到输入密码的框框
pass_input = driver.find_element_by_id('Password')
# 找到登录按钮
login_button = driver.find_element_by_xpath('loginbtn')

# name_input.clear()
# 填写用户名
name_input.send_keys('admin')
time.sleep(0.2)
# pass_input.clear()
# 填写密码
pass_input.send_keys('12345')
time.sleep(0.2)
login_button.click()

# 点击配置
time.sleep(1)
imenu5 = driver.find_elements_by_id('iMenu5')
imenu5.click()

time.sleep(10)
# 切换到frame
driver.switch_to.frame('contentframe')

# 切换到字符叠加
adeviceoverlay = driver.find_elements_by_id('aDeviceOverlay')
adeviceoverlay.click()

# 切换到视频叠加
time.sleep(1)
aOSDSetting = driver.find_elements_by_id('aOSDSettings')
aOSDSetting.click()

# 找到通道名
channelname = driver.find_elements_by_id()
channelname.click()
# channelname.clear()
# channelname.send_keys(11111)
channelname.get_attribute("value")
print(channelname.get_attribute("value"))
