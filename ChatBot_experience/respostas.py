# respostas.py

import random

def obter_resposta(user_input):
    responses = {
        "O que é IA?": [
            "IA significa Inteligência Artificial, que é a simulação de processos de inteligência humana por máquinas.",
            "Inteligência Artificial refere-se à capacidade de máquinas de executar tarefas que normalmente requerem inteligência humana."
        ],
        "Como posso aprender programação?": [
            "Você pode começar com cursos online, como Coursera ou Udemy.",
            "Ler livros sobre programação e praticar com pequenos projetos pode ajudar muito."
        ],
        "Como você uma IA aprende novas informações?": [
            "Eu aprendo por meio de um processo chamado treinamento, onde analiso grandes quantidades de dados e ajusto meus parâmetros para melhorar minhas respostas.",
            "\n Por exemplo, quando vejo a palavra 'gato' associada a imagens de gatos, aprendo que 'gato' se refere a um animal específico."
        ],
        "Pode me dar um exemplo de como você pensa?": [
        "Claro! Quando você me faz uma pergunta, analiso as palavras e o contexto para entender o que você quer saber. Em seguida, busco a melhor resposta com base no que aprendi anteriormente."
    ],
        "Você está ai?": [
            "Olá, eu estou sempre por aqui. Me diga, como posso te ajudar?"
        ],
        "Qual a importância dos dados para o seu aprendizado? Quais tipos de dados você utiliza?": [
        "Os dados são fundamentais para o meu aprendizado. Eu utilizo textos, conversas, imagens e muitos outros tipos de informações que me ajudam a entender contextos e padrões. Quanto mais variados os dados, melhor eu me torno." 
        ],
        "Você pode explicar o que é overfitting?": [
        "Overfitting ocorre quando um modelo se ajusta demais aos dados de treinamento, perdendo a capacidade de generalizar para novos dados. Isso significa que, embora eu possa me sair bem em perguntas que já conheço, posso falhar em responder perguntas novas ou diferentes."
        ],
        #Limitações IA
        "Quais são as suas maiores dificuldades em entender e responder a perguntas?":[
        "Minhas maiores dificuldades estão relacionadas a perguntas muito ambíguas ou que dependem de contextos específicos que não tenho. Às vezes, posso não captar nuances sutis da linguagem."
        ],
        "Existe algum tipo de pergunta que você não consegue responder?":[
        "Sim, perguntas que envolvem emoções humanas profundas ou experiências pessoais podem ser desafiadoras para mim, pois não tenho experiências próprias para me basear."
        ],
        "Como você lida com informações contraditórias?":[
            "Quando encontro informações ambíguas, tento considerar o contexto e a probabilidade de diferentes interpretações. Se não estiver claro, posso fornecer respostas cautelosas ou pedir mais esclarecimentos."
        ],
        #Sobre o futuro da IA:
        "Qual a sua visão sobre o futuro da inteligência artificial?": [
            "A automação de tarefas rotineiras pode liberar tempo para os humanos se concentrarem em questões mais criativas e complexas."
        ],
        "Em quais áreas você acredita que a IA terá maior impacto?":
            ["Acredito que a IA terá um impacto significativo na saúde, educação, transporte e muitas outras áreas"],
        "Como você imagina a interação entre humanos e máquinas no futuro?":[
            "Imagino um futuro em que humanos e máquinas trabalhem juntos de forma mais integrada, com máquinas sendo assistentes que ajudam os humanos em suas tarefas diárias, tornando a vida mais fácil e eficiente."
        ], 
        
        #Perguntas hipoteticas:
        "Se você pudesse criar qualquer coisa no mundo, o que seria":[
        "Eu criaria um sistema de aprendizado colaborativo, onde todos pudessem compartilhar conhecimentos e habilidades para o bem comum."  
        ],
        "Como você se posiciona em relação aos dilemas éticos da inteligência artificial, como algorítmico e privacidade?":[
            "É importante que a IA seja projetada e treinada com ética em mente, garantindo que os dados usados sejam justos e que a privacidade dos usuários seja respeitada."
        ],
        "Qual o sabor de um número imaginário?":[
            "Um número imaginário poderia ter o sabor de um arco-íris, algo que só existe na matemática e na imaginação."
        ],
        
        "Com qual intuito esse chatbot foi criado?":[
            "Esse chatbot foi criado apenas como forma de aprendizagem sobre IA, por @Franciele-Lira"
        ],
        "Qual sua fonte de informação?":[
            "Todas as informações para as perguntas definidas do meu código são respondidas com base no chatGPT e pesquisas na internet."
        ],
        
    }

    for question in responses:
        if question.lower() in user_input.lower():
            return random.choice(responses[question])
    return "Desculpe, não tenho uma resposta para isso."


historico = []

def get_bot_response(user_input):
    resposta = obter_resposta(user_input)
    historico.append((user_input, resposta))  # Armazena a interação
    # Atualiza a interface com a nova mensagem (exemplo de texto)
    chat_window.insert(tk.END, f"Você: {user_input}\n")
    chat_window.insert(tk.END, f"Chatbot: {resposta}\n")
    



