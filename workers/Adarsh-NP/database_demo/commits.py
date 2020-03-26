'''Python flask application for creating and inserting data into the commits table'''

import os
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class commits(db.Model):
    __tablename__ = "commits"
    short_id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, nullable=False)
    title = db.Column(db.String, nullable=False)
    message = db.Column(db.String, nullable=False)
    author_name = db.Column(db.String, nullable=False)
    author_email = db.Column(db.String, nullable=False)
    committer_name = db.Column(db.String, nullable=False)
    committer_email = db.Column(db.String, nullable=False)