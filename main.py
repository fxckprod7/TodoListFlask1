from flask import Flask, render_template, request, redirect

from db_controller import Database

app = Flask(__name__)

Database = Database("todo.db")


# Custom 404 error handler
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


@app.route('/create_task', methods=['POST', 'GET'])
def create_task():
    if request.method == 'POST':
        title = request.form.get("title")
        description = request.form.get("description")

        Database.create_task(title, description)

        return redirect('/')
    else:
        return redirect('/404')


@app.route('/ready', methods=['POST', 'GET'])
def ready_task():
    if request.method == 'POST':
        task_id = int(request.form.get("task_id"))
        Database.delete_task(task_id)
        return redirect('/')
    else:
        return redirect('/404')


@app.route('/submit_feedback', methods=['POST', 'GET'])
def submit_feedback():
    if request.method == 'POST':
        # TODO: Create feedback to mail
        return render_template("submit_feedback.html")
    else:
        return redirect('/404')


@app.route('/')
def index():
    tasks = Database.get_tasks()
    return render_template("index.html", tasks=tasks)


@app.route('/feedback')
def feedback():
    return render_template('feedback.html')


if __name__ == "__main__":
    app.run(debug=True, port=5000)
