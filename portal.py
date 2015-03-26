from flask import Flask
import requests
import motor

SERVER_NAME = '127.0.0.1:5001'

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/pull/<duration>')
def pull(duration):
    url = "http://{0}/pull/{1}".format(motor.SERVER_NAME, duration)
    r = requests.get(url)
    result = r.json()
    return result['status']

if __name__ == '__main__':
    app.run()