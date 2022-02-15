import os
import pandas as pd

entries = os.listdir('data/')

## MAIN PROGRAM FUNCTION
def project_program():
  print('Please Select the file you wish to review...\n')

## DISPLAYS FILES IN "DATA" FOLDER
  for entry in entries:
     print(entry)


  selection = input('\n Please enter the name of the file you wish to review... ')

##CREATES URL BASED ON FILE SELECTION
  url = "data/" + selection
  

  if selection in entries:
    print("\n You selected, " + selection + ". Is that correct?")
    confirmation = input("Yes or No? ")
    
  else:
    print('\n There is no file by that name. Please check your spelling.')
    confirmation = input("Press Enter To Try Again")
    project_program()

    

  df = pd.read_csv(url)


  if confirmation.lower() == 'yes':
    print(url)
    print(df)
    next = input("Would you like to like to view another file? Yes/No? ")
    if next.lower() == 'yes':
      project_program()
    else:
      exit()

  else: 
    project_program()



project_program()

