from .jsonConverter import jsonConverter
from .getHidden import getHiddenData
from .requestsHandler import Response
def login(sendAuth_data,auth_data):
  login_url = "https://www.nhis.or.kr/nhis/etc/personalSimpleLogin.do"
  common_header = {
                      "Host": "www.nhis.or.kr",
                      "Accept":
                        "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                      "Sec-Fetch-Site": "same-origin",
                      "Accept-Language": "ko-KR,ko;q=0.9",
                      "Accept-Encoding": "gzip, deflate, br",
                      "Sec-Fetch-Mode": "navigate",
                      "Content-Type": "application/x-www-form-urlencoded",
                      "Origin": "https://www.nhis.or.kr",
                      "Referer": "https://www.nhis.or.kr/nhis/etc/personalLoginPage.do",
                      "Sec-Fetch-Dest": "document",
                      "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4.1 Safari/605.1.15 axios/0.21.1",
                      "Cookies": "JSESSIONID=ODWmr5zmiqXJFnld12zladLP032NUGgB82wyPWY61ALDyPOWcR_U!1138526054; XTVID=A2408090020031947; xloc=2304X1296; bgColorIndex=0; fontColorIndex=0; fontSize=; voiceSpeed=3; voiceStart=stop; voiceStartX=stop; voiceVolum=3; zoomVal=100; JSESSIONID_NHIS_WWW=hl6mr5WRFF2ALJJ9rDvwwc9jFWP_QzaBmSssvc2ThPIfh7STlhJS!728328674; locale=ko; WMONID=NDSUu1r3ZMn"
                    };
  hiddenData = getHiddenData()
  hiddenData["reqTxId"] = sendAuth_data["userInfoEditer"]
  hiddenData["res"] = auth_data
  res = Response(login_url,common_header,hiddenData,"POST")
  # ssotoken이 set-Cookie에 없음
  return res.headers