from ahorcado import*

def test_cargar_palabras(palabras:List[str])->None:
    print(f"Palabras cargadas: {len(palabras)}")
    print(f"Primeras tres palabras: {palabras[:3]}")
    print(f"Últimas tres palabras: {palabras[-3:]}")

def test_elegir_palabra(palabras:List[str])->None:
    palabra=elegir_palabra(palabras)
    print(f"Palabra elegida: {palabra}")

def test_enmascarar_palabra(palabra:str,letras:set)->None:
    enmascarada=enmascarar_palabra(palabra,letras)
    print(enmascarada)

def test_pedir_letra(letras:set)->None:
    nuevo_letras,letra=pedir_letra(letras)

def test_comprobar_letra(palabra:str,letra:str)->None:
    res=comprobar_letra(palabra,letra)
    if res==True:
        print('¡Bien hecho! Esa letra está en la palabra.')
    elif res==False:
        print('Lo siento, esa letra no está en la palabra.')

def test_comprobar_palabra_completa(palabra:str,letras:set)->None:
    res=comprobar_palabra_completa(palabra,letras)
    if res==True:
        print('Completa')
    elif res==False:
        print('Incompleta')

def test_ejecutar_turno(palabra:str,letras:set)->None:
    tupla=ejecutar_turno(palabra,letras)
    if tupla[0]==True:
        print('¡Bien hecho! Esa letra está en la palabra.')
    elif tupla[0]==False:
        print('Lo siento, esa letra no está en la palabra.')

if __name__=='__main__':
    palabras=cargar_palabras('data/palabras_ahorcado.txt')
    #test_cargar_palabras(palabras)
    #test_elegir_palabra(palabras)
    #print('Testeando enmascarar_palabra() con la palabra python y las letras ()...')
    #test_enmascarar_palabra('python',{})
    #print('Testeando enmascarar_palabra() con la palabra python y las letras (p,y,o,t,h,n)...')
    #test_enmascarar_palabra('python',{'p','y','o','t','h','n'})
    #print('Testeando enmascarar_palabra() con la palabra python y las letras (e,b,d,a,c)...')
    #test_enmascarar_palabra('python',{'e','b','d','a','c'})
    #print('Testeando enmascarar_palabra() con la palabra python y las letras (e,u,o,i,a)...')
    #test_enmascarar_palabra('python',{'e','u','o','i','a'})
    #print('Testeando pedir_letra() con las letras (c,a,b)...')
    #test_pedir_letra({'c','a','b'})
    #print('Testeando comprobar_letra() con la palabra python y la letra p...')
    #test_comprobar_letra('python','p')
    #print('Testeando comprobar_letra() con la palabra python y la letra a...')
    #test_comprobar_letra('python','a')
    #print('Testeando comprobar_palabra_completa() con la palabra python y las letras (y,o,t,h,p,n)...')
    #test_comprobar_palabra_completa('python',{'y','o','t','h','p','n'})
    #print('Testeando comprobar_palabra_completa() con la palabra python y las letras (c,e,b,d,a)...')
    #test_comprobar_palabra_completa('python',{'c','e','b','d','a'})
    #print('Testeando comprobar_palabra_completa() con la palabra python y las letras ()...')
    #test_comprobar_palabra_completa('python',{})
    #print('Testeando ejecutar_turno() con la palabra python y las letras (d,c,b,a,e)...')
    #test_ejecutar_turno('python',{'d','c','b','a','e'})
    #print('Testeando ejecutar_turno() con la palabra python y las letras (p,o,t,y,h)...')
    #test_ejecutar_turno('python',{'p','o','t','y','h'})
    jugar(6,palabras)