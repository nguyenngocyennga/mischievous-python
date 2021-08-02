from selenium import webdriver
import time

chrome_driver_path = "/Users/nganguyen/Development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

# Get cookie to click on.
cookie = driver.find_element_by_id("cookie")

timeout = time.time() + 60*5  # 5 minutes
time_to_buy = time.time() + 5

while True:

    cookie.click()

    # After 5 minutes stop the bot and check the cookies per second count.
    if time.time() > timeout:
        cookie_per_second = driver.find_element_by_id("cps").text
        print(cookie_per_second)
        break

    # Every 5 seconds:
    if time.time() > time_to_buy:
        # Get current cookie count
        money = int(driver.find_element_by_id("money").text.replace(",", ""))

        # Create dictionary of store items and prices
        store = driver.find_elements_by_css_selector("#store b")
        upgrades = {item.text.split(" - ")[0]: int(item.text.split(" - ")[1].replace(",", "")) for item in store[:-1]}

        # Find upgrades that we can currently afford
        most_expensive_affordable = [(item, cost) for (item, cost) in upgrades.items() if cost < money]

        # Purchase the most expensive affordable upgrade
        if most_expensive_affordable:
            buy = driver.find_element_by_id(f"buy{most_expensive_affordable[-1][0]}")
            buy.click()

        # Add another 5 seconds until the next check
        time_to_buy += 5

driver.quit()
