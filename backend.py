from flask import Flask, render_template, request, redirect, url_for
from threading import Thread
from flask_socketio import SocketIO, emit
from fileinput import filename 
from flask import send_from_directory
from networktables import NetworkTables

NetworkTables.initialize(server='roborio-3984-frc.local') 
app = Flask(__name__)
socketio = SocketIO(app)
sd = NetworkTables.getTable('ButtonBoard')
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/update_table', methods=['GET'])
def update_table():
    param1 = request.args.get('🎛️')
    sd.putString('🎛️', param1)
    return render_template('index.html', dataToRender=param1)

if __name__ == '__main__':
    socketio.run(app, debug=False, use_reloader=False, host='0.0.0.0', port='8008')