# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, redirect, url_for
from clean_ex2 import app
import pandas as pd
import numpy as np
#from .a_Model3 import ModelIt
from .a_Model4 import ModelIt
import os
from werkzeug.utils import secure_filename
from Bio import SeqIO


#user = 'tsoare'                     
#host = 'localhost'

UPLOAD_FOLDER = 'clean_ex2/static/data'
ALLOWED_EXTENSIONS = set(['fa', 'fasta', 'fas', 'seq', 'fsa'])

#app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
          
          
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def seqrecord_length_passes(seq_record):
    passed = len(seq_record.seq) > 950 and len(seq_record.seq) < 1050
    print passed
    return passed

def seqrecord_alphabet_passes(seq_record):
    passed = set(str(seq_record.seq)) == set(['A', 'C', 'G', 'T'])
    print passed
    return passed
    

@app.route('/')                        
@app.route('/upload')
def upload_file():
   return render_template('upload.html')
	


@app.route('/output',methods=['GET','POST'])
def upload():
    # Get the name of the uploaded file
    select = request.form.get('Go_select')
    print(select)

    if select == "test_data":
        file = True
        target_file_path = os.path.join(app.config['UPLOAD_FOLDER'], "my_promoters_to_test.fa")
        filename = "my_promoters_to_test.fa"
    elif select == "user_choose":
        file = request.files['user_input']
        #if not allowed_file(file.filename):
            #return render_template('file_error.html')
        #else:
        filename = secure_filename(file.filename)
        print("filename:")
        print(filename)
        target_file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(target_file_path)
    #else:
        #file = None

    #if not file:
        #return render_template('file_error.html')
    target = app.config['UPLOAD_FOLDER']
    user_file = os.path.join(target, filename)
    
    
    # check sequence length and alphabet:
    pass_records = []
    fail_records = []
    for seq_record in SeqIO.parse(user_file, "fasta"):
        #print(seq_record)
        if seqrecord_length_passes(seq_record) and seqrecord_alphabet_passes(seq_record):
            pass_records.append(seq_record)
        else:
            fail_records.append(seq_record)
    
    if fail_records: 
        return render_template("error.html")
    else:
    
        # analyze:
        the_result = ModelIt(pass_records)
        return render_template("output.html", the_result = the_result)


