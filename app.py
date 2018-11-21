from flask import Flask, render_template
from flask_pymongo import PyMongo
import db, reportService

app = Flask(__name__)

app.config['MONGO_URI'] = db.get_db() #'mongodb://localhost:27017/chazkiv2'

mongo = PyMongo(app)

@app.route('/')
def home():
    users = mongo.db.user.find({})#db._collection('storage')
    return render_template("index.html", users=users)

@app.route('/report/crossdocking')
def crossdocking():
    storage = reportService.crossdocking(mongo, 'crossdocking')
    return render_template("index.html", storage=storage)#reportService.crossdocking(mongo, 'crossdocking')

if __name__ == '__main__':
    app.run(debug=True) # pepito