from app import db

class User(db.Model):
    user_id = db.Column(db.String(8), primary_key = True)
    invite_text = db.Column(db.String(60), nullable = False)
    language = db.Column(db.String(2), nullable = False)
    answer = db.Column(db.Boolean())
    email = db.Column(db.String(50))

    def __init__(self, user_id, invite_text, language):
        self.user_id = user_id
        self.invite_text = invite_text
        self.language = language

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.user_id)

    def __repr__(self):
        return '<User: {}, {}, {}, {}>'.format(
            self.user_id,
            self.invite_text,
            self.language,
            self.answer
        )

class Person(db.Model):
    id         = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(64))
    last_name  = db.Column(db.String(64))
    user_id    = db.Column(db.String(8), db.ForeignKey("user.user_id"), nullable = False)

    def __repr__(self):
        return '{}, {}'.format(self.last_name, self.first_name)

class FoodChoice(db.Model):
    id         = db.Column(db.Integer, primary_key = True)
    person     = db.Column(db.Integer, db.ForeignKey("person.id"), unique = True, nullable = False)
    vegetarian = db.Column(db.Boolean)
    vegan      = db.Column(db.Boolean)
    kid_menu   = db.Column(db.Boolean)
    allergy    = db.Column(db.String(128))

    def __repr__(self):
        diet = 'Normal'

        if self.vegetarian:
            diet = 'Vegetarian'
        if self.vegan:
            diet = 'Vegan'

        return '<FoodChoice: p_id: {}, Diet: {}, Kid Menu: {}, Allergies: {}'.format(
            self.person,
            diet,
            'YES' if self.kid_menu else 'NO',
            self.allergy if self.allergy else 'None'
        )
