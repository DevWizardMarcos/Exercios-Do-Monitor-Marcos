# filepath: c:\Users\INFINITY SCHOOL\Desktop\Lista De Exercios Do Monitor Marrcos\For\main.py

print("Lista de Exercícios")

exercises = {
    "01": "Controle de Gastos Pessoais 💰 - O usuário insere seus gastos diários, e o programa calcula o total e avisa quando ultrapassa um orçamento definido.",
    "02": "Simulador de Relógio Pomodoro ⏳ - Um cronômetro para estudar/trabalhar por 25 minutos e descansar por 5 minutos, repetindo isso 4 vezes.",
    "03": "Checklist de Tarefas Diárias ✅ - O usuário adiciona tarefas a uma lista e marca conforme as conclui.",
    "05": "Organizador de Contatos Telefônicos 📞 - O usuário adiciona contatos e pode buscar um contato pelo nome.",
    "06": "Gerenciador de Hábitos 📊 - O usuário define hábitos que deseja manter (ex: 'Ler 10 páginas') e marca diariamente o progresso.",
    "07": "Simulador de Consumo de Combustível 🚗 - O usuário insere a distância percorrida e o consumo médio do carro, e o programa calcula quanto combustível foi gasto.",
    "08": "Simulador de Previsão de Economia 💵 - O usuário insere quanto economiza por mês e o programa mostra a evolução ao longo dos anos.",
    "09": "Calculadora de Gorjeta 🍽️ - O usuário insere o valor da conta e escolhe uma porcentagem de gorjeta.",
    "10": "Gerador de Nomes Aleatórios para Projetos 🎲 - O programa gera nomes criativos para projetos baseados em palavras aleatórias."
}

for key, description in exercises.items():
    print(f"{key}. {description}")