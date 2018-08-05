import pandas as pd
import numpy as numpy
def excel_to_dataframe(excel_file):
    df = pd.read_excel(excel_file)
    row_pl = df[df['Data provided by SimFin']== 'Profit & Loss statement'].index[0]
    row_bs = df[df['Data provided by SimFin'] == 'Balance Sheet'].index[0]
    row_cf = df[df['Data provided by SimFin']== 'Cash Flow statement'].index[0]
    pl_df = df.iloc[row_pl:row_bs-1, 1:]
    pl_df.columns = pl_df.iloc[1]
    pl_df.set_index('in million USD', inplace = True)
    pl_df.dropna(axis=0)
    pl_df = pl_df[2:]
    bs_df = df.iloc[row_bs:row_cf, 1:]
    bs_df.columns = bs_df.iloc[1]
    bs_df.set_index('in million USD', inplace = True)
    bs_df = bs_df.iloc[2:]
    cf_df = df.iloc[row_cf: ,1:]
    cf_df.columns = cf_df.iloc[1]
    cf_df.dropna()
    cf_df.set_index('in million USD',inplace = True)

    return df, pl_df, bs_df, cf_df

def transpose_dataframe(excel_file):
    df = pd.read_excel(excel_file)
    row_pl = df[df['Data provided by SimFin']== 'Profit & Loss statement'].index[0]
    row_bs = df[df['Data provided by SimFin'] == 'Balance Sheet'].index[0]
    row_cf = df[df['Data provided by SimFin']== 'Cash Flow statement'].index[0]
    pl_df = df.iloc[row_pl:row_bs-1, 1:]
    pl_df.columns = pl_df.iloc[1]
    pl_df.set_index('in million USD', inplace = True)
    pl_df.dropna(axis=0)
    pl_df = pl_df[2:]
    bs_df = df.iloc[row_bs:row_cf, 1:]
    bs_df.columns = bs_df.iloc[1]
    bs_df.set_index('in million USD', inplace = True)
    bs_df = bs_df.iloc[2:]
    cf_df = df.iloc[row_cf: ,1:]
    cf_df.columns = cf_df.iloc[1]
    cf_df.dropna()
    cf_df.set_index('in million USD',inplace = True)
    pl_df_T = pl_df.T
    df_t = df.T
    bs_df_T = bs_df.T
    cf_df_T = cf_df.T

    return DF, PL_df, BS_df, CF_df


    
    