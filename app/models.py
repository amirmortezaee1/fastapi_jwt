import datetime  as datetime
import sqlalchemy as sqlalchemy
import sqlalchemy.orm as orm 
import passlib.hash as  hash 

import database as database 

class UserModel(database.Base):
    __tablemame__ = "users"
    id = sqlalchemy.Column(sqlalchemy.Integer)
    email = sqlalchemy.Column(sqlalchemy.String, unique= True, index=True)
    password_hash = sqlalchemy.Column(sqlalchemy.String)
    created_at = sqlalchemy.Column(sqlalchemy.DateTime, default = datetime.datetime.utcnow)
    posts = orm.relationship("Post", back_populates= "users")
    
    def password_verification(self, password: str):
        return hash.bcrypt.verify(password, self.password_hash)
class PostModel(database.Base):
    __tablename__ ="posts"
    id = sqlalchemy.Column(sqlalchemy.Integer)
    user_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("user.id"))
    post_title = sqlalchemy.Column(sqlalchemy.String, index = True)
    post_description = sqlalchemy.Column(sqlalchemy.String, index = True)
    created_at = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.utcnow)
    users = orm.relationship("User", back_populates="posts")