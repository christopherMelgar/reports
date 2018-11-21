import datetime

def crossdocking(mongo, params):
    findfilters = {
        'log.date': {
            '$gte': datetime.datetime.strptime(params['dateFrom'], "%Y-%m-%d"),#datetime.datetime(2018,1,24),
            '$lt': datetime.datetime.strptime(params['dateTo'], "%Y-%m-%d")#datetime.datetime(2018,1,25)
        },
        'removed': False
    }
    return list(mongo.db.storage.find(findfilters))