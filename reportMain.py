import reportService as pepito


class Report:
    def conexion(self):
        pass

class MongoConexion(Report):

    def __init__(self, mongo):
        self.mongo = mongo

    def conexion(self):
        return self.mongo


class Crossdocking:

    def __init__(self, date_from, date_to):
        self.date_from = date_from
        self.date_to = date_to

    def cross(self, mongo):
        return pepito.crossdocking(mongo, self.date_from, self.date_to)