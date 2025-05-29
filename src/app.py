from flask import Flask, jsonify
import datetime
import socket

ip = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

app = Flask(__name__)

@app.route('/api/v1/details')

def details():
    return jsonify({
        'time': datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y"),
        'hostname': socket.gethostname(),
        'message': 'Deployed on K8s cluster!'
    })

@app.route('/api/v1/healthz')

def health():
    return jsonify({'status': 'up'}), 200

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)
    try:
        # doesn't even have to be reachable
        s.connect(('10.254.254.254', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

if __name__ == '__main__':

    app.run(host="0.0.0.0")
