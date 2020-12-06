from flask import Flask,request,abort
from linebot import(LineBotApi,WebhookHandler)
from linebot.exceptions import(InvalidSignatureError)
from linebot.models import(MessageEvent,TextMessage,TextSendMessage)


app=Flask(__name__)

ACCESS_TOKEN = "/qpqZBhWUEmB1pyOT9pvqMsNaJnTzDc2RF9SXzl2PckRRONWt/PViT9RC8+mVQlYcTCd33zjcKv7QCGD4LCOH64p0QQ7FhAQXMgHKB1O/TaxzMPeiY0h4NeRdhEPU0anNjfHs1pteYicz7m/1wSwqAdB04t89/1O/w1cDnyilFU="
SECRET = "5668269638be4261988bd1092008c514"


line_bot_api=LineBotApi(ACCESS_TOKEN)
handler=WebhookHandler(SECRET)

@app.route("/callback",methods=['POST'])
def callback():
    signature=request.headers['X-Line-Signature']
    body=request.get_data(as_text=True)
    app.logger.info("Requestbody:"+body)
    try:
        handler.handle(body,signature)
    except InvalidSignatureError:
        abort(400)
        
    return'OK'
    
@handler.add(MessageEvent,message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))

if __name__=='__main__':
    app.run()
    
