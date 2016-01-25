
while True:
    print 'You find yourself inside a small house.'
    print 'In front of you is a small box. What do you do?'
    print '1: Open the box ' 
    print '2: Leave the house'
    s = int(raw_input('-->'))
    if s == 1:
        print 'Inside the box you find a magic cookie.'
        print 'You win the game!'
        break
    elif s == 2:
        print 'You walk away and never come back.'
        break
    else:
        print 'You cannot do that.'


