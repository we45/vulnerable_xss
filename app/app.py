from flask import Flask, request, render_template, redirect
from jinja2 import Environment, FileSystemLoader
from flask_sqlalchemy import SQLAlchemy
import os
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop

app = Flask(__name__, template_folder='templates')
loader = FileSystemLoader( searchpath="templates/")
Jinja2 = Environment(loader=loader, autoescape=False)

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{0}".format(os.path.join(project_dir, "show_content.sqlite"))
app.config['SQLALCHEMY_DATABASE_URI'] = database_file
db = SQLAlchemy(app)
app_port = os.environ.get('APP_PORT', 5060)

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String,nullable=False)

    def __repr__(self):
        return '<Note : id={0}, name={1}'.format(self.id, self.name)


@app.route('/', methods=['GET'])
def home():
    if request.method == 'GET':
        db.create_all()
        note = db.session.query(Note).all()
        if(len(note) > 0):
            output = note
        else:
            output = "Welcome to XSS Lab"
        return render_template('note.html', output=output)

@app.route('/note', methods=['GET', 'POST'])
def create_note():
    if request.method == 'GET':
        db.create_all()
        note = db.session.query(Note).all()
        if(len(note) > 0):
            output = note
        else:
            output = "Welcome to XSS Lab"
        return render_template('note.html', output=output)
    elif request.method == 'POST':
        # name = Jinja2.from_string(request.form['note']).render()
        name = request.form['note']
        page = Note(name=name)
        db.session.add(page)
        db.session.commit()
        note = db.session.query(Note).all()
        if (len(note) > 0):
            output = note
        else:
            output = "Welcome to XSS Lab"
        return render_template('note.html', output=output)
    else:
        output = "Welcome to Server Side Template Injection"
        return render_template('note.html', output=output)

@app.route("/todo", methods=['GET'])
def create_todo():
    return render_template('todo.html')

@app.route("/contact_us", methods=['GET', 'POST'])
def contact_us():
    if request.method == 'GET':
        return render_template('contact.html')
    elif request.method == 'POST':
        email = request.form['email']
        # description = request.form['description']
        return redirect ('/contact?q={0}'.format(email))
    else:
        return render_template('contact.html')

@app.route("/contact", methods=['GET'])
def contact():
    name = request.values.get('q')
    output = '</br> </br> </br> </br> </br> <div style="margin-left:500px;">Dear <strong> {0} </strong> </br> Thank you for submiting your request. </br> We will update soon</div>'.format(name)
    return output

if __name__ == '__main__':
    http_server = HTTPServer(WSGIContainer(app))
    http_server.listen(app_port)
    IOLoop.instance().start()
    # app.run(host = '0.0.0.0', port=5000)
