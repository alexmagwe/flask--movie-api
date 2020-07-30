from . import db
class Movies(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(20),index=True)
    rating=db.Column(db.Integer,index=True)
    def __repr__(self):
        return f"{self.title},{self.rating}" 



