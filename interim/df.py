import pandas as pd

vardict = {
    'Q': 'hus',
    'V': 'va',
    'U': 'ua',
    'Z': 'z',
    'R': 'hurs',
    '2T': 'tas',
    'T': 'ta',
    'MN2T': 'tasmin',
    'MX2T': 'tasmax',
    'SLP': 'psl',
    'SST': 'sst',
    'TP': 'pr',
}

df = pd.read_pickle('interim20_daily.pickle')
df[('GLOBALS', 'stdvarname')] = df[('GLOBALS', '_DRS_variable')].map(vardict)
df.to_pickle('interim20_daily.pickle')
