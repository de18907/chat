import os
class archivos:
    lista_archivos_chat = []
    dirs1 = os.listdir("chat/")#achivos del chat 
    for file_chat in dirs1:
        lista_archivos_chat.append(f"chat/{file_chat}")   