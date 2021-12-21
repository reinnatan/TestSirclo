from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class BeratBadanModel(db.Model):
    __tablename__ = "BeratBadan"

    id = db.Column(db.Integer, primary_key=True)
    tanggal = db.Column(db.Date())
    max = db.Column(db.Integer())
    min = db.Column(db.Integer())
    perbedaan = db.Column(db.Integer)

    def __init__(self,  tanggal, max, min, perbedaan):
        self.tanggal = tanggal
        self.max = max
        self.min = min
        self.perbedaan = perbedaan