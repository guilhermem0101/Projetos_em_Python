import string

# Define uma função para limpar o texto removendo pontuações e espaços em branco
def limpar_texto(texto):
    texto = texto.translate(str.maketrans('', '', string.punctuation)) # remove pontuações
    texto = texto.lower() # transforma em minúsculo
    texto = ' '.join(texto.split()) # remove espaços em branco extras
    return texto

# Abre o arquivo de texto
with open('texto.txt', 'r') as arquivo:
    conteudo = arquivo.read()

# Limpa o conteúdo do arquivo
conteudo_limpo = limpar_texto(conteudo)

# Divide o texto em palavras e conta a frequência de cada palavra
palavras = conteudo_limpo.split()
frequencias = {}
for palavra in palavras:
    if palavra in frequencias:
        frequencias[palavra] += 1
    else:
        frequencias[palavra] = 1

# Cria um ranking das palavras mais frequentes
ranking = sorted(frequencias.items(), key=lambda x: x[1], reverse=True)

# Exibe o ranking
print('Ranking de palavras:')
for i, (palavra, frequencia) in enumerate(ranking):
    print(f'{i+1}. {palavra}: {frequencia} ocorrências')
