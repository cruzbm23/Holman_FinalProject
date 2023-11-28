import json

def decryptLocation(team):
    '''
    Decrypts the location clue for a team
    @param team: the team that the clue belongs to
    @return: decrypted text containing the location clue
    '''
    with open('EncryptedGroupHints Fall 2023 Section 001.json') as f:
        encrypted = json.load(f)[team]
    
    with open('english-2.txt', 'r') as f:
        english = f.read().split('\n')
        
    decrypted = ' '.join([english[int(index)] for index in encrypted])
    return decrypted[0].upper() + decrypted[1:]
