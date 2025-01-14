from flask import Flask, render_template
from flask_socketio import SocketIO
from datetime import datetime

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

def send_time():
    while True:
        socketio.sleep(1)
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        socketio.emit('time', {'time': current_time})

@socketio.on('connect')
def handle_connect():
    socketio.start_background_task(send_time)

if __name__ == '__main__':
    print('Server starting at: http://127.0.0.1:8080')
    socketio.run(app, host='127.0.0.1', port=8080)