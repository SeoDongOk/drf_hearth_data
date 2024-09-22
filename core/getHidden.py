import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def getHiddenData():
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

  hidden_data = {"juminNo1":None, 
                 "juminNo2":None,
                 "hidfrmId":"",
                 "seedKey_trxTbwbla01VO":"",
                 "initTime_trxTbwbla01VO":"",
                 "keyIndex_juminNo2_trxTbwbla01VO":"",
                 "keyboardType_juminNo2_trxTbwbla01VO":"",
                 "fieldType_juminNo2_trxTbwbla01VO":"",
                 "transkeyUuid_trxTbwbla01VO":"",
                 "transkey_juminNo2_trxTbwbla01VO":"",
                 "transkey_HM_juminNo2_trxTbwbla01VO":"",
                 "Tk_juminNo2_checkbox_value_trxTbwbla01VO":""}
  for element in hidden_elements:
    if str(element.get_attribute('name')) in hidden_data.keys():
      hidden_data[element.get_attribute('name')]=element.get_attribute('value')

  driver.quit()
  return hidden_data