# -~-~-~-~-~-~-~-~- Manipulando Textos ~-~-~-~-~-~-~-~-
# 
#   frase = 'ESTOU APRENDENDO A PROGRAMAR EM PYHTON'
# 
#   frase[9] ------> Pega os caracteres das posições indicadas ------------------- letra E
#   frase[9:13] -> Pega os caracteres das posições indicadas ------------------- ENDE
#   frase[9:18:2]--> Pega os caracteres das posições indicadas pulando 2 - EDNOA
#   len() -------------> Mostra quantas letras tem a frase -------------------------------- len(frase) = 38 letras
#   count() ---------> Conta quantas vezes aparece a letra escolhida ----------- frase.count('s')
#   find() ------------> Procura os caracteres escolhido ---------------------------------- frase.find('aprendendo')
#   replace() ------> Troca uma palavra por outra na frase --------------------------- frase.replace('python','JavaScript')
#   upper() ---------> Colocar todas as outras letras em maiúsculo -------------- frase.upper()
#   lower() ---------> Colocar todas as outras letras em minusculo -------------- frase.lower()
#   capilalize() ---> Coloca todas a frase em minusculo menos a 1 letra --- frase.capitalize()
#   title() ------------> Todas as palavras começa com letra maiúscula --------- frase.title()
#   strip() -----------> Tira o espaço do começo e no fim da frase ----------------- frase.strip()  frase.lstrip()  frase.rstrip()
#   split() -----------> Vai ocorrer uma divisão entre os espaços da frase ----- frase.split()
#   .join() -----------> Juntar uma coisa com a outra -------------------------------------- '-'.join.frase Estou-aprendendo-a-programar-em-python
# 
# -~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-

frase = 'Aprendendo Python'
print(frase[1:9])
print(len(frase))
print(frase.count('o'))
print(frase.find('e'))
print(frase.replace('Python','Android'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
print(frase.strip())
print(frase.split())
print(frase.join('em casa'))