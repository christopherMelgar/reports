def get_db():
    connection = 'mongodb://localhost:27017/chazkiv2'#mongodb://${auth}${dbConfig.host}:${dbConfig.port}/${dbConfig.name}
    return connection

def _collection(name):
    db = get_db()
    return db.getCollection(name)