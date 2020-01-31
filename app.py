# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 23:38:52 2020

@author: Citrus
"""
from flask import Flask, request, abort
import os

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, ImageSendMessage
)

app = Flask(__name__)

line_bot_api = LineBotApi(os.environ['Channel_Access_Token'])
handler = WebhookHandler(os.environ['Channel_Secret'])

#@handler.add(MessageEvent, message=TextMessage)
#def handle_message(event):
#    message = TextSendMessage(text='Hello, world')
#    line_bot_api.reply_message(event.reply_token, message)

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = {
            "type": "sticker",
            "packageId": "1",
            "stickerId": "1"
}
line_bot_api.reply_message(event.reply_token, message)
    
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

if __name__ == "__main__":
    app.run()