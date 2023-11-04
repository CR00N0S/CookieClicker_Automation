from selenium import webdriver
from selenium.webdriver.common.by import By


crome = webdriver.ChromeOptions()
crome.add_experimental_option("detach", True)

web = webdriver.Chrome(options=crome)
web.get("https://www.python.org")

data = web.find_element(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]/div/ul').text
lines = data.strip().split('\n')


# Initialize an empty dictionary to store the results
r = []
u = []

print(lines)
for i in range(10):
    if i % 2 == 0:
        r.append(lines[i])
    else:
        u.append(lines[i])

# Now, r and u should contain the desired data.

p = {}
for i in range(5):
    p[r[i]] = u[i]

print(p)
