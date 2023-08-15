def whos_first(p1, p2):
    # ваше решение
    lenn = p1.find('B') - p2.find('B')
    if lenn<0:
        return 'p1'
    elif lenn>0:
        return 'p2'
    else: 
        return 'tie'

print(whos_first( "    Bang!        ","        Bang!   "))
    
