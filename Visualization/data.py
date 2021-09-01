import pandas as pd
pd.set_option('display.max_rows', 550)


#Read the csv file

df=pd.read_csv('Resources/cities.csv')

#save to file
df.to_html('data.html', index=False)

#Assign string
table = df.to_html(max_rows=None)
print(table)
