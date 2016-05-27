from flask import Flask, render_template, request, redirect, url_for
from db_admin import query_mongo as db
app = Flask(__name__)


@app.route("/")
@app.route("/index")
def load_home_page():
    return render_template('index.html')


# route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if (request.form['username'] != 'admin' or
                request.form['password'] != 'admin'):
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('login_page.html', error=error)


# route for handling the menu page logic
@app.route('/menu', methods=['GET', 'POST'])
def show_menu():
    error = None
    data = db.get_menu()
    return render_template('menu.html', error=error, menu=data)


@app.route('/admin', methods=['GET', 'POST'])
def admin():
    error = None
    payload = {"dish": request.args.get('dish'),
               "category": request.args.get('category'),
               "description": request.args.get('description'),
               "price": request.args.get('price')}
    li = ["", "None", "null"]
    if not(payload['dish'] in li):
        db.insert_data(payload)
    return render_template('admin.html', error=error)

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=8080, debug=True)
