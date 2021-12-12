import logging
import time
from flask import Flask
from flask import Response
from flask import render_template

app = Flask(
        __name__,
        static_url_path='',
        static_folder='static',
        template_folder='templates'
        )

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/stream')
def stream():
    def event_stream():
        data = 0
        while True:
            time.sleep(1)
            yield f"event: update\ndata: {data}\n\n"
            data += 1
    return Response(event_stream(), mimetype="text/event-stream")


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    app.run('0.0.0.0')

