import time
from .requestsHandler import Response
from .jsonConverter import jsonConverter
from .encoder import userIpnutEncoder
from .settings import userInfoEditer, contentInfo, providerOptionInfo,deviceInfo

def sendAUTH(userInput,issue_data):
  encode_userInput = userIpnutEncoder(userInput)
  auth_url = "https://www.nhis.or.kr/oacx/api/v1.0/authen/request";
  authBody = {
    "id": "",
    "provider": "banksalad_v1.5",
    "token":issue_data["token"],
    "txId":issue_data["txId"],
    "appInfo": { "code": "", "path": "", "type": "" },
    "userInfo":userInfoEditer(encode_userInput),
    "deviceInfo":deviceInfo,
    "contentInfo":contentInfo,
    "providerOptionInfo" : providerOptionInfo,
    "compareCI": False,
  };
  commonHeaders = {
                      "Accept": "application/json; charset=utf-8",
                      "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4.1 Safari/605.1.15",
                      "Cookie":"JSESSIONID=uXvc3QjJA-D56m9HGvpzE86OFHatEff21kA1VYgiLqMgoMm8uS-M!1241807923; WMONID=jZ5g3-x7usf",
                      "Content-Type": "application/json; charset=utf-8",
                    };
  res=Response(auth_url,commonHeaders,jsonConverter(authBody,"json"),"POST")
  res = jsonConverter(res.text,"dict")
  return {"cxId":res["cxId"], "token":res["token"],  "txId":res["reqTxId"], "userInfoEditer":userInfoEditer(encode_userInput)}