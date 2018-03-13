def funcion(*args):
    text=""
    for x in args:
        text=text+str(x)
    return text
        
print(funcion(2,3,5,5,1,2,3))

def quitaresp(args):
    text=args
    cont=0
    for x in text:
        if(x==' '):
            text=text[0:cont]+text[cont+1:]
            cont-=1
        cont+=1
    return text

print(quitaresp("Ho l      a mundo   pru  e va       un      o  "))
               

 