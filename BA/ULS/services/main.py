from flask import Flask, make_response, jsonify
from flask_sqlalchemy import SQLAlchemy
from config import Config
from sqlalchemy.exc import OperationalError

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)


class FactoryLog(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    workshopNumber = db.Column(db.Integer)
    resource = db.Column(db.String(255))
    activityName = db.Column(db.String(255))
    transactional_info = db.Column(db.String(255))
    ts = db.Column(db.TIMESTAMP)


@app.route('/')
def hw():
    try:
        avg_service_time = 0
        completed_activities = 0
        activities = FactoryLog.query.filter_by(workshopNumber=Config.WORKSHOP_NUM)\
            .with_entities(FactoryLog.activityName).distinct().all()
        for act in activities:
            all_transactions = FactoryLog.query.\
                filter_by(workshopNumber=Config.WORKSHOP_NUM, activityName=act.activityName).all()
            start, end = 0, 0
            for trans in all_transactions:
                if trans.transactional_info == "start":
                    start = trans.ts
                if trans.transactional_info == "end":
                    end = trans.ts
            if start != 0 and end != 0:
                avg_service_time += (end - start).total_seconds() / 3600  # Total Hours
                completed_activities += 1
        try:
            avg_service_time = avg_service_time / completed_activities
        except ZeroDivisionError:
            avg_service_time = 0
        return make_response(jsonify({'AverageServiceTime': avg_service_time}), 200)
    except OperationalError:
        return make_response(jsonify({'ErrorDescription': 'Database is offline'}), 500)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
