# Script to generate uniform samples for the FOREX dataset (to enable the KPCA process)
import pandas as pd

input_dataset = "datasets/forex.csv"
separator = ','

df = pd.read_csv(input_dataset, header=None, index_col=False, sep=separator)

#remove label column (optional)
#df.drop([0], axis=1, inplace=True)

print df.shape

for x in range(10):
	df_s = df.sample(frac=0.1)

	print df_s.shape
	df_s.to_csv("forex_s%d.csv" % x)

