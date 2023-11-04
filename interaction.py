from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

web = webdriver.Chrome(options=chrome_options)
web.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = web.find_element(By.XPATH, '//*[@id="cookie"]')
timeout = time.time() + 5


upgrades = [
    "buyCursor", "buyGrandma", "buyFactory", "buyMine",
    "buyShipment", "buyAlchemy lab", "buyPortal", "buyTime machine"
]

# Initialize a dictionary to store upgrade costs
upgrade_costs = {}

while True:
    cookie.click()
    if time.time() > timeout:
        # Update upgrade costs
        for upgrade_id in upgrades:
            try:
                element = web.find_element(By.ID, upgrade_id)
                cost_text = element.find_element(By.XPATH, './b').text
                cost = int(cost_text.split('-')[1].strip().replace(',', ''))
                upgrade_costs[upgrade_id] = cost
            except Exception as e:
                print(f"Failed to retrieve cost for {upgrade_id}: {e}")

        # Find affordable upgrades and buy the most expensive one
        money_element = web.find_element(By.ID, "money").text
        money = int(money_element.replace(',', ''))
        affordable_upgrades = {upgrade_id: cost for upgrade_id, cost in upgrade_costs.items() if cost <= money}
        print(affordable_upgrades)

        if affordable_upgrades:
            highest_price_affordable_upgrade = max(affordable_upgrades)
            web.find_element(By.ID, highest_price_affordable_upgrade).click()

        # Reset the timeout for the next check
        timeout = time.time() + 5

    # Break out of the loop if the purchase timeout is reached
