logo = ''' 
    _    _
   | |  | |
   | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
   |  __  |/ _' | '_ \ / _' | '_ ' _ \ / _' | '_  \\
   | |  | | (_| | | | | (_| | | | | | | (_| | | | |
   |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        __/ |
                       |___/           
                        '''

lev1 = ''' 

     /_______________
    /             |
    |             |
    |
    |
    |
    |
    |
    |
    |
    |
    |________________________
    '''
lev2 = ''' 

     /_______________
    /             |
    |             |
    |           |0 0|
    |           |(=)|
    |          
    |
    |
    |
    |
    |
    |________________________
    '''
lev3 = ''' 
     /_______________
    /             |
    |             |
    |           |0 0|
    |           |(=)|
    |          /     \\
    |          |     |
    |          |_____|
    |
    |
    |
    |________________________
    '''
lev4 = ''' 
     /_______________
    /             |
    |             |
    |           |0 0|
    |           |(=)|
    |          /      \\\\
    |          |     | \\\\
    |          |_____|  \\\\
    |
    |
    |    
    |________________________
    '''
lev5 = ''' 
     /_______________
    /             |
    |             |
    |           |0 0|
    |           |(=)|
    |         //     \\\\
    |        //|     |\\\\
    |       // |_____| \\\\
    |
    |
    |
    |________________________
    '''
lev6 = ''' 
     /_______________
    /             |
    |             |
    |           |0 0|
    |           |(=)|
    |         //     \\\\
    |        //|     |\\\\
    |       // |_____| \\\\
    |          | |
    |          | |
    |          |_|
    |________________________
    '''

lev7 = ''' 
     /_______________
    /             |
    |             |
    |           |0 0|
    |           |(=)|
    |         //     \\\\
    |        //|     |\\\\
    |       // |_____| \\\\
    |          | | | |  
    |          | | | |
    |          |_| |_|
    |________________________
    '''
GameBored = '''
Please enter a word: hangman



_ _ _ _ _ _ _
'''
print(logo)
print(GameBored)
leter = input("Guess a letter:")
leter = leter.lower()
# harta = [ '!'  '@'  '#'  '$'  '%'  '^'  '&'  '*'  '('  ')' ]

if leter[1::]:
    if leter == ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']:
        print("E3")
    else:
        print("E1")
elif leter in ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']:
    print("E2")
else:
    print(leter)
