ARQUIVO = "biblio.txt"

def adicionarLivro(livro):
    try:
        with open(ARQUIVO, "a", encoding="utf-8") as arq:
            arq.write(f"{livro['nome']};{livro['autor']};{livro['genero']};{livro['disponibilidade']}\n")
    except Exception as e:
        print(f"Erro indefinido ao localizar arquivo - {e}")
    else:
        print("Livro cadastrado com sucesso!")
        
def listarLivros():
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as arq:
            livros = arq.readlines()
            return [eval(linha.strip()) for linha in livros]
    
    except FileNotFoundError:
        print("Arquivo não encontrado.")
        return []
    except Exception as e:
        print(f"Erro ao carregar livros: {e}")
        return []
    
def salvar_livros(livros):
    try:
        with open(ARQUIVO, "w", encoding="utf-8") as f:
            for livro in livros:
                f.write(str(livro) + "\n")
    except Exception as e:
        print(f"⚠️ Erro ao salvar livros: {e}")
        
def mostrarLivros():
    livros = listarLivros()
    if not livros:
        print("Nenhuma livro cadastrado ainda.")
    else:
        print("\n--- Pessoas Cadastradas ---")
        for i, linha in enumerate(livros, 1):
            nome, autor, genero, disponibilidade = linha.strip().split(";")
            print(f"{i}. Nome: {nome} | Autor: {autor} | Genero: {genero} | Disponibilidade: {disponibilidade}")
            
def limparLivros():
    with open(ARQUIVO, "w", encoding="utf-8") as arq:
        arq.write("")
                    
def removerLivro():
    
    lista = listarLivros()
    mostrarLivros()
    selecao = int(input("Digite o numero do livro a ser removido: "))
    nome, autor, genero, disponibilidade = lista[selecao-1].strip().split(";")           
    dicLivro = {
        "nome" : nome,
        "autor" : autor,
        "genero" : genero,
        "disponibilidade" : disponibilidade
    }
    
    if (dicLivro["disponibilidade"] == "alugado"):
        print(f"Não é possivel excluir o livro {dicLivro["nome"]}, o mesmo esta {dicLivro["disponibilidade"]}")
        return
    
    
    lista.pop(selecao-1)
    limparLivros()
    print("aqui")
    for livro in lista:
        nome, autor, genero, disponibilidade = livro.strip().split(";")           
        dicLivro = {
            "nome" : nome,
            "autor" : autor,
            "genero" : genero,
            "disponibilidade" : disponibilidade
        }
        print(livro)
        continue
        adicionarLivro(dicLivro)
    mostrarLivros()