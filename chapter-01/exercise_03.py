# Running timing

def run_timing():
    contador = 0
    tiempo_total = 0
    while True:
        tiempo_usuario = input("Enter 10 km run time: ")
        if tiempo_usuario == '':
            break
        tiempo_total += float(tiempo_usuario)
        contador += 1
    return f"Average of {tiempo_total/contador:.1f}, over {contador} runs."

print(run_timing())