from microsoftbotframework import ReplyToActivity

djn_reply = "ㅇㅇ"

def echo_response(message):
    if message["type"] == "message":
        ReplyToActivity(fill=message,
                        text=message["text"]).send()

def djn_response(message):
    if message["type"] == "message":
        ReplyToActivity(fill=message, text=djn_reply).send()
        
def djn_echo(message):
    if message["type"] == "message":
        ReplyToActivity(fill=message, text=message["text"]+djn_reply+"...").send()
        