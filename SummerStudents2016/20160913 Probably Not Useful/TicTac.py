from LEDsetup import*

print'Welcome to Python TicTacToe.'
Color1=raw_input('player 1 pick your Color: blue = x, red = c, green = z. ')
if Color1=='x':
    print 'You have chosen Blue as your color.'
    
elif Color1=='c':
    print 'you have chosen Red as your color.'
elif Color1=='z':
    print 'You have chosen Green as your color.'
else:
    print 'Your color is Red.'
Color2=raw_input('Player 2 Pick your Color:  ')
if  Color2==Color1:
    Color2=raw_input('Pick another color:')
if Color2=='x':
    print 'You have chosen Blue as your color.'
elif Color2=='c':
    print 'You have chosen red as your color.'
elif Color2=='z':
    print 'You have chosen Green as your color.'
else:
    print 'Your color is Green.'



