from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(512), nullable=False)
    important = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<Note {self.id}: {self.text} (Important: {self.important})>'

@app.route('/')
def index():
    notes = Note.query.all()
    return render_template('index.html', notes=notes)

@app.route('/add_note', methods=['POST'])
def add_note():
    text = request.form['text']
    important = 'important' in request.form
    new_note = Note(text=text, important=important)
    db.session.add(new_note)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/clear_notes', methods=['POST'])
def clear_notes():
    Note.query.delete()
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
