from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.seoul_matzip

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/matzip', methods=["GET"])
def get_matzip():
    gu_receive = request.args.get('gu_give')
    matzip_list = list(db.matzip.find({'gu': gu_receive}, {'_id': False}))
    return jsonify({'result': 'success', 'matzip_list': matzip_list})

if __name__ == '__main__':
    app.run('0.0.0.0',port=5000,debug=True)