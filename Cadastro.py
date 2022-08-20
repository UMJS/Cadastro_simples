codigo_livro = int(1000)

def cadastrar_livro():
    livro = []
    codigo = codigo_livro

    nome = input("O nome dos autores da obra: ")
    autor = input("O nome da obra: ")
    editora = input("O nome da editora: ")
    livro.append(codigo)
    livro.append(nome)
    livro.append(autor)
    livro.append(editora)
    return livro

def mostrar_livros(livros):
    for livro in livros:
        print(livro)

lista_livros = []
qtd_livro_inseridos = int(0)

while True:

    menu = input("Escolha um opção do menu: 1.CADASTRO   2.PESQUISA  0.ENCERRAR \n")


    #gato no codigo
    if menu == "0" or menu == "1" or menu == "2":
        menu = int(menu)

    if menu == 1:
        if qtd_livro_inseridos > 4:
            print("Sistema de cadastro lotado. Não é possível armazenar mais informações!")
            continue
        livro = cadastrar_livro()
        lista_livros.append(livro)
        qtd_livro_inseridos += 1
        codigo_livro += 1


    elif menu == 2:
        if len(lista_livros) == 0:
            print("Lista vazia!")
            continue

        mostrar_livros(lista_livros)


    elif menu == 0:
        break

    else:
        print(" Erro: opção inválida! ")
