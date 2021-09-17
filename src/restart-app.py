# Python script to restart given Heroku app

import os
import sys

if len(sys.argv) < 2:
    print("Usage: restart-app.py <Heroku app to be restarted>")
    sys.exit()

APP = sys.argv[1]

os.system("heroku restart --app " + APP)
