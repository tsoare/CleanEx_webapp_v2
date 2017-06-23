# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, redirect, url_for
from clean_ex2 import app
import pandas as pd
import numpy as np
#from .a_Model3 import ModelIt
from .a_Model4 import ModelIt
import os
from werkzeug import secure_filename

#user = 'tsoare'                     
#host = 'localhost'

@app.route('/')                        
@app.route('/upload')
def upload_file():
   return render_template('upload.html')
	

@app.route('/output', methods = ['GET', 'POST'])
def predict():
   if request.method == 'POST':
      #pull 'input sequence' from input field and store it
      user_file = request.files["user_file"]
      #user_file.save(secure_filename(user_file.filename))
      #print user_file#.filename
      the_result = ModelIt(user_file)
      return render_template("output.html", the_result = the_result)

