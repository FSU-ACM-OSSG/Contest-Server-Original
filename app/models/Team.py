from app import db
# from app.models import Profile

# from sqlalchemy.types import TypeDecorator, Unicode

# class CoerceUTF8(TypeDecorator):
#     """Safely coerce Python bytestrings to Unicode
#     before passing off to the database."""
#
#     impl = Unicode
#
#     def process_bind_param(self, value, dialect):
#         if isinstance(value, str):
#             value = value.decode('utf-8')
#         return value

class Team(db.Document):
    team_name = db.StringField(required=True)
    username = db.StringField(required=True, unique=True)
    password = db.StringField(required=True)

    # members = db.relationship("Profile",back_populates="team")
    members = db.ListField(db.ReferenceField('Profile'))


    def __repr__(self):
        if self.team_name is not None:
            return '<Team %r>' % self.team_name
        else:
            return super(Team, self).__repr__()

    def csv(self, include_students=False):

        part1 = "{0},{1},{2}".format(self.username, self.password,
            self.team_name.encode('utf-8'))

        if include_students:
            for student in self.students:
                part1+=(","+str(student.fsuid))

        return part1