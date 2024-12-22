import redis
from flask import Flask, request

app = Flask(__name__)
print("Connecting to redis...")
r = redis.Redis(host='localhost', port=6379, db=0)
print("Connected to redis")


@app.route('/health', methods=['GET'])
def health():
    r.ping()
    return "OK", 200


@app.route('/callevent', methods=['POST'])
def callevent():

    print("\nReceived ACS callback")
    body = request.get_json()
    print("Event normal body: ", body)
    body = body[0]
    event_type = body['type']

    print("Event type: ", event_type)
    print("Event data: ", body)
    print("Event callConnectionId: ",  body['data']['callConnectionId'])
    r.set(body['data']['callConnectionId'], "true")

    return "OK", 200


if __name__ == "__main__":
    app.run(port=3000)
