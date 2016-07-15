from django.http import HttpResponse
from channels.handler import AsgiHandler
from channels import Group
import time


# def ws_message(message):
#     # ASGI WebSocket packet-received and send-packet message types
#     # both have a "text" key for their textual data.
#     message.reply_channel.send({
#         "text": message.content['text'],
#     })


def ws_connected(message):
    Group("chat").add(message.reply_channel)


def ws_receive(message):
    for i in range(20):
        Group("chat").send({
            "text": "[user] %s " % i
        })


def ws_disconnect(message):
    Group("chat").discard(message.reply_channel)
