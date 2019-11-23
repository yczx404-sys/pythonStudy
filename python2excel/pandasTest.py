import pandas as pd
data = {"姓名":["庞娅惠","刘超"],"性别":["男","女"],"课程":["python","java"]}
df = pd.DataFrame(data)
df.to_excel("demo1.xlsx", sheet_name="程序员",index=False, header=True)