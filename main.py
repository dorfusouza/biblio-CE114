from funcoes import adicionarLivro, mostrarLivros, removerLivro

def menu():
    while True:
        print("\n=== Sistema de Cadastro ===")
        print("1 - Cadastrar novo livro")
        print("2 - Remover um livro cadastrado")
        print("9 - Listar livros cadastradas")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            livro = {
                "nome" : input("Digite o nome: ").strip(),
                "autor" : input("Digite o autor: ").strip(),
                "genero" : input("Digite o genero: ").strip(),
                "disponibilidade" : "disponivel"
            }
            
            adicionarLivro(livro)
        elif opcao == "2":
            removerLivro()
        elif opcao == "9":
            mostrarLivros()
        elif opcao == "0":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida! Tente novamente.")

menu()
