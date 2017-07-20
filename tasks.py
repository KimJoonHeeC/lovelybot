from microsoftbotframework import ReplyToActivity
import requests
import json
from datetime import datetime


# https://api.korbit.co.kr/v1/ticker

def echo_response(message):
    print(message)

    if message["type"] == "message":
        #if "bitcoin" in message["text"] or "비트코인" in message["text"]:
        if "bitcoin" or "비트코인" or "ethereum" or "이더리움" in message["text"]:
            r_bit = requests.get("https://api.korbit.co.kr/v1/ticker?currency_pair=btc_krw")
            r_etc = requests.get("https://api.korbit.co.kr/v1/ticker?currency_pair=etc_krw")
            r_eth = requests.get("https://api.korbit.co.kr/v1/ticker?currency_pair=eth_krw")
            bitcoin_price = r_bit.json()["last"]
            eclassic_price = r_etc.json()["last"]
            ethe_price = r_eth.json()["last"]
            current_time = datetime.fromtimestamp(r_bit.json()['timestamp'] / 1000).strftime('%Y-%m-%d %H:%M:%S')
            msg = "at %s, \nbitcoin price is %s won. " \
                  "\nethereum classic price is %s won. \nethereum price is %s won." \
                  % (current_time, bitcoin_price, eclassic_price, ethe_price)
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