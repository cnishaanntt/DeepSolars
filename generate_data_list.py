""" Generate lists containing filepaths and labels for training, validation and evaluation. """
import pickle
import os.path
import random
import pandas as pd

##### generate test set #####
TEST_SET_DIR = 'SPI_eval'
test_set_list = []
pos_num = 0
neg_num = 0
eval_set_meta = pd.read_csv(os.path.join(TEST_SET_DIR, 'eval_set_meta.csv')).values
for index in range(1, 66):
    region_type = eval_set_meta[index-1, 5] # get the type of the regions
    region_dir = os.path.join(TEST_SET_DIR, str(index))

    # negative samples
    for i in range(1, 3001):
        img_path = os.path.join(region_dir, '0', str(i) + '.png')
        if not os.path.exists(img_path):
            continue
        neg_num += 1
        test_set_list.append((img_path, [0], index, i, region_type))

    # positive samples
    for i in range(1, 3001):
        img_path = os.path.join(region_dir, '1', str(i) + '.png')
        if not os.path.exists(img_path):
            continue
        pos_num += 1
        test_set_list.append((img_path, [1], index, i, region_type))

with open('test_set_list.pickle', 'w') as f:
    pickle.dump(test_set_list, f)

print ('Test set list done. # positive samples: '+str(pos_num)+' # negative samples: '+str(neg_num))
