#Name: Sam Smallwood
#email: smallwse@mail.uc.edu
#Assignment Title: Final Project
#Due Date: 20231207
#Course: IS 4010
#Semester/Year: Fall 2023
#Brief Description: This module contains the function that displays our group photo at the baseball field
#Citations:
#Anything else that's relevant:

from PIL import Image

def displayPhoto():
    '''
    Displays the photo we took on the baseball field
    @return: None
    '''
    Image.open('baseball.jpg').show()