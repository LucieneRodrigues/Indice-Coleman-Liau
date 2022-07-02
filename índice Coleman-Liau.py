''' índice Coleman-Liau / O índice Coleman-Liau de um texto é projetado para mostrar qual nível escolar nos (EUA)
é necessário para entender o texto.
Fórmula: L = Letras ÷ Palavras × 100
         S = Frases ÷ Palavras × 100 '''

texto = str(input('Digite o texto:')).upper().strip()
lista = texto.split()
len(''.join(lista))
p = 0
let0 = list()
let1 = list()
let2 = list()
excluir = texto.count('!') + texto.count('.') + texto.count('?') + texto.count(':') + texto.count('-') + texto.count('(') + texto.count(')') + texto.count('"') + texto.count(';') + texto.count(',') + texto.count("'")
for i, l in enumerate(lista):
    p = len(lista) # quant palavas     
    if l.count('!') > 0:
        let0.append(l[-1].count('!'))
    elif l.count('?') > 0:
        let1.append(l[-1].count('?'))
    elif l.count('.') > 0:
        let2.append(l[-1].count('.'))
s0 = 0
for i, v in enumerate(let0):
    s0 = s0 + v
s1 = 0
for i, v in enumerate(let1):
    s1 = s1 + v
s2 = 0
for i, v in enumerate(let2):
    s2 = s2 + v
s = s0 + s1 + s2 # setença
 
letra = len(''.join(lista)) - excluir

l =letra /p * 100
s1 =s / p *100 

indice = 0.0588 * l - 0.296 * s1 - 15.8
grade = round(indice)
if grade < 1:
    print('Before Grade 1')

elif grade >= 2 and grade < 2.5:
    print('Grade 2')
    
elif grade > 2.5 and grade < 3.5:
    print('Grade 3')

elif grade > 3.5 and grade < 5.5:
    print('Grade 5')
    
elif grade > 5.5 and grade < 7.5:
    print('Grade 7')
    
elif grade > 7.5 and grade < 8.5:
    print('Grade 8')

elif grade > 8.5 and grade < 9.5:
    print('Grade 9')
    
elif grade > 9.5 and grade < 16:
    print('Grade 10')
    
elif grade >= 16:
    print('Grade 16+')




   
    

    
