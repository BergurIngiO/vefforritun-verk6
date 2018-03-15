from bottle import run, route, template, static_file, error, request
import requests
import os

@route('/')
def index():
    return template('index')

@route('/pizza')
def pizza():
    return template('pizza')

@route('/login')
def login():
    return template('login')

@route('/new_user', method = 'POST')
def new_user():
    email = request.forms.email
    user = request.forms.user
    password = request.forms.password
    return template('new_user', email=email, user=user, password=password)

@route('/order')
def order():
    fullname = request.query.fullname
    heimilisfang = request.query.heimilisfang
    netfang = request.query.netfang
    simi = request.query.simi
    pizzasize = int(request.query.pizzasize)
    Skinka = request.query.Skinka
    Beikon = request.query.Beikon
    Pepperoni = request.query.Pepperoni
    return template('order', fullname=fullname, pizzasize=pizzasize, Skinka=Skinka, Pepperoni=Pepperoni, Beikon=Beikon,
    heimilisfang=heimilisfang, netfang=netfang, simi=simi)



run()