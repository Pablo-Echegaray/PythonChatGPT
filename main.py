import openai
import config

openai.api_key = config.API_KEY

# Contexto del asistente
messages = [{"role":"system", "content":"Eres un asistente muy útil."}]

while True:

    content = input("¿Sobre qué quieres hablar?")
    
    if content == "exit":
        break
    
    # Contexto de la pregunta realizada
    messages.append({"role":"user", "content":content})
    
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                 messages=messages)
    
    # Contexto de la respuesta devuelta
    response_content = response.choice[0].message.content
    
    messages.append({"role": "assistant", "content": response_content})
    
    print(response_content)
    
    # Guardando el contexto de la pregunta y la respuesta, podemos lograr una conversación fluida.