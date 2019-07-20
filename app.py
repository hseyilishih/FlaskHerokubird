# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 01:00:17 2018

@author: linzino
"""


from flask import Flask, request, abort

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

#要改這三個
#token(line_bot_api)
#token e3YZCdHcbbPd3fe+2igbNDXcq8a43JUUg1yBCdsnAFiI1owa+RDsSLxspQwIYTtbdiQazOdCpkwwJdItLCdVe/afn5J72DdHMSFt1mfA5ogWYvXpxBn6/m0jjgJe4fZkOqRH3A+QWuOukfejEK6gGQdB04t89/1O/w1cDnyilFU=
#secret webhookhandler
# 7a89e39c4866c1404b826a0b0356fc1d
#Your user ID (line_bot_api.push_message)  U47fabe554720f74767f786fa537962f8


line_bot_api = LineBotApi('e3YZCdHcbbPd3fe+2igbNDXcq8a43JUUg1yBCdsnAFiI1owa+RDsSLxspQwIYTtbdiQazOdCpkwwJdItLCdVe/afn5J72DdHMSFt1mfA5ogWYvXpxBn6/m0jjgJe4fZkOqRH3A+QWuOukfejEK6gGQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('7a89e39c4866c1404b826a0b0356fc1d')

line_bot_api.push_message('U47fabe554720f74767f786fa537962f8', TextSendMessage(text='Hello World!'))

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


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))
 

print('juhuhu')

if __name__ == '__main__':
    app.run(debug=True)

