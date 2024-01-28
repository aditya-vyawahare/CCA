from flask import Flask,request, jsonify
from subprocess import Popen
import socket

app = Flask(__name__)

def run_script():
    try:
        Popen(['python3','stress_cpu.py'])
    except:
        print('Error coudnt run stress_cpu.py')

@app.route('/',methods=['GET','POST'])
def user():
    if request.method=='POST':
        run_script()
        return ''
    if request.method=='GET':
        return str(socket.gethostbyname(socket.gethostname()))
    
app.run(host='0.0.0.0', port=5000)
