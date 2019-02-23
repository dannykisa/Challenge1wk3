def list_sort(w):

    character = []
    odds = []
    evens = []
    mydict = dict()
    if not isinstance(w, list):
        return 'Invalid Input'

    if not w:
        
        mydict['chars'] = character
        mydict['odds'] = odds
        mydict['evens'] = evens
        return mydict

    for k in w:

        if isinstance(k, int):
            if k % 2 == 0:
                evens.append(k)
            
            else:
                odds.append(k)

        elif isinstance(k, str):
            character.append(k)

    mydict['chars'] = sorted(character)
    mydict['odds'] = sorted(odds)
    mydict['evens'] = sorted(evens)
    return mydict


print(list_sort([4, 8, 9, 5, 'p']))