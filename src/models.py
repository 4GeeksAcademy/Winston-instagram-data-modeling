import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er
from datetime import datetime

Base = declarative_base()

class Follower(Base):
    __tablename__ = 'follower'

    id = Column(Integer(), primary_key=True)
    user_from_id = Column(Integer, ForeignKey("user.id"),nullable=False)
    user_to_id = Column(Integer, ForeignKey("user.id") ,nullable=False)
    user_from = relationship("User", back_populates="follower")
    user_to = relationship("User", back_populates="follower")

    
class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table user
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False, unique=True)
    firstname = Column(String(100), nullable=False)
    lastname = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    created_at = Column(DateTime(), default=datetime.now)
    post = relationship('Post', back_populates="user")
    comment = relationship('Comment', back_populates="user")


class Comment(Base):
    __tablename__ = 'comment'
    # Here we define columns for the table comment.
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(250))
    author_id = Column(Integer, ForeignKey("user.id"))
    post_id = Column(Integer, ForeignKey("post.id"))
    user = relationship("User", back_populates="comment")
    post = relationship("Post", back_populates="comment")

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", back_populates="post")
    media = relationship("Media", back_populates="post")

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key= True)
    type = Column(String)
    url = Column(String(250))
    post_id = Column(Integer, ForeignKey("post.id"))
    post = relationship("Post", back_populates="media")

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
