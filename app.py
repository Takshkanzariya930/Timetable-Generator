from flask import Flask, render_template, request, redirect, url_for, session, flash
from display import forms
from utils.db import *
from utils.handling_json_files import *


app = Flask(__name__,template_folder="display/templates")
app.secret_key = "my_secret_key"

@app.route('/', methods=['GET', 'POST'])
def home():

    pass

@app.route('/classes', methods=['GET', 'POST'])
def classes():
    
    pass

if __name__ == '__main__':
     app.run(host="0.0.0.0",debug=True)