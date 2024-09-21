import json

def jsonConverter(data,method):
  try:
    if method == "dict":
      dict_data = json.loads(data)
      return dict_data
    elif method == "json":
      dict_data = json.dumps(data)
      return dict_data
  except Exception as e:
    raise Exception("Error on jsonConverter: ", e)