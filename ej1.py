import subprocess
# Ejecutar el comando 'echo' usando el shell
result = subprocess.run('echo Hello, World!', capture_output=True, text=True, shell=True)
# Imprimir el resultado
print(result.stdout)