from .requestsHandler import Response
def getToken(data):
  try:
    issue_token_url = "https://www.nhis.or.kr/oacx/issue_token.jsp"
    commonHeaders = {
                      "Accept": "application/json; charset=utf-8",
                      "User-Agent":
                        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4.1 Safari/605.1.15",
                      "Content-Type": "application/json; charset=utf-8",
                    };
    customBody = { "token": "" };
    response=Response(issue_token_url,commonHeaders,customBody,"POST")
    
    return response.text
  except Exception as e:
    raise Exception("issue token request error", e)