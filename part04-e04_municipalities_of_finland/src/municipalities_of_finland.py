#!/usr/bin/env python3

import pandas as pd

def municipalities_of_finland():
    df = pd.read_csv("src/municipal.tsv", sep="\t", index_col="Region 2018")
    #index_col=0
    return df["Akaa":"Äänekoski"]
    '''
    df.drop('WHOLE COUNTRY', inplace=True)
    return df[:311]
    '''
    #df[:df.index.get_loc('Äänekoski')+1]
    
def main():
    print(municipalities_of_finland())
    
if __name__ == "__main__":
    main()
