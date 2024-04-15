from extensions import db

# Violation Attributes
class Violation(db.Model):
    __tablename__ = 'violation'

    violation_id = db.Column(db.Integer, primary_key=True)
    violation_date = db.Column(db.String(80), nullable=False, unique=True)
    violation_type = db.Column(db.String(200), nullable=False)
    violation_status = db.Column(db.String(80), nullable=False)
    
    vehicle_id = db.Column(db.Integer(), db.ForeignKey("vehicle.vehicle_id"))

    # A static method to get an violation data by the name
    @classmethod
    def get_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    # A static method to get an violation data by the id
    @classmethod
    def get_by_id(cls, violation_id):
        return cls.query.filter_by(violation_id=violation_id).first().name

    # Save the record
    def save(self):
        db.session.add(self)
        db.session.commit()
