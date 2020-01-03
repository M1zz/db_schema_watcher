import requests, json


def send_message():
    url = "https://wh.jandi.com/connect-api/webhook/12835000/6ce9d437323d752bf11f7bf27cc5c653"
    headers = {"Accept": "application/vnd.tosslab.jandi-v2+json",
               "Content-Type": "application/json"}
    body = ""

    r = open("diff.txt", 'r')
    for line in r:
        body = body + (str(line))

    data = {
        "body": str(body),
        "connectColor": "FFFFFFF",
        "connectInfo": [{
            "title": "기타 문의",
            "description": "이현호 프로에게 문의 부탁드립니"
        }]}

    r = requests.post(url, headers=headers, data=json.dumps(data))

    return r.status_code
