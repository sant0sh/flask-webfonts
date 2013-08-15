from flask import Flask
from flask.ext.webfonts import Webfonts
from fonts import fonts

app = Flask(__name__)

wf = Webfonts(fonts, app)
# Alternatively use
# wf = Webfonts()
# wf.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)
