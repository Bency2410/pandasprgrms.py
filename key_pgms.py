import pandas as pd
arr={"Name":["Dhanya","Arya","Divya"],
"Rollno":[1,2,3],
"Admssnno":[1651,2013,567]}
df=pd.DataFrame(arr)
print(df[["Name","Rollno"]])