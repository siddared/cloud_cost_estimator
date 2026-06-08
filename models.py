from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    username = db.Column(
        db.String(100),
        unique=True,
        nullable=False
    )

    password = db.Column(
        db.String(200),
        nullable=False
    )


class Estimate(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    username = db.Column(
        db.String(100)
    )

    region = db.Column(
        db.String(100)
    )

    ec2_type = db.Column(
        db.String(100)
    )

    ec2_hours = db.Column(
        db.Integer
    )

    s3_storage = db.Column(
        db.Float
    )

    rds_instances = db.Column(
        db.Integer
    )

    data_transfer = db.Column(
        db.Float
    )

    total_cost = db.Column(
        db.Float
    )

    created_at = db.Column(
        db.String(100)
    )