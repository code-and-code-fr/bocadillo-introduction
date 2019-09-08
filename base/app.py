"""Application definition."""
from bocadillo import App, configure, Templates

import socketio


app = App()
configure(app)
templates = Templates()

sio = socketio.AsyncServer(async_mode="asgi")
app.mount("/sio", socketio.ASGIApp(sio))


@app.route("/")
async def index(req, res):
    res.html = await templates.render("index.html")
