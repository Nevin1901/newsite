from flask import Blueprint
import requests
import json
import sys
from flask import render_template
from models.models import Repository
from models.models import VPSData
from markupsafe import escape

gb = Blueprint("github", __name__)


@gb.route("/github")
def GitHub():
    # https://api.github.com/users/Nevin1901/repos
    request = requests.get("https://repositories.nevin.cc/")
    repositories = json.loads(request.text)
    totalRepositories = []
    for repository in repositories:
        totalRepositories.append(Repository(repository["name"], repository["description"],
                                            repository["language"], repository["html_url"], repository["stargazers_count"], ("https://raw.githubusercontent.com/Nevin1901/" + repository["name"] + "/" + repository["default_branch"] + "/images/1.png")))
    return render_template('github.html', repositories=totalRepositories)


@gb.route("/status")
def status():
    return render_template('status.html')


@gb.route("/user/<string:username>/<int:userId>")
def user(username, userId):
    return escape(username + " " + str(userId))
