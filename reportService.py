import datetime

def crossdocking(mongo, date_from, date_to):
    findfilters = {
        'log.date': {
            '$gte': datetime.datetime.strptime(date_from, "%Y-%m-%d"),
            '$lt': datetime.datetime.strptime(date_to, "%Y-%m-%d")
        },
        'removed': False
    }
    storage = list(mongo.db.storage.find(findfilters))
    res = []
    for idx, store in enumerate(storage):
        len_log = len(store['log'])
        shipment_storage = {
            'tracking': store['tracking'],
            'dateFirst': store['log'][0]['date'],
            'flowFirst': store['log'][0]['flow'],
            'dateLast': store['log'][len_log - 1]['date'],
            'flowLast': store['log'][len_log - 1]['flow']
        }
        res.insert(idx, shipment_storage)

    return res