
import base64
import json
def userIpnutEncoder(data):    
  try:
    ascii_name=base64.b64encode(str(data["name"]).encode('UTF-8'))
    encode_name = ascii_name.decode('ascii')
    ascii_birthday=base64.b64encode(str(data["birth_date"]).encode('UTF-8'))
    encode_birthday = ascii_birthday.decode('ascii')
    ascii_phone_number=base64.b64encode(str(data["phone_number"]).encode('UTF-8'))
    encode_phone_number = ascii_phone_number.decode('ascii')
    print("base64 encode is done!")
  except:
    raise Exception("no Elements for base64")