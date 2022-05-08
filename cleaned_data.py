import pandas as pd

# create a dataframe
data=pd.read_csv('cleaned_data.csv')
df = pd.DataFrame(data)
print(df.head())

# create a subset of the dataframe

for topic in topics:
  temp_df = data[data['topic'] == topic][:5000]
  df = pd.concat([df, temp_df])

# create_vectors

df['vector'] = df['title'].apply(lambda x: nlp(x).vector)

#drop columns

df = df[['topic', 'title']]

#drop 'NATION' and 'WORLD" labels
data = df[df['topic'] != 'NATION' or df['topic'] != 'WORLD']


# clean_dict
for i in range(len(data)):
  for key in data[i].keys():
    data[i][key] = data[i][key]["S"]

print(data[:2])

# list of dict

import

data = []
with open('data.json', 'r') as f:
  data = f.readlines()

data = [json.loads(item)['Item'] for item in data]

print(data[:2])

# count_labels_plot

counts = data['topic'].value_counts()
counts.plot(kind='bar', legend=False, grid=True, figsize=(8, 5))


