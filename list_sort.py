w = [5, 4,'p', 6.4]

def list_sort(w):

    character = []
    odds = []
    evens = []
    mydict = dict()

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


print(list_sort([5, 4,'p', 6.4]))