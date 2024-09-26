import argparse
# Creación del parser
parser = argparse.ArgumentParser (description= 'Ejemplo con argparse')
# Añadir un argumento
parser.add_argument('name', type=str, help='Tu nombre')
# Parsear los argumentos
args = parser.parse_args()
# Usar los argumentos
print(f'Hola {args.name}')