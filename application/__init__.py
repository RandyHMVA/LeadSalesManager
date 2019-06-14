from flask import Flask

app = Flask(__name__)
app.config.from_mapping(SECRET_KEY='f96e704a4b594b6986304ed5e5b5f0084a05461bab5b40f991957db9c8dbc000')

from application import routes