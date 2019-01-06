# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 13:21:13 2019

@author: AnhNVT2
"""
import os
import re
import codecs
import numpy as np
import theano
import pdb

models_path = "models"
eval_path = "evaluation"
eval_temp = os.path.join( eval_path, "temp")
eval_script = os.path.join(eval_path, "conlleval.pl")
print(eval_script)
print(os.path.isfile(eval_script))