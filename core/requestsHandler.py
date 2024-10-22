import requests

def Response(url,header,body,type):
  try:
    if type == "GET":
      response=requests.get()
      return response
    elif type == "POST":
      if "personalSimpleLogin.do" in url:
        response = requests.post(url, headers=header, data=body, allow_redirects=False)
        # 2023년 건강보험 연말정산내역 조회
        r=requests.post("https://www.nhis.or.kr/nhis/minwon/retrieveIndiYetaList.do",data="jungNo=&corrYear=2022", cookies=dict(response.cookies),headers={'user-agent':'Mozilla/5.0'}) 
        return r
      response=requests.post(url=url,headers=header,data=body)
      return response
  except Exception as e:
    raise Exception(f"request error in {url} \n\n\n header: {header} \n\n\n body: {body} \n\n\n with ", e)