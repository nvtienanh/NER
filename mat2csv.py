# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 19:50:06 2018

@author: AnhNVT2
"""

import scipy.io
import pandas as pd
import numpy as np

char_layer_data = scipy.io.loadmat('models/english/char_layer.mat')
char_layer_info = scipy.io.whosmat('models/english/char_layer.mat')

mat_files = ['char_layer',
             'char_lstm_for',
             'char_lstm_rev',
             'final_layer',
             'tanh_layer',
             'transitions',
             'word_layer',
             'word_lstm_for',
             'word_lstm_rev']

for mfile in mat_files:
    
    file_path = 'models/english/' + mfile + '.mat'
    save_path = 'models/english/' + mfile
    _data = scipy.io.loadmat(file_path)
    _info = scipy.io.whosmat(file_path)

    lists = [item[0] for item in _info]
    for table in lists:
        data = _data[table]
        np.savetxt((save_path + '/' + table + ".csv"), data, delimiter=',')

print('Done!')
#data = scipy.io.loadmat("subject.mat")
#
#for i in data:
#	if '__' not in i and 'readme' not in i:
#		np.savetxt(("filesforyou/"+i+".csv"),data[i],delimiter=',')
