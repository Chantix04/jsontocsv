import pandas as pd
obj = pd.read_json('message.json',orient='records')
print(obj)
obj.index+=1
obj.to_cav('message_values.csv')
