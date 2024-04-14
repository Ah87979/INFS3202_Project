from extensions import db

# Owner Attributes
class Owner(db.Model):
    __tablename__ = 'owner'

    owner_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=True)
    address = db.Column(db.String(200), nullable=False, unique=True)
    password = db.Column(db.String(200))
    # is_active = db.Column(db.Boolean(), default=False)
    # created_at = db.Column(db.DateTime(), nullable=False, server_default=db.func.now())
    # updated_at = db.Column(db.DateTime(), nullable=False, server_default=db.func.now(), onupdate=db.func.now())

    vehicles = db.relationship('Vehicle', backref='owner')

    # A static method to get an owner data by the username
    @classmethod
    def get_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    # A static method to get an owner data by the email
    @classmethod
    def get_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    # A static method to get an owner data by the id
    @classmethod
    def get_name_by_id(cls, owner_id):
        return cls.query.filter_by(id=owner_id).first().username

    # Save the record
    def save(self):
        db.session.add(self)
        db.session.commit()
