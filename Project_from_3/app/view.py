from flask import Flask, render_template, request, redirect, url_for, flash, session
from datetime import datetime, date
import sys
import platform
from os import abort
import os

from flask import current_app as app
# from app import app, bcrypt #  import current_app


menu = {'Головна':'/', 'Коротка інформація':'/info', 'Мої досягнення':'/achievement', 'Contact':'/contact', 'FormTask':'/task', 'Login':'/login'}
today = date.today()
age = today.year - 2001 - ((today.month, today.day) < (4, 14))


@app.route('/')
def index():
    return render_template('index.html', menu=menu, my_os=platform.system(),
                           user_agent=request.headers.get('User-Agent'), version=sys.version,
                           time_now=datetime.now().strftime("%H:%M"))

@app.route('/info')
def info():
    return render_template('info.html', menu=menu,age=age, month=today.month, day=today.day)

@app.route('/achievement')
def achievement():
    return render_template('achievement.html', menu=menu)