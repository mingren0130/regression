VERSION = 0.1

import numpy as np
from pandas import MultiIndex, Int64Index
import pandas as pd
import xgboost as xgb 
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import scale
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from sklearn import set_config 
from sklearn.model_selection import cross_val_predict
import sys, getopt,os
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from sklearn import metrics
import scipy as sp
from tqdm import tqdm

inputfile = ''
outputfile = ''

try:
	opts, args = getopt.getopt(sys.argv[1:],"hvi:o:")  
except getopt.GetoptError:
	print('Usage: python3 Reg.py\n  -i <input filename> (please use .csv files) \n  -o <output file>\n   [-h (Display this help message)]')
	sys.exit(2)                             
                                                                 
for opt, arg in opts:
	if opt == '-i':
		inputfile = arg
	elif opt == '-o':
		outputfile = arg
df = pd.read_csv(inputfile,dtype={'genome_id':str})
print('load ok')
X = df.iloc[0:,5:]
y = df['new_value']
xg_reg = xgb.XGBRegressor(objective ='reg:linear')
xg_reg.fit(X, y) 
feature_important = xg_reg.get_booster().get_score(importance_type='gain')
keys = list(feature_important.keys())
values = list(feature_important.values())
datagroup_v = pd.DataFrame(index=keys,data=values,columns=["score"]).sort_values(by = "score", ascending=False)

c=pd.DataFrame()
for iu in range(0,datagroup_v.shape[0],1):
	c = pd.concat([c, X[datagroup_v.index[iu]]], axis=1, names=datagroup_v.index[iu])

Best=0
point=0
from sklearn.model_selection import cross_val_score 
from sklearn.model_selection import train_test_split
aList = list()
for line in tqdm(range(0,c.shape[1],1)): 
	XX=c.iloc[:,:line+1]
	rfr = RandomForestRegressor()
	scores = cross_val_predict(rfr,XX,y,cv=10)
	#print("r2_score: %f" %r2_score(y,scores))
	aList.append(round(r2_score(y,scores), 4))
	if(r2_score(y,scores)>Best):
		Best=r2_score(y,scores)
		point=line
		print("Best r2_score: %f" %r2_score(y,scores))
		print("Best point =",point+1)


c = c.iloc[0:,:point+1]
rfr = RandomForestRegressor()
scores = cross_val_predict(rfr,c,y,cv=10)

rmse=np.sqrt(metrics.mean_squared_error(y,scores))
print("RMSE: %f" % (rmse))
print('Pearson’s p-value:',sp.stats.pearsonr(np.squeeze(y), scores))
print("MAE: %f" % mean_absolute_error(y,scores))
print("r2_score: %f" %r2_score(y,scores))




outF = open(outputfile, "w")
outF.write("Extracted ")
outF.write(str(datagroup_v.shape[0]))
outF.write(" features\n")

for line in datagroupxorr.columns.values:
	outF.write(line)
	outF.write("\n")

outF.write("RMSE is ")
outF.write(str(rmse))
outF.write("\n")
outF.write("Pearson’s p-value is")
outF.write(str(sp.stats.pearsonr(np.squeeze(y), scores)))
outF.write("\n")
outF.write("MAE is ")
outF.write(str(mean_absolute_error(y,scores)))
outF.write("\n")
outF.write("R2_score is ")
outF.write(str(r2_score(y,scores)))
outF.write("\n")


	

