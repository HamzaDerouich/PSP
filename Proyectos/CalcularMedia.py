def CalcularNotas():
    try:
        numero_notas = int(input("Ingrese el número de notas que desas ingresar: "))
        notas = []
        i = 0
        while( i < numero_notas):
            nota = int(input("Ingrese la nota: "))
            notas.append(nota)
            i += 1
        suma = 0
        for j in notas:
            suma += j
        print(f"\nNotas ingresadas ( {notas} )" + f"\nMedia de las notas {suma / len(notas)}")    
    except ValueError:
        print("Datos no validos!!")    
        
CalcularNotas()