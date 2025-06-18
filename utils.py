import os

def nome_sem_extensao(caminho):
    return os.path.splitext(os.path.basename(caminho))[0]

