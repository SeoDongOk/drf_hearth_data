import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
# import requests
# from bs4 import BeautifulSoup

def getHiddenData():
  ### javascript 랜더링 이슈 맞음 ###
  # r = requests.get("https://www.nhis.or.kr/nhis/etc/personalLoginPage.do")
  # cookies = dict(r.cookies)
  # sp = BeautifulSoup(r.text)
  # hidden_inputs = sp.select('input[type="hidden"]')
  # for input_tag in hidden_inputs:
  #   print(input_tag)
  # login_data = {i.attrs['name']: i.get('value') for i in hidden_inputs}
  # print("\n\n\n",login_data,cookies, "\n\n\n")
  # return login_data,cookies
  ##########


  chrome_options = Options()
  chrome_options.add_argument("--headless")
  chrome_options.add_argument("--disable-gpu")
  chrome_options.add_argument("--no-sandbox")
  chrome_options.add_argument("--disable-dev-shm-usage")

  driver = webdriver.Chrome( options=chrome_options)
  driver.get("https://www.nhis.or.kr/nhis/etc/personalLoginPage.do")
  time.sleep(2)
  input_elements = driver.find_elements(By.TAG_NAME, "input")
  hidden_elements = [element for element in input_elements if element.get_attribute("type") == "hidden"]

  hidden_data = {
    "logintype":"",
    "idn":"",
    "signedMsg":"",
    "vidMsg":"",
    "burl":"",
    "site":"",
    "plain":"",
    "userIdForAuth":"",
    "ci":"",
    "reqTxId":"",
    "hidfrmId":"",
    "seedKey_trxTbwbla01VO":"",
    "initTime_trxTbwbla01VO":"",
    "keyIndex_juminNo2_trxTbwbla01VO":"",
    "keyboardType_juminNo2_trxTbwbla01VO":"",
    "fieldType_juminNo2_trxTbwbla01VO":"",
    "transkeyUuid_trxTbwbla01VO":"",
    "transkey_juminNo2_trxTbwbla01VO":"",
    "transkey_HM_juminNo2_trxTbwbla01VO":"",
    "Tk_juminNo2_checkbox_value_trxTbwbla01VO":""
    }
  for element in hidden_elements:
    if str(element.get_attribute('name')) in hidden_data.keys():
      hidden_data[element.get_attribute('name')]=element.get_attribute('value')
  cookies=driver.get_cookies()
  driver.quit()
  return hidden_data,cookies