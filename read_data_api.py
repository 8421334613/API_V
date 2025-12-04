import requests
import pandas as pd

data=requests.get("https://jsonplaceholder.typicode.com/users").json()

df=pd.DataFrame(data)
print(df)