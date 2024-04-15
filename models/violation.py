from extensions import db

# Violation Attributes
class Violation(db.Model):
    __tablename__ = 'violation'

    violation_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=True)
    address = db.Column(db.String(200), nullable=False, unique=True)
    phone = db.Column(db.Integer)
    license_no = db.Column(db.Integer, nullable=False, unique=True)

    vehicles = db.relationship('Vehicle', backref='violation')

    # A static method to get an violation data by the name
    @classmethod
    def get_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    # A static method to get an violation data by the id
    @classmethod
    def get_name_by_id(cls, violation_id):
        return cls.query.filter_by(violation_id=violation_id).first().name

    # Save the record
    def save(self):
        db.session.add(self)
        db.session.commit()
