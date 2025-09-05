from flask import Flask, request, jsonify

app = Flask(__name__)
todos = []

@app.route('/')
def home():
    return "✅ Welcome to ALLLL!!!! Todo List App again post updation in html page! Use /add?task=TaskName and /list."

@app.route('/add')
def add_task():
    task = request.args.get("task")
    if task:
        todos.append(task)
        return f"Task '{task}' added!"
    return "No task provided."

@app.route('/list')
def list_tasks():
    return jsonify(todos)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
