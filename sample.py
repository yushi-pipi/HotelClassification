from flask import Flask,redirect,url_for,request,logging,jsonify
import os

app=Flask(__name__)


@app.route('/')
def index():
    return request.args.get('param','get_test')

@app.route('/hoge')
def hoge():
    app.logger.warn('hoge')
    return 'helloworld_hoge'

@app.route('/hello')
def hello():
    return redirect(url_for('hoge'))

@app.route('/my',methods=['GET'])
def my_route_get():
    return 'get'

@app.route('/my',methods=['POST'])
def my_route_post():
    return 'post'

@app.route('/json')
def json():
    return jsonify(name = 'yushi',email='yushi@example.com')

@app.route("/json",methods=['POST'])
def post_json():
    json_data = request.get_json()
    app.logger.warn(json_data)
    return jsonify(json_data)

if __name__== "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))