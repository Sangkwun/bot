from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def welcome():
    if request.method == 'GET':
        response = {
            "type" : "text",
            "content" : "원하는 사진을 보내주세요!"
        }
        return jsonify(response)
    elif request.method == 'POST':
        response = {
            "type" : "text",
            "content" : "10점!"
        }
        return jsonify(response)

@app.route('/keyboard', methods=['GET'])
def keyboard():
    msg = "사진을 보내주세요."
    response = {
            "type" : "text",
            "message":{
                    "text" : msg
                }
        }
    return jsonify(response)

@app.route('/message', methods=['POST'])
def message():
    print(request.json)

    if request.json['type'] == 'photo':
        msg = "신난당!"

    else:
        msg = "사진을 보내주세요~"

    response = {
                "message":{
                    "text" : msg
                }
            }
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0')