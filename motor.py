from flask import Flask, jsonify
# from ports import serial_ports
# import serial

SERVER_NAME = '127.0.0.1:5002'

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/pull/<duration>')
def pull(duration):
    # port = serial_ports()[0]
    # ser = serial.Serial(port)
    # message = "pull:{0}".format(duration)
    # ser.write(message)
    return jsonify(
        action='pull',
        status='success',
        duration=duration
    )

if __name__ == '__main__':
    app.run()