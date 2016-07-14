from channels.routing import route
from push.consumers import ws_receive, ws_connected, ws_disconnect

# channel_routing = [
#     route("http.request", "push.consumers.http_consumer"),
# ]

channel_routing = [
    route("websocket.connect", ws_connected),
    route("websocket.receive", ws_receive),
    route("websocket.disconnect", ws_disconnect),
]
