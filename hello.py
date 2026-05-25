"""
Este é um hello world multilínguas. Dependendo do idioma, ele imprime hello world no idioma do computador
"""

__version__ = "0.0.1"
__author__ = "Matheus"
__license__ = "Unlicense"

#Dunder = Double underline.

import os

if __name__ == "__main__":
    current_language = os.getenv("LANG","en_US")[:5]
    #snake case = padrão de nomenclatura onde as palavras são separadas por underline e todas as letras são minúsculas. Ex: current_language, hello_world, etc.
    msg = "Hello world!"

    if current_language == "de_DE":
        msg = "Hallo Welt!"
    elif current_language == "it_IT":
        msg = "Ciao, mondo!"
    elif current_language == "pt_BR":
        msg = "Olá, mundo!"

    print(msg)

    