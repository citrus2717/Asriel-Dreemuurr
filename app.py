# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 23:38:52 2020

@author: Citrus
"""

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = TextSendMessage(text='Hello, world')
    line_bot_api.reply_message(event.reply_token, message)