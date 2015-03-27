import serial
import myserial.dummy_serial as dummy_serial
from myserial.ports import serial_ports


def get_serial(port, use_real=True):
    if port is None:
        ports = serial_ports()
        port = ports[0] if len(ports) > 0 else 'whatever'
    return serial.Serial(port) if use_real else dummy_serial.Serial(port=port,timeout=60)