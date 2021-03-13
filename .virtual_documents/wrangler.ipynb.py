import pandas as pd
import numpy as np


df = pd.read_csv("./3000-vocb-only.csv", names=['vocab'])
df


test_df = pd.DataFrame({'col1': ['aaa', 'xaaaa'],
                   'col2': ['bbb', 'ybbbb']},
                  index=['row1', 'row2'])
test_df


test_df.assign(new=lambda x: x.col1.str[0].str.capitalize())


a = pd.Series(['a','b','c'])


a


type(a[0])


df = df.assign(first_letter=lambda row: row.vocab.str[0].str.upper())
df


df.query("first_letter == 'A' ")


df.groupby('first_letter').describe()


df.loc[df.first_letter=='B']


alphabets  = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
dictionary = {}

for letter in alphabets:
    dictionary[letter] = df.loc[df.first_letter==letter].vocab.to_numpy().tolist()


dictionary



