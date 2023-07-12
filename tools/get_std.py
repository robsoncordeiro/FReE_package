# Script to get the standard deviation of the datasets
import pandas as pd

input_path = 'datasets/SUSY.csv'
output_path = 'SUSY_std_out.csv'
separator = ','

df = pd.read_csv(input_path, header=None, index_col=False, sep=separator)
df.std().to_csv(output_path)
