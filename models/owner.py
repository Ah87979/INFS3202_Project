from extensions import db

# Owner Attributes
class Owner(db.Model):
    __tablename__ = 'owner'

    owner_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=True)
    address = db.Column(db.String(200), nullable=False, unique=True)
    phone = db.Column(db.Integer)
    license_no = db.Column(db.Integer, nullable=False, unique=True)

    vehicles = db.relationship('Vehicle', backref='owner')

    @property
    def data(self):
        return {
            'owner_id': self.owner_id,
            'name': self.name,
            'address': self.address,
            'phone': self.phone,
            'license_no': self.license_no
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
    def get_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def get_by_id(cls, owner_id):
        return cls.query.filter_by(owner_id=owner_id).first()
    
    @classmethod
    def get_name_by_id(cls, owner_id):
        return cls.query.filter_by(owner_id=owner_id).first().name

    def save(self):
        db.session.add(self)
        db.session.commit()
