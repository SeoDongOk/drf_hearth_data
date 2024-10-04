from urllib import parse
from .getHidden import getHiddenData
from .requestsHandler import Response
def login(sendAuth_data,auth_data):
  login_url = "https://www.nhis.or.kr/nhis/etc/personalSimpleLogin.do"
  hiddenData,cookies = getHiddenData()
  hiddenData["reqTxId"] = sendAuth_data["txId"]
  hiddenData["res"] = auth_data
  cookie_str = '; '.join([f"{cookie['name']}={cookie['value']}" for cookie in cookies])
  common_header = {
    "User-Agent":"Mozilla/5.0",
    "Referer": "https://www.nhis.or.kr/nhis/etc/personalLoginPage.do",
    "content-type": "application/x-www-form-urlencoded",
    "Cookie":cookie_str
  }
  
  res = Response(login_url,common_header,parse.urlencode(hiddenData),"POST")
  print(res)
  # ssotoken이 set-Cookie에 없음
  return res.text