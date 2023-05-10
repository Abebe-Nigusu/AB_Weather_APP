from flask import Flask, render_template, redirect, session, request, flash
from flask_app import app
from flask_app.models.model_favorites import Favorite
from flask_app.models.model_user import User

import requests
import configparser

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/favorite/create',  methods=['POST'])
def add_favorite():

    if 'user_id' not in session:
        return redirect('/subscribe')
    data = {
        "location": request.form["location"],
        "user_id": session["user_id"]
    }
    Favorite.create_favorite(data)
    return redirect('/')


@app.route('/myfavorites')
def get_my_favorites():
    if 'user_id' not in session:
        return redirect('/')
    user_data = {
        "id": session['user_id']

    }
    favorites = Favorite.get_my_favorites(user_data)
    # print("*****************&&&&&&&&&&&&&", favorites)
    appid = "292d2ecbe4f5709f56c1be3c3c93dd47"
    results = []
    for favorite in favorites:
        location = favorite.location
        # print("###############@@@@@@@@@", location)
        api_url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={appid}"

        response = requests.get(api_url)

        result = response.json()
        results.append(result)
    # print("%%%%%%%%%%%%%%%%%", results)
    return render_template("new_favorite.html", results=results, user=User.get_user_by_id(user_data))
