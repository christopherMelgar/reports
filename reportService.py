import moment
import datetime

def crossdocking(mongo, params):
    findfilters = {
        'log.date': {
            '$gte': datetime.datetime(2018,1,24,21,34,54),
            '$lt': datetime.datetime(2018,1,25,21,34,54)
        }
    }
    storage = mongo.db.storage.find(findfilters)
    return storage