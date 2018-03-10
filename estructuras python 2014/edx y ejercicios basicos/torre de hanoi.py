

def printMove(fr, to,):
    print('mueve desde ' + str(fr) + ' a ' + str(to))

def Towers(n, fr, to, spare):
    if n == 1:
        printMove(fr, to)
    else:
        Towers(n-1, fr, spare, to)
        Towers(1, fr, to, spare)
        Towers(n-1, spare, to, fr)
    
Towers(3,"inicio","objetivo","auxiliar")