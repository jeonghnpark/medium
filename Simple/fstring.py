
variable='alignment'

print(f"{variable:>20}")  #left align
print(f"{variable:<20}")
print(f"{variable:^20}")  #center

import pandas as pd

df=pd.DataFrame.from_dict({2019:[1,4,7,2,3,1], 2020:[5,4,3,2,3,5], 2021:[1,5,3,7,6,4]})
print(df)

for col in [2020,2021]:
    df[f'{col} Rolling5']=df[col].rolling(5).mean()

print(df)

#formatting

df=pd.DataFrame.from_dict({'Value':[2342423423.23423,23412312.34,9059646.256]})
print(df)
df['Currency']=[f"${x:,.2f}" for x in df['Value']]
print(df)
print(df.loc[1][0]+4)
#print(df.loc[1][1]+4)   #error since 'currency' is string type
df['Currency2']=df["Value"].apply(lambda x:f"{x:,.3f}")
print(df)

#pad with zero

df=pd.DataFrame.from_dict({'ID':[2423423423,234234234,2342334]})
print(df)
df['padding']=[f"{x:012}" for x in df["ID"]]
print(df)
df['padding2']=df['ID'].apply(lambda x:f"{x:09}")
print(df)