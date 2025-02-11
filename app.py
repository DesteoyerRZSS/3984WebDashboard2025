from flask import Flask, render_template
from flask_socketio import SocketIO
from networktables import NetworkTables

# Connect to NetworkTables
NetworkTables.initialize(server='roborio-XXXX-frc.local')  # Change XXXX to your team number
table = NetworkTables.getTable("SmartDashboard")

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')  # Serves HTML UI

@socketio.on('get_data')
def send_data():
    data = {
        'robot_battery': table.getNumber('BatteryVoltage', 0),
        'robot_speed': table.getNumber('Speed', 0)
    }
    socketio.emit('update_data', data)  # Sends data to frontend

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=3984, debug=True)