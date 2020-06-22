#!/usr/bin/env python3

import pandas as pd

def cities():
    idx = ["Helsinki", "Espoo", "Tampere", "Vantaa", "Oulu"]
    pop = pd.Series([643272, 279044, 231853, 223027, 201810], index=idx, name="Population")
    area = pd.Series([715.48, 528.03, 689.59, 240.35, 3817.52], index=idx, name="Total area")
    return pd.DataFrame({"Population": pop, "Total area": area})
    
def main():
    print(cities())
    
if __name__ == "__main__":
    main()
