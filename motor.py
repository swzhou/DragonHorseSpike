from flask import Flask, jsonify
import myserial.serial_wrapper as wrapper

SERVER_NAME = '127.0.0.1:5002'
USE_REAL_SERIAL = False

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/pull/<duration>')
def pull(duration):
    ser = wrapper.get_serial(port=None, use_real=app.config['USE_REAL_SERIAL'])
    message = "pull:{0}".format(duration)
    ser.write(message.encode('utf-8'))
    return jsonify(
        action='pull',
        status='success',
        duration=duration
    )

if __name__ == '__main__':
    app.run()