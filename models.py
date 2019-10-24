from app import db

class Employee(db.Model):
    __tablename__ = 'Employee'

    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(64))
    middleName = db.Column(db.String(64))
    lastName = db.Column(db.String(64))
    allowance = db.Column(db.Integer)
    hourlyRate = db.Column(db.Float)
    hoursWorked = db.Column(db.Float)
    
    def __repr__(self):
        return '<Employee %r %r>' % (self.firstName, self.lastName) 
