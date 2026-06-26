# app.py
from flask import Flask, jsonify, render_template
from datetime import datetime

app = Flask(__name__)

# 仮のデータ（後でデータベースに置き換えてもOK）
tasks = [
    {"id": 1, "title": "Gitの演習をする", "done": False},
    {"id": 2, "title": "Flaskを復習する", "done": True},
]

# 画面（HTML）を返すルート
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/tasks", methods=["GET"])
def get_tasks():
    now = datetime.now()
    generated_at = now.strftime("%Y-%m-%d %H:%M:%S")

    total_count = len(tasks)
    done_count = len([t for t in tasks if t["done"]])

    return jsonify({
        "generated_at": generated_at,
        "total_count": total_count,
        "done_count": done_count,
        "tasks": tasks
    })
    pass


if __name__ == "__main__":
    app.run(debug=True, port=5001)
