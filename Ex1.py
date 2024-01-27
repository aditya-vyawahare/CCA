from flask import Flask, request, jsonify

app=Flask(__name__)

num=0
@app.route('/',methods=['GET','POST'])
def user():
    global num
    if request.method=='POST':
        num=request.get_json('num')['num']
        return jsonify({"num": num})
    
    if request.method=='GET':
        return str(num)

app.run(host='0.0.0.0', port=5000)