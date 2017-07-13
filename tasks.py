from microsoftbotframework import ReplyToActivity

djn_reply = "ㅇㅇ"

def echo_response(message):
    if message["type"] == "message":
        ReplyToActivity(fill=message,
                        text=message["text"]).send()

def djn_response(message):
    if message["type"] == "message":
        ReplyToActivity(fill=djn_reply, text=message["text"]).send()