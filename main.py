import flask
from flask import Flask, render_template, request, make_response
from faker import Faker
import csv
import requests


app = Flask(__name__)

@app.route("/requirements/")
def requirements():
    with open("requirements.txt", 'r') as text:
        return text.read()


requirements()


f = Faker()

@app.route("/generate_users/<int:user_count>/")
def generate_users(user_count):
    name = f.name()
    email = f.email()
    users = dict()

    for num in range(1, 101):
        if num == user_count:
            users[user_count] = name, email
            return users
            # return flask.render_template('generate_users.html')



@app.route("/mean/")
def mean():
    weights = 0
    len_file = 25000
    with open("hw.csv", 'r') as file:
        reader = csv.reader(file)
        x = list(next(reader))

        for rows in reader:
            for el in rows:
                if float(el) > 0:
                    weights += float(el)
                    mean_weight = weights / len_file
        return str(mean_weight)



@app.route("/space/")
def number_of_astro():
    resp = requests.get('http://api.open-notify.org/astros.json')
    data = resp.json()['number']
    data = str(data)
    return data


if __name__ == '__main__':
    app.run(debug=True)


