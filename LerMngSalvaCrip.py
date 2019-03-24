mensagem = open('mensagem.txt', 'r')
for c in mensagem.readlines():
    print(c)
mensagem.close()
