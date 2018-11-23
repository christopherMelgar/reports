from flask import Flask, render_template, request, jsonify, json
from flask_pymongo import PyMongo
import db
import reportService
import numpy as np

app = Flask(__name__)

app.config['MONGO_URI'] = db.get_db()#'mongodb://localhost:27017/chazkiv2'

mongo = PyMongo(app)


@app.route('/')
def home():
    users = mongo.db.user.find({})#db._collection('storage')
    return render_template("index.html", users=users)


@app.route('/crossdocking')
def crossdocking():
    date_from = request.args.get('dateFrom', '')
    date_to = request.args.get('dateTo', '')
    storage = reportService.crossdocking(mongo, date_from, date_to)

    return jsonify(storage)


if __name__ == '__main__':
    app.run(debug=True) # pepito