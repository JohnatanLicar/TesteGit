arquivo = open('número.txt', 'w')
for linha in range(1, 101):
    arquivo.write(f'\n{linha}')
arquivo.close()
