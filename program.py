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
  
##CONFIRMS YOU CHOSE A VALID/CORRECT FILE

  if selection in entries:
    print("\n You selected, " + selection + ". Is that correct?")
    confirmation = input("\nYes or No? ")

  else:
    print('\n There is no file by that name. Please check your spelling.')
    confirmation = input("\nPress Enter To Try Again")
    project_program()

    
## IF SELECTION IS VALID, THIS VARIABLE READS THE CSV FILE

  df = pd.read_csv(url)

##IF USER CONFIRMS THEIR SELECTION, IT THEN DISPLAYS THE CONTENTS OF THE FILE

  if confirmation.lower() == 'yes':
    print("\n Now displaying the contents of " + selection + ":\n")
    print(df)
    next = input("\n Would you like to like to view another file? Yes/No? ")
    if next.lower() == 'yes':
      project_program()
    else:
      exit()

##IF THE USER CONFIRMS THAT THE SELECTION IS 
  else: 
    project_program()



project_program()

