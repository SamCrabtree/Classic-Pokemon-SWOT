import os
import pandas as pd
import requests

entries = os.listdir('data/')

## MAIN PROGRAM FUNCTION

def project_program():
  print('Please Select the file you wish to review...\n')

## DISPLAYS FILES IN "DATA" FOLDER

  for entry in entries:
     print(entry)

## PROMPTS THE USER FOR WHICH FILE THEY WISH TO REVIEW

  selection = input('\n Please enter the name of the file you wish to review. OR type "EXIT" to close the program.')

## CREATES URL BASED ON USER FILE SELECTION

  url = "data/" + selection
  
##CONFIRMS YOU CHOSE A VALID/CORRECT FILE

  if selection in entries:
    print("\n You selected, " + selection + ". Is that correct?")
    confirmation = input("\nYes or No? ")

  else:
    print('\n There is no file by that name. Please check your spelling.')
    confirmation = input('\nPress Enter To Try Again OR type "EXIT" to close the program.')
    project_program() 

    
## IF SELECTION IS VALID, THIS VARIABLE READS THE CSV FILE

  df = pd.read_csv(url)

##IF USER CONFIRMS THEIR SELECTION, IT THEN DISPLAYS THE CONTENTS OF THE FILE

  if confirmation.lower() == 'yes':
    print("\n Now displaying the contents of " + selection + ":\n")
    print(df)
    next = input("\n Would you like to like to view another file? Yes/No? If not, hit enter to exit.")
    if next.lower() == 'yes':
      project_program()
    else:
      exit()

##IF THE USER CONFIRMS THAT THE SELECTION IS INCORRECT, IT RESTARTS THE PROGRAM
  else: 
    project_program()



project_program()

