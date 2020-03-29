from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Contributor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    repo_id = db.Column(db.Integer)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    commits = db.Column(db.Integer)
    additions = db.Column(db.Integer)
    deletions = db.Column(db.Integer)
    updated_at = db.Column(
        db.DateTime,
        server_default=db.func.now(),
        server_onupdate=db.func.now()
    )
