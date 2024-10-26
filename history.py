import random 

# funcao que gera a introducao da historia 
def gerar_introducao() :
    introducoes = ["Era uma vez", " ha muito tempo atras", " num reino distante"]
    return random.choice(introducoes)

# funçao que gera o desenvolvimento da historia 
def gerar_desenvolvimento():
    desenvolvimentos =["Um valente cavaleiro","uma destemida guerreira", "um bravo guerreiro", "uma poderosa feiticeira", "um sabio mago"]
    return random.choice(desenvolvimentos)

# Função que gera o final da história
def gerar_final():
    finais = ["enfrentando dragões ferozes.", "derrotando um terrível vilão.",
              "descobrindo um tesouro escondido.", "salvando o reino da escuridão.",
              "encontrando um amor verdadeiro."]
    return random.choice(finais)

# Função principal que gera toda a história
def gerar_historia():
    introducao = gerar_introducao()
    desenvolvimento = gerar_desenvolvimento()
    final = gerar_final()

    historia = f"{introducao} {desenvolvimento} {final}"
    return historia

# Exibe a história gerada
if __name__ == "__main__":
    print(gerar_historia())

