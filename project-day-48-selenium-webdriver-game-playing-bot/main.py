from selenium import webdriver
import time

GAME_DURATION_MIN = 5
BUY_NEW_ITEM_SEC = 5

chrome_driver_path = "/Users/nganguyen/Development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element_by_id("cookie")

timeout = time.time() + 60*GAME_DURATION_MIN
time_to_buy = time.time() + BUY_NEW_ITEM_SEC

game_is_on = True
while game_is_on:

    cookie.click()

    if time.time() > timeout:
        cps = driver.find_element_by_id("cps").text
        print(cps)
        break

    if time.time() > time_to_buy:
        money = int(driver.find_element_by_id("money").text.replace(",", ""))

        upgrades = driver.find_elements_by_css_selector("#store b")
        # The following line can lead to a selenium.common.exceptions.StaleElementReferenceException Error if
        # time_to_buy is too small
        store = {up.text.split(" - ")[0]: int(up.text.split(" - ")[1].replace(",", "")) for up in upgrades[:-1]}

        most_expensive_affordable = [(item, cost) for (item, cost) in store.items() if cost < money]

        if most_expensive_affordable:
            # print(most_expensive_affordable[-1][0])
            buy = driver.find_element_by_id(f"buy{most_expensive_affordable[-1][0]}")
            buy.click()

        time_to_buy += BUY_NEW_ITEM_SEC

driver.quit()
