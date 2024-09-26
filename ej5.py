import re
# Buscar una palabra en una cadena
pattern = r'\bworld\b'
text = 'Hello, world!'
match = re.search(pattern, text)
if match:
    print("Se encontró la palabra world")