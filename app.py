from flask import Flask, render_template
import psutil

app = Flask(__name__)


@app.route('/')
def index():
    processes = get_top_processes()
    return render_template('index.html', processes=processes)


def get_top_processes():
    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'memory_info']):
        if proc.info['memory_info'] is not None:
            processes.append(proc.info)
    processes.sort(key=lambda x: x['memory_info'].rss, reverse=True)
    return processes[:10]


if __name__ == "__main__":
    app.run(debug=True)
