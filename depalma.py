#!/usr/bin/env python3

from flask import Flask
from flask_github import GitHub

app = Flask(__name__)
app.config['GITHUB_CLIENT_ID'] = 'hickey'
app.config['GITHUB_CLIENT_SECRET'] = '04b338f565bb627bab0a9c2faf994a3bbc72a54f'

# For GitHub Enterprise
app.config['GITHUB_BASE_URL'] = 'https://api.github.com/api/v3/'
app.config['GITHUB_AUTH_URL'] = 'https://github.com/login/oauth/'

github = GitHub(app)
