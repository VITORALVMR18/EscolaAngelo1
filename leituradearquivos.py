with open('arquivo.txt', 'w') as arquivo:
    arquivo.write
    arquivo.write
    linhas = ['proxima linha', 'Outra linha']
    arquivo.writelines(linhas)

texto = "Aqui vai uma mensagem"
with open('arquivoswrite.teste', 'w') as arquivo:
    arquivo.write(texto)

arquivo = open('teste2.txt', 'w')
arquivo.write(texto)
arquivo.write("\nOutra linha\n")
arquivo.write("finalizando o texto.")
arquivo.close()