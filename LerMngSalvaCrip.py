mensagem = open('mensagem.txt', 'r')
crypto = open('crypto.txt', 'w')
for c in mensagem.readlines():
    for l in c:
        if l in 'aeiou':
            crypto.write('*')
        else:
            crypto.write(l)
mensagem.close()
crypto.close()
