from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import model_user

import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class Favorite:
    DB = "weather_app_db"

    def __init__(self, data):
        self.id = data['id']
        self.location = data['location']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.uer_id = data['user_id']

    @classmethod
    def create_favorite(cls, data):
        query = "INSERT INTO favorites (location, user_id) VALUES(%(location)s, %(user_id)s);"
        return connectToMySQL(cls.DB).query_db(query, data)
        

    @classmethod
    def get_my_favorites(cls,data):
        query = "SELECT * FROM favorites WHERE user_id = %(id)s;"
        results = connectToMySQL(cls.DB).query_db(query, data)
        all_my_favorites = []
        for row in results:
            all_my_favorites.append(cls(row))
        return all_my_favorites

