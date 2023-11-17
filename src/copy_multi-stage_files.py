#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Copy files for multi-stage TEP problems

@author: abdelrahmanayad
"""

from pathlib import Path
import os
import pandas as pd
import numpy as np
import shutil

# Directories and files
parent_dir = Path(__file__).parents[1]
# data_dir   = os.path.join(parent_dir, 'data')
# results_dir   = os.path.join(parent_dir, 'results')

cases_dir    = os.path.join(parent_dir, 'Example_Systems')
inputs_folder = 'Inputs'
inputs_prefix = 'Inputs_p'

case_name = 'Graver_10years_BESS_full'
case_dir  = os.path.join(cases_dir, case_name)
initial_period = os.path.join(case_dir, inputs_folder, 'Inputs_p1')

num_periods = 10
load_growth = 0.04
replace_old_files = True

def create_load_file(df, p, load_growth):
    load_cols = [c for c in df.columns if "Load" in c]
    
    for col in load_cols:
        df[col] = [d * (1+load_growth)**2 for d in df[col]]
        
    return df

for p in range(2, num_periods+1):
    print(f'processing period {p}')
    new_period_folder = os.path.join(case_dir, inputs_folder, inputs_prefix + str(p))
    
    if not os.path.exists(new_period_folder): os.mkdir(new_period_folder)
        
    for root, dirs, files in os.walk(initial_period):
        for filename in files:            
            old_file = os.path.join(initial_period, filename)
            new_file = os.path.join(new_period_folder, filename)   
            
            if replace_old_files or not os.path.exists(new_file):
                if filename =='Load_data.csv':
                    df = pd.read_csv(old_file)            
                    new_df = create_load_file(df, p, load_growth)
                    new_df.to_csv(new_file, index = False)
                    
                else:
                    shutil.copy(old_file, new_file)