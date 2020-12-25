import time
import datetime
import pyfiglet as f
import undetected_chromedriver as UC
import pickle
import account as ac

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import *
from fake_useragent import UserAgent

UC.TARGET_VERSION = 87 # You can change your chrome version target

options = UC.ChromeOptions()
options.headless = False
# Add proxy to become more invisible
server = input("Proxy / Socks5 / Nope : ")
if server.lower == "proxy":
    proxy = input("Masukan proxy : ")
    options.add_argument(f'--proxy-server={proxy}')
elif server.lower == "socks5":
    socks5 = input("Masukan socks5 : ")
    options.add_argument(f'--proxy-server=socks5://{socks5}')
else:
    pass
options.add_argument('--disable-extensions')
# Some WEBSITE dont accept random version of user agent, make sure your choice
# Sorry for my bad english hehe
# ua = UserAgent()
# userAgent = ua.random
# print(userAgent)
# options.add_argument(f'user-agent={userAgent}')
prefs = {"profile.default_content_setting_values.notifications": 2, "credentials_enable_service": False, "profile.password_manager_enabled" : False}
options.add_experimental_option("prefs", prefs)
browser = UC.Chrome(options=options, enable_console_log=True)

def authors():
    style = f.figlet_format("Shopee Autobuy")
    print(style)
    print("----- Github : https://github.com/kevinopee -----")
    print("-----  E-mail : helloimscarface@gmail.com   -----")

def load_cookies():
    browser.get("https://shopee.co.id")
    try:
        cookies = pickle.load(open("cookies.pkl", "rb"))
        for cookie in cookies:
            browser.add_cookie(cookie)
    except NoSuchCookieException as e:
        print(e)

def tombol_beli():
    try:
        beli = WebDriverWait(browser, 60).until(EC.element_to_be_clickable((
                By.XPATH, '//*[@id="main"]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[5]/div/div/button[2]')))
        browser.execute_script("arguments[0].click();", beli)
        print("- Barang terbeli!")
        print(datetime.datetime.now().microsecond)
        # iframe = WebDriverWait(browser, 60).until(EC.frame_to_be_available_and_switch_to_it((
        #        By.XPATH, '# //*[@id="main"]/div/div[2]/div[2]')))
        checkout = WebDriverWait(browser, 60).until(EC.element_to_be_clickable((
                By.XPATH, '//*[@id="main"]/div/div[2]/div[2]/div[3]/div[2]/div[7]/div[5]/button/span')))
        browser.execute_script("arguments[0].click();", checkout)
        print("- Barang tercheckout!")
        print(datetime.datetime.now().microsecond)
        pesanan = WebDriverWait(browser, 60).until(EC.element_to_be_clickable((
                By.XPATH, '//*[@id="main"]/div/div[2]/div[3]/div[4]/div[2]/div[7]/button')))
        browser.execute_script("arguments[0].click();", pesanan)
        print("- Barang terpesan!")
        print(datetime.datetime.now().microsecond)
        bayar = WebDriverWait(browser, 60).until(EC.element_to_be_clickable((
                By.ID, 'pay-button'))).click()
        browser.execute_script("arguments[0].click();", bayar)
        print("- Barang terbayar!")
        pin_shopee = WebDriverWait(browser, 60).until(EC.element_to_be_clickable((
                By.XPATH, '//*[@id="pin-popup"]/div[1]/div[3]/div[1]')))
        browser.execute_script("arguments[0].click();", pin_shopee)
        pin_shopee.send_keys(ac.pin_number)
    except NoSuchElementException as e:
        print(e)

def main():
    minute = datetime.datetime.now().minute
    authors()
    time.sleep(5)
    load_cookies()
    # Input product link
    link_produk = input("Masukan link produk : ")
    browser.get(link_produk)
    # Input menit
    menit = int(input("Masukan menit untuk memulai beli : "))

    # This is my masterpiece logic piece of shit
    # Ini countdown buat nentuin menit beli 
    while minute != menit:
        minute = datetime.datetime.now().minute

    tombol_beli()

if __name__ == "__main__":
    main()
