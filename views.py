# -*- coding: utf-8 -*-
from flask import render_template, request
from clean_ex import app
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
import pandas as pd
import psycopg2
from Bio import SeqIO
import numpy as np
from collections import Counter
#from nltk import *
from sklearn import linear_model
from .a_Model import ModelIt
#from .addl_funx import find_ngrams

#user = 'tsoare'                     
#host = 'localhost'

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html",
       title = 'Home', user = { 'nickname': 'Fooey McFooBar' },
       )

@app.route('/input')
def input():
    return render_template("input.html")

@app.route('/output')
def output():
  #pull 'input sequence' from input field and store it
  user_sequence = request.args.get("user_sequence")

  #print user_sequence
  
  rand_bf = []
  the_result = ModelIt(user_sequence, rand_bf)
  return render_template("output.html", rand_bf = rand_bf, the_result = the_result)

