from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

TWITTER_USERNAME = "YOUR TWITTER USERNAME"
TWITTER_PASSWORD = "YOUR TWITTER PASSWORD"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://speedtest.net/")
driver.maximize_window()

cancel_cookies = driver.find_element(By.XPATH, '//*[@id="onetrust-close-btn-container"]/button')
cancel_cookies.click()

go = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
go.click()

sleep(45)
download_speed = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div['
                                               '3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
down_speed = download_speed.text

upload_speed = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div['
                                             '3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
up_speed = upload_speed.text

driver.get("https://twitter.com/")
driver.maximize_window()

sleep(1)
sign_in = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div['
                                        '3]/div[5]/a/div')
sign_in.click()

sleep(2)
username = driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div['
                                         '2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div['
                                         '2]/div/input')
username.send_keys(TWITTER_USERNAME)
username.send_keys(Keys.ENTER)

sleep(2)
password = driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div['
                                         '2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
password.send_keys(TWITTER_PASSWORD)
password.send_keys(Keys.ENTER)

sleep(3)
tweet_button = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div['
                                             '3]/a/div')
tweet_button.click()

sleep(2)
driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div['
                              '1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/label/div['
                              '1]/div/div/div/div/div/div[2]/div/div/div/div').send_keys(
  f"Dear Internet Provider,\nI am getting {down_speed}/50Mbps Download and {up_speed}/60Mbps Upload speed. Fix it now!")

sleep(3)
submit = driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div['
                                       '3]/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div['
                                       '4]/div/span/span')
submit.click()
sleep(5)
driver.close()
