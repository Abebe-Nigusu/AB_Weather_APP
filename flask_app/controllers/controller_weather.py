from flask import Flask, render_template, redirect, session, request, flash

from flask_app import app
# from flask import Flask, render_template, request, redirect

import requests
import configparser


@app.route('/')
def weather_dashboard():
    return render_template('home.html')


@app.route('/results', methods=['POST'])
def render_results():
    city = request.form['city']
    units = request.form["units"]
    api_key = get_api_key()
    data = get_weather_results(city, units, api_key)

    temp = "{0: .2f}".format(data["main"]["temp"])
    feels_like = "{0: .2f}".format(data["main"]["feels_like"])
    icon = data["weather"][0]["icon"]
    weather = data["weather"][0]["main"]
    description = data["weather"][0]["description"]
    location = data["name"]

    return render_template('show_weather.html', units=units, temp=temp, feels_like=feels_like, icon=icon, weather=weather, description=description, location=location)


def get_api_key():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['openweathermap']['api']


def get_weather_results(city, units, api_key):
    appid = "292d2ecbe4f5709f56c1be3c3c93dd47"
    q = city

    api_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units={units}&appid={api_key}"

    print(api_url)
    response = requests.get(api_url)
    return response.json()


# print(get_weather_results("New York", "imperial", get_api_key()))


if __name__ == "__main__":
    app.run(debug=True)
