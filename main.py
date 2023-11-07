import pandas as pd
obj = pd.read_json('message.json',orient='columns')
print(obj)
obj.index+=1
obj.to_csv('message_values.csv')
