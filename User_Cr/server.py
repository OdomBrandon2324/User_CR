from flask import Flask, render_template, request, redirect


from users import User

app = Flask(__name__)


@app.route('/')
def index():
    return redirect('/users')


@app.route('/users')
def users():
    users = User.get_all()
    return render_template('users.html', user=users)


@app.route('/user/new')
def new_user():
    return render_template("new_user.html")


@app.route('/user/create', methods=['POST'])
def create():
    print(request.form)
    User.save(request.form)
    return redirect('/users')


@app.route('/user/edit/<int:id>')
def edit(id):
    data = {
        "id": id
    }
    return render_template("edit_user.html", user=User.get_one(data))


@app.route('/user/show/<int:id>')
def show(id):
    data = {
        "id": id
    }
    return render_template("show_user.html", user=User.get_one(data))


@app.route('/user/update', methods=['POST'])
def update():
    User.update(request.form)
    user_id=request.form["id"]
    return redirect(f'/user/show/{user_id}')


@app.route('/user/destroy/<int:id>')
def destroy(id):
    User.destroy(id)
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
