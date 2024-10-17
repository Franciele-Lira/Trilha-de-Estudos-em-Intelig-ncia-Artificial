import tkinter as tk
from respostas import obter_resposta  # Importa a função de respostas

def send_message():
    user_input = entry.get()
    if user_input.lower() == 'sair':
        root.quit()
    
    chat_box.insert(tk.END, f"Você: {user_input}\n")
    
    response = obter_resposta(user_input)  # Chama a função de respostas
    chat_box.insert(tk.END, f"Chatbot: {response}\n")
    
    entry.delete(0, tk.END)  # Limpa a entrada de texto

# Mensagem de início
def mensagem_inicial():
    chat_box.insert(tk.END, "Chatbot: Olá, eu sou o Chatbot criado pela dev Franciele Lira, e minha função é apenas para fins de prática e estudo de inteligência artificial.\n É muito bom ter você por aqui, me faça uma pergunta sobre IA:\n Observação: As repostas da IA foi baseada nas respostas do chatGPT")

# Configuração da interface gráfica
root = tk.Tk()
root.title("Chatbot")

root.grid_rowconfigure(0, weight=1)  # Permite que a primeira linha se expanda
root.grid_columnconfigure(0, weight=1) 

chat_box = tk.Text(root, height=35, width=80)
chat_box.pack()

entry = tk.Entry(root, width=50)
entry.pack()

button = tk.Button(root, text="Enviar", command=send_message)
button.pack()

mensagem_inicial()  # Chama a função para mostrar a mensagem inicial

root.mainloop()
