import os
import pandas as pd

entries = os.listdir('data/')

print('Please Select the file you wish to review...\n')

for entry in entries:
    print(entry)

selection = input('\n Please enter the name of the file you wish to review... ')

if selection in entries:
  print("\n You selected, " + selection + ". Is that correct?")
else:
    print('\n There is no file by that name. Please check your spelling and try again.')

url = "data/" + selection

df = pd.read_csv(url)


print(url)
print(df)