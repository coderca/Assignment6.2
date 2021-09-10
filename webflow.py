from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

PATH ="C:\Program Files\chromedriver_win32\chromedriver.exe"
#youtube automation
driver = webdriver.Chrome(PATH)
driver.get("https://youtube.com/")
print(driver.title)
time.sleep(5)
main = driver.find_element_by_id("contents")
print(main.text)

search = driver.find_element_by_id("search")
search.send_keys("selenium")
search.send_keys(Keys.RETURN)
time.sleep(5)



video = driver.find_element_by_xpath("/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/div/div[1]/div/h3/a")
video.click()
time.sleep(5)
like = driver.find_element_by_xpath("/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[6]/div[2]/ytd-video-primary-info-renderer/div/div/div[3]/div/ytd-menu-renderer/div/ytd-toggle-button-renderer[1]/a/yt-icon-button")
like.click()
time.sleep(5)
signin = driver.find_element_by_xpath("/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown[2]/div/ytd-modal-with-title-and-button-renderer/div/ytd-button-renderer/a/tp-yt-paper-button")
signin.click()
time.sleep(5)
driver.back()
time.sleep(5)
pause = driver.find_element_by_xpath("/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div/div/div/ytd-player/div/div/div[31]/div[2]/div[1]/button")
pause.click()
time.sleep(5)
search = driver.find_element_by_id("search")
search.send_keys("automation")
search.send_keys(Keys.RETURN)
time.sleep(5)

#form automation
driver = webdriver.Chrome(PATH)
driver.get("https://studentformapp.herokuapp.com/")
print(driver.title)
time.sleep(5)

add = driver.find_element_by_xpath("/html/body/div/div/div/p[2]/a")
add.click()
usn = driver.find_element_by_id("usn")
name = driver.find_element_by_id("name")
select = Select(driver.find_element_by_id("sem"))
branch = driver.find_element_by_id("branch")
usn.send_keys("1307")
name.send_keys("Tony Stark")
select.select_by_value("6")
branch.send_keys("CSE")
time.sleep(5)
sub = driver.find_element_by_id("submit")
sub.click()
time.sleep(5)
ret = driver.find_element_by_xpath("/html/body/div/div/div/p[3]/a")
ret.click()
time.sleep(5)
new = driver.find_element_by_xpath("/html/body/div/div/div/ul/li[1]/a")
new.click()


time.sleep(6)
#game automation
driver = webdriver.Chrome(PATH)
driver.get("https://orteil.dashnet.org/cookieclicker/")
print(driver.title)
time.sleep(5)

driver.implicitly_wait(5)

cookie = driver.find_element_by_id("bigCookie")
cookie_count = driver.find_element_by_id("cookies")
items = [driver.find_element_by_id("productPrice" + str(i)) for i in range(1,-1,-1)]

actions = ActionChains(driver)
actions.click(cookie)

for i in range(5000):
    actions.perform()
    count = int(cookie_count.text.split(" ")[0])
    for item in items:
        value = int(item.text)
        if value <=count:
            upgrade_actions = ActionChains(driver)
            upgrade_actions.move_to_element(item)
            upgrade_actions.click()
            upgrade_actions.perform()

