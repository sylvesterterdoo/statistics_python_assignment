import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# TODO: remove this script before you submit 
# upload a csv file with two columns
def Main():
    df = pd.DataFrame([[4, 9]] * 3, columns=['A', 'B'])
    r = df['B'].apply(np.sqrt)
    print(df)
    print(r)
    


# Starter program
if __name__ == '__main__':
    Main()