from app import db


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    description = db.Column(db.String) #why dont we specify the type here?
    
    def to_string(self):
        return f"{self.id}: {self.title} Description: {self.description}"
    
    