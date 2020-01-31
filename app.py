# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 23:38:52 2020

@author: Citrus
"""
from flask import Flask, request, abort
import os

from Checker import Receipt_Numbers
from Utilities_Functions import filter_inputs, parse_results

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi(os.environ['Channel_Access_Token'])
handler = WebhookHandler(os.environ['Channel_Secret'])

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = TextSendMessage(text='Hello, world')
    line_bot_api.reply_message(event.reply_token, message)