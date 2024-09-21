
import time
from .requestsHandler import Response
from .jsonConverter import jsonConverter
from .settings import userInfoEditer, contentInfo, providerOptionInfo,deviceInfo
def authChecker(data):
  try:
    authCheckUrl = "https://www.nhis.or.kr/oacx/api/v1.0/authen/result";
    commonHeaders = {
                        "Accept": "application/json; charset=utf-8",
                        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4.1 Safari/605.1.15",
                        "Cookie":"JSESSIONID=uXvc3QjJA-D56m9HGvpzE86OFHatEff21kA1VYgiLqMgoMm8uS-M!1241807923; WMONID=jZ5g3-x7usf",
                        "Content-Type": "application/json; charset=utf-8",
                      };
    authCheckBody = {
      "providerId": "banksalad",
      "providerName": "뱅크샐러드",
      "deeplinkUri": "",
      "naverAppSchemeUrl": "",
      "telcoTxid": "",
      "mdlAppHash": "",
      "id": "",
      "provider": "banksalad_v1.5",
      "token":data["token"],
      "txId":data["txId"],
      "cxId":data["cxId"],
      "appInfo": { "code": "", "path": "", "type": "" },
      "userInfo":data["userInfoEditer"],
      "deviceInfo":deviceInfo,
      "contentInfo":contentInfo,
      "providerOptionInfo":providerOptionInfo,
      "compareCI": False,
      "useMdlSsn": False,
    };
    startTime = time.time()
    while True:
      if int(time.time()-startTime) > 20:
        break
      time.sleep(2)
      print("time: ", time.time())
      res=Response(authCheckUrl,commonHeaders,jsonConverter(authCheckBody,"json"),"POST")
      if "성공" in str(res.text):
        return res.text
  except Exception as e:
    raise Exception("Error on authChecker: ",e)
