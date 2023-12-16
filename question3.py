import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Upload a csv file with two columns (Name, Age)
# if a valid csv file is uploaded, plot a histogram of ages
def Main():
    st.set_option('deprecation.showPyplotGlobalUse', False)

    st.write('Upload a valid CSV file with two column (Name, Age)')
    uploaded_file = st.file_uploader("Choose a file")

    if uploaded_file is not None:
        dataframe = pd.read_csv(uploaded_file)
        ages_series = dataframe['Age']
        ages = np.array(ages_series)
        plt.hist(ages)

        # Label the graph
        plt.xlabel('Age distribution')
        plt.ylabel('Frequency')
        plt.title('Histogram of Ages')

        print('Plotting age from csv')
        st.pyplot()
        # st.write(dataframe)
    else:
        print('Upload a valid CSV file')


# Starter program
if __name__ == '__main__':
    Main()