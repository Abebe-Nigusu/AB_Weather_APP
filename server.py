from flask_app import app

# Import *ALL* controller files

from flask_app.controllers import controller_weather
from flask_app.controllers import controller_user
from flask_app.controllers import controller_favorites

# MUST BE AT THE BOTTOM
if __name__ == "__main__":
    app.run(debug=True)
