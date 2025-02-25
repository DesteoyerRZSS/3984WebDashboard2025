from flask import Flask, render_template_string, request
from flask_socketio import SocketIO
from networktables import NetworkTables
import os
import gevent
import eventlet
import threading
NetworkTables.initialize(server='roborio-3984-frc.local') 
app = Flask(__name__)
#socketio = SocketIO(app, async_mode='threading')
sd = NetworkTables.getTable('ButtonBoard')
@app.route('/')
def home():
    template = '''
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Robot Dashboard</title>
    <style>
        /* From Uiverse.io by btongheng */ 
body{
    background-color: rgb(69, 69, 69);
    color: white;
    position: fixed;
}
.level, .levels{
  --lol: #644dff;
  --lolol: #4836bb;
  --lololol: #654dff63;
  cursor: pointer;
  width: 70%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 1rem;
  font-size: 1.125em;
  font-weight: 800;
  letter-spacing: 3px;
  color: #fff;
  background: var(--lol);
  border: 2px solid var(--lolol);
  border-radius: .75rem;
  box-shadow: 0 8px 0 var(--lolol);
  transform: skew(-10deg);
  transition: all .1s ease;
  filter: drop-shadow(0 15px 20px var(--lololol));
  margin: auto;
  
}

/* .levels{
    padding-bottom: 0;
} */

.level:active {
  letter-spacing: 0px;
  transform: skew(-10deg) translateY(8px);
  box-shadow: 0 0 0 var(--lololol);
}

table{
    margin-top: 0;
    margin:auto;
}


td{
    width: 3%;
    padding-bottom: 5%;
    height: 125px;
    
}

#0{
    width: 100%;
}
    </style>
</head>
<body>

    <table>
        <th></th>
        <tr>
            <td><button id="L3" class="level" style="background-color: red; border-color: maroon; box-shadow: 0 8px 0 maroon; filter: drop-shadow(0 15px 20px maroon)">L3</button></td>
            <td><button id="R3" class="level" style="background-color: red; border-color: maroon; box-shadow: 0 8px 0 maroon; filter: drop-shadow(0 15px 20px maroon)">R3</button></td>
        </tr>
        <tr>
            <td><button id="L2" class="level" style="background-color: orange; border-color: chocolate; box-shadow: 0 8px 0 chocolate; filter: drop-shadow(0 15px 20px chocolate)">L2</button></td>
            <td><button id="R2" class="level" style="background-color: orange; border-color: chocolate; box-shadow: 0 8px 0 chocolate; filter: drop-shadow(0 15px 20px chocolate)">R2</button></td>
        </tr>
        <tr>
            <td><button id="L1" class="level" style="background-color: green; border-color: darkgreen; box-shadow: 0 8px 0 darkgreen; filter: drop-shadow(0 15px 20px darkgreen)">L1</button></td>
            <td><button id="R1" class="level" style="background-color: green; border-color: darkgreen; box-shadow: 0 8px 0 darkgreen; filter: drop-shadow(0 15px 20px darkgreen)">R1</button></td>
        </tr>
        <tr>
            <td colspan="2"><button id="0" class="level">0</button></td>
        </tr>
            
        
    </table>
    


    <script>
        function httpGet(theUrl)
{
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", theUrl, false ); // false for synchronous request
    xmlHttp.send( null );
    return xmlHttp.responseText;
}
        var buttons = document.querySelectorAll('.level');
        buttons.forEach(function(button){
            button.addEventListener('click', function(){
                var level = this.id;
                var response = httpGet('http://localhost:8008/level?cumber=' + level);
                console.log(response);
            });
        });
    </script>
</body>
</html>
    '''
    return render_template_string(template, name='Robot Dashboard')

@app.route('/level', methods=['GET'])
def update_table():
    param1 = request.args.get('cumber')
    sd.putString('cumber', param1)
    print(param1)
    return "recieved " + param1

if __name__ == '__main__':
    os.system("start chrome \"http://localhost:8008\"")
    app.run(host='0.0.0.0',port='8008')
    #socketio.run(app, debug=False, use_reloader=False, host='0.0.0.0', port='8008')
    #os.system("start chrome \"http://0.0.0.0:8008\"")
