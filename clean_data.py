#import lib
import pandas as pd
import os
import sqlalchemy
#import data
df = pd.read_csv("D:\\PROJECT\\data.csv")
#check datatype
df.dtypes
#covert 'DATE' Column 
df ['Date'] = pd.to_datetime(df['Date'])
#extract and add ‘hour’ column from 'Date' column
transactions['houroftheday'] =transactions['transaction_date'].dt.hour
#extract and add 'source' column from 'MA Referrer' 
df['MA Referrer'] = df['MA Referrer'].astype(str)
pattern = re.compile(r'://[^/]+?\.([a-zA-Z0-9]+)')
df['source'] = df['MA Referrer'].apply(lambda url: re.search(pattern, 
url).group(1) if re.search(pattern, url) else 'Unknown') 
df['Email']= df['Email'].astype(str)
df['Domain']=df['Email'].apply(lambda x: x.split('@')[-1])
df['Customer Type'] = df['Domain'].apply(lambda x: 'Người bình thường' if
'gmail.com' in x else
('Nhân viên' if 'outlook' in x or 'outlook.com.vn' in x
else 'Sinh Viên'))
