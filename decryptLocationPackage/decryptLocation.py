# Name: Stewary Hamilton (Holman)
# email: hamiltsw@mail.uc.edu
# Assignment Title: Assignment Final Project
# Due Date: 20231207
# Course: IS 4010
# Semester/Year: Fall 2023
# Brief Description: Decrypts the location clue for a team
# Citations: 
# Anything else that's relevant: 

import json

def decryptLocation():
    '''
    Decrypts and prints the location clue for a team (Holman)
    @return: None
    '''
    
    team = 'Holman'
    
    with open('EncryptedGroupHints Fall 2023 Section 001.json') as f:
        encrypted = json.load(f)[team]
    
    with open('english-2.txt', 'r') as f:
        english = f.read().split('\n')
        
    decrypted = ' '.join([english[int(index)] for index in encrypted])
    print(decrypted[0].upper() + decrypted[1:])

