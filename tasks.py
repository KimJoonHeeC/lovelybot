from microsoftbotframework import ReplyToActivity
import requests
import json
from datetime import datetime


# https://api.korbit.co.kr/v1/ticker

def echo_response(message):
    print(message)

    if message["type"] == "message":
        if "bitcoin" in message["text"] or "비트코인" in message["text"]:
            r = requests.get("https://api.korbit.co.kr/v1/ticker")
            bitcoin_price = r.json()["last"]
            current_time = datetime.fromtimestamp(r.json()['timestamp'] / 1000).strftime('%Y-%m-%d %H:%M:%S')
            msg = "bitcoin price is %s at %s" % (bitcoin_price, current_time)
            print(msg)
            ReplyToActivity(fill=message, text=msg).send()

        elif "ㅇㅇ" in message["text"]:
            djn_reply = "그래그래 ㅇㅇ"
            ReplyToActivity(fill=message, text=djn_reply).send()

        elif "ㅠㅠ" in message["text"] or "ㅜㅜ" in message["text"]:
            yor_reply = "우쮸쮸쮸 ㅇㅇ..."
            ReplyToActivity(fill=message, text=yor_reply).send()

        else:
            data = {
                "documents": [{"language": "en", "id": "1", "text": message["text"]}]
            }
            headers = {'Ocp-Apim-Subscription-Key': '4cfe6f744f1b486db3fa83d874bafdd9',
                       'Content-Type': 'application/json',
                       'Accept': 'application/json',
                       }

            r = requests.post("https://westus.api.cognitive.microsoft.com/text/analytics/v2.0/sentiment",
                              data=json.dumps(data), headers=headers)
            emo_score = r.json()["documents"][0]["score"]
            msg = "emotion score is %s\n" % emo_score

            if emo_score > 0.5:
                msg = msg + "\nYou look happy!"

            elif emo_score == 0.5:
                msg = msg + "\nI'm not sure how you feel."

            else:
                msg = msg + "\nYou look unhappy.."

            print(msg)
            ReplyToActivity(fill=message, text=msg).send()