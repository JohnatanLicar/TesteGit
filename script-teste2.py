arquivo = open('número.txt', 'r')
for linha in arquivo.readlines():
    print(linha.rstrip())
arquivo.close()
