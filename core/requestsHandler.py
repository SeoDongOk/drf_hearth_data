import requests

def Response(url,header,body,type):
  try:
    if type == "GET":
      response=requests.get()
      return response
    elif type == "POST":
      response=requests.post(url=url,headers=header,data=body)
      print(f"request error in {url}, header: {header}, body: {body}")
      return response
  except Exception as e:
    raise Exception(f"request error in {url}, header: {header}, body: {body} \n\n\n with ", e)