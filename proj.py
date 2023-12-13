import pandas as pd
import numpy as np


def main():
    # var initialization, commented code meant to strip recoded fields
    # commented out due to some data not being available not recoded in PUF
    # will look further into it
    df = pd.read_csv("./data/rhfspuf.csv")
    # non_recode = [
    #     "CAPRATE_R",
    #     "MRKTVAL_R",
    #     "PURPRICE_R",
    #     "MRENTRCTS_R",
    #     "TRENTPRCTPV_R",
    #     "OPTAX_R",
    #     "APPVAL_R",
    # ]
    # creation of target dataframe
    # targdf = df[[x for x in df.columns if ((x[-2:] != "_R") | (x in non_recode))]]
    targdf = df[df.OUTCOME.isin([1, 3, 5, 7, 201, 203, 204])]
    targdf = targdf[~targdf.RENT.isin([-9, -8])]
    targdf = targdf[targdf.COMMSPACE.isin([-9, 2])]
    print(targdf)


if __name__ == "__main__":
    main()
