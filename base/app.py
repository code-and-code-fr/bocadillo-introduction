"""Application definition."""
from bocadillo import App, Templates, static

import socketio


app = App()
templates = Templates()

sio = socketio.AsyncServer(async_mode="asgi")
app.mount("/sio", socketio.ASGIApp(sio))
app.mount("/socket.io", static("node_modules/socket.io-client/dist"))


@app.route("/")
async def index(request, response):
    response.html = await templates.render("index.html")


@sio.on("message")
async def broadcast(sid, data: str):
    print("message:", data)
    await sio.emit("response", data)
