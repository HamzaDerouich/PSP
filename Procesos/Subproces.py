import subprocess

a = subprocess.Popen("dir",stdout=subprocess.PIPE, stdin =subprocess.PIPE, stderr=subprocess.PIPE,shell=True)
salida = a.stdout.read()
error = a.stderr.read()

a.wait()

print(salida.decode("latin1"))
print(error)