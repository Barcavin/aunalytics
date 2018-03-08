import pandas as pd
import numpy as np
train = pd.read_csv("/home/kevindong1994/aunalytics/au_train.csv", header=0, delimiter=",")
test = pd.read_csv("/home/kevindong1994/aunalytics/au_test.csv", header=0, delimiter=",")

complete_data = pd.concat([train,test],keys=["train","test"]) # Combine the two dataset. It will make the get_dummies method more convenient.

# Convert all categorical columns to dummy variable
for each in train.select_dtypes(include="object").dtypes.index[:-1]:
    complete_data = pd.concat([complete_data,pd.get_dummies(complete_data[each],prefix = each,drop_first = True)],axis=1)