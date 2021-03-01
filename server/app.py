from server import create_app
from server import socketio
from server.models.user import User

if __name__ == '__main__':

    app=create_app()

    socketio.run(app=app,host='0.0.0.0',threaded=True)

