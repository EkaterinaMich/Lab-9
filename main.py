from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask('Step tracker')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///steps.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class StepRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(50))
    steps = db.Column(db.Integer)

    def __repr__(self):
        return f'Record{self.id}. {self.date} - {self.steps} steps.'

@app.route('/')
def main():
    records = StepRecord.query.all()
    # Считаем суммарное количество шагов
    total_steps = sum(record.steps for record in records)
    return render_template('index.html', records_list=records, total=total_steps)

@app.route('/add', methods=['POST'])
def add_record():
    data = request.json
    record = StepRecord(date=data['date'], steps=int(data['steps']))
    db.session.add(record)
    db.session.commit()
    return 'OK'

@app.route('/clear', methods=['POST'])
def clear_records():
    # Удаляем все записи из таблицы
    StepRecord.query.delete()
    db.session.commit()
    return 'OK'

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)