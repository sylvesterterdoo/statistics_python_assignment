import pandas as pd

# FILE_NAME -> Name of csv file
# COLUMN_NAME -> name of column operation (vowel count) will be operated on

VOWELS = ['a', 'e', 'i', 'o', 'u']
FILE_NAME = 'titles.csv'
COLUMN_NAME = 'title'


def Main():
    # Read csv file
    print('Reading CSV file')
    df = pd.read_csv(FILE_NAME)

    # dataframe column cleanup
    new_df = df.dropna()

    # Select column from df
    column_selected_df = new_df[COLUMN_NAME]
    column_selected_df = column_selected_df.apply(str)

    # Apply function on column
    new_vowel_df = column_selected_df.apply(count_vowel)

    # Create new dataframe with 2 columns, selected column and vowel count 
    # result_df = pd.DataFrame({COLUMN_NAME: column_selected_df, 'Vowels_Count': new_vowel_df})
    # print(result_df.head(5))

    # Add new column to initial dataframe
    df['Vowels'] = new_vowel_df
    print(df)


# compute the vowel count of a given word
def count_vowel(word):
    vowels = set(VOWELS)
    count = 0

    lowcase_word = word.lower() 
    for character in lowcase_word:
        if character in vowels:
            count += 1
    return count


if __name__ == '__main__':
    Main()