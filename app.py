from flask import Flask, render_template
from flask_socketio import SocketIO

from random import randint
import time

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

def update_data():
    while True:
        # Data 
        data = []

        for i in range(5):
            data.append(str(randint(0,10)))

        # Send data as message to js
        socketio.emit('data update', {'data': data}, namespace='/')
        time.sleep(2)

if __name__ == '__main__':
    socketio.start_background_task(update_data)
    socketio.run(app, debug=True)
