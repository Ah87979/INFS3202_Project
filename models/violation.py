from extensions import db

# Violation Attributes
class Violation(db.Model):
    __tablename__ = 'violation'

    violation_id = db.Column(db.Integer, primary_key=True)
    violation_date = db.Column(db.Integer, nullable=False, unique=True)
    violation_type = db.Column(db.String(200), nullable=False)
    violation_status = db.Column(db.String(80), nullable=False)
    
    vehicle_id = db.Column(db.Integer(), db.ForeignKey("vehicle.vehicle_id"))

    @property
    def data(self):
        return {
            'violation_id': self.violation_id,
            'violation_date': self.violation_date,
            'violation_type': self.violation_type,
            'violation_status': self.violation_status,
            'vehicle_id': self.vehicle_id
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_all(cls):
        r = cls.query.all()

        result = []

        for i in r:
            result.append(i.data)

        return result

    @classmethod
    def get_by_id(cls, id):
        return cls.query.filter(cls.violation_id == id).first()

    # Save the record
    def save(self):
        db.session.add(self)
        db.session.commit()
