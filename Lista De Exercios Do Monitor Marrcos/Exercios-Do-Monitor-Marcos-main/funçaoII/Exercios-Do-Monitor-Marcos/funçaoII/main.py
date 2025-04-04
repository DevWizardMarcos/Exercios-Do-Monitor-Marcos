# filepath: c:\Users\pc\Desktop\Exercios-Do-Monitor-Marcos-main\Exercios-Do-Monitor-Marcos-main\funçaoII\main.py

def main():
    exercicios = {
        "Analisador de Textos": "Ferramenta que analisa um texto colado pelo usuário e retorna:\n- Número total de palavras\n- Palavras mais repetidas\n- Palavras únicas\n- Palavras-chave buscadas pelo usuário",
        "Calculadora de Divisão de Conta": "Calculadora para dividir uma conta entre amigos com:\n- Valor total\n- Número de pessoas\n- Percentual de gorjeta",
        "Gerador de Desculpas Criativas": "Gera desculpas criativas para atrasos, permitindo que o usuário escolha entre várias opções.",
        "Gerador de Planos de Estudos": "Gera um cronograma equilibrado por matéria com:\n- Lista de matérias\n- Tempo disponível por dia\n- Total de dias",
        "Recomendador de Filmes": "Recomenda filmes baseados no seu humor ou tempo.",
        "Simulador de Orçamento de Viagem": "Usuário informa:\n- País de destino\n- Dias de viagem\n- Orçamento total\n- Moeda original",
        "Assistente de Criação de Histórias Interativas": "Cria histórias interativas aleatórias, permitindo que o usuário participe da criação da narrativa.",
        "Tradutor de Emoções": "Converte sentimentos em mensagens automáticas, ajudando o usuário a expressar suas emoções de forma mais clara."
    }

    print("Exercícios Disponíveis:")
    for nome, descricao in exercicios.items():
        print(f"\n{nome}:\n{descricao}")

if __name__ == "__main__":
    main()