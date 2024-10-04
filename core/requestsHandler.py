import requests

def Response(url,header,body,type):
  try:
    if type == "GET":
      response=requests.get()
      return response
    elif type == "POST":
      if "personalSimpleLogin.do" in url:
        response = requests.post(url, headers=header, data=body, allow_redirects=False)
        r = requests.get('https://www.nhis.or.kr/nhis/index.do', cookies=dict(response.cookies),headers={'user-agent':'Mozilla/5.0'})
        return r
      response=requests.post(url=url,headers=header,data=body)
      return response
  except Exception as e:
    raise Exception(f"request error in {url} \n\n\n header: {header} \n\n\n body: {body} \n\n\n with ", e)