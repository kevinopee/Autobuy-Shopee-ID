# Autobuy-bot-for-E-Commerce

> Tested in Shopee ID.

-----

Using Python 3.9 , driven with Selenium and undetected-chromedriver from https://github.com/ultrafunkamsterdam/undetected-chromedriver which is awesome.

My first python project made by myself, and a lil help from youtube and stackoverflow :D.

This project is only for **educational purposes**.
I'm not responsible for any *causes* by using these codes.

> Read the requirements before using this codes.

-----

## To run headless browser, add this code in chrome options attribute : 

```py
options.headless = True
```

```py
options.add_argument("--headless")
```
> Update : Already add the codes above as an options, you can run headless or normal view

-----

## Input the minute to start buying stuff : 

```py
menit = int(input("Masukan menit untuk memulai beli : "))
```
> Ex : Flash sale start at 12 A.M, which is 00.00 in our real-time clock. input the first 2 digit : 00

-----

## Steps :
  - Clone this repo.
  - Fill your account information such as phone number/email, and a pin number for your payment in account file.
  - Add a proxy/socks5 server is the best options. VPN might be better.
  - Run the save_cookies file first, this file for saving your account, no need to login anymore. Dont **RUN** this code in headless mode.
  - Input your verification code manually, cause the value of the text box is readonly. Still looking forward to fix this.
  - It will made a new .pkl file, don't delete it, except you want to use another account.
  - Then you ready to go with shopee_bot file.  *You can run this in headless mode, for more speed*.
  
  -----
 
 > Update : Added a new warning if there is no cookie exception.
 
 Sorry for my bad English. :p
