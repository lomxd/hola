def verificar_mayor_edad():
    #verifica la edad del usuario
    edad = int(input("porfavor,ingresa tu edad: "))
    if edad >= 18:
        print("eres mayor de edad")
    else:
        print("eres menor de edad")  
    
def validar_usuario_contraseña():
    #valida las credenciales del usuario
    usuarios ={
        "francisco": "1234",
        "agustin":"a4s1"
    }   
    
    while True:
        usuario = input ("ingresa tu nombre de usuario: ")
        contraseña = input("ingresa tu contraseña: ") 
        if usuario in usuarios and usuarios[usuario] == contraseña:
            print("acceso concedido!")
            break
        else:
            print("usuario o contraseña incorrectos. intentalo nuevamente.")
        
def calcular_promedio_notas():
    # calcula el promedio de tres notas
    notas = []
    for i in range(3):
        nota = float(input(f"ingresa la nota{i + 1}: "))
        notas.append(nota)
        
    promedio = sum(notas) / len(notas) 
    print(f"el promedio de tus 3 notas es: {promedio: .2f}")
    
    if promedio >= 4.0:
        print("aprobado")
    else:
        print("reprobado")
        
def preguntar_sobre_animales():
    #pregunta de los animales
    print("¿cual de los siguientes animales vive en el agua?")
    print("1.perro")
    print("2. cocodrilo")
    print("3. conejo")
    print("4.tiburon")
    
    respuesta = input("elige una opcion (1-4):")
    puntaje = 0
    
    if respuesta == "2":
        puntaje += 0.5
    elif respuesta =="4":
        puntaje += 1.0
    print(f"puntaje obtenido: {puntaje}")
    
def formulario_preguntas():
    #formulario con tres preguntas
    preguntas = [
        {
            "pregunta": "¿en que serie aparece walter white?",
            "respuesta": ["a)breaking bad", "b) the office", "c) game of thrones", "d) dexter"],
            "correcta": "a"
        },
        {
            "pregunta": "¿cual serie sigue a unos niños enfrentandp lo sobrenatural?",
            "respuestas": ["a) stranger things", "b) the walking dead", "c) lost", "d) dexter"],
            "correcto": "a"
        },
        {
            "pregunta": "¿cual serie es una comedia ambientada en una oficina de papel?",
            "respuestas": ["a) thebig ban theory", "b) the office", "c) parks anda recreation", "d) how i met your mother"],
            "correcta": "b"      
        }
    ]
    
    puntaje_total = 0
    
    # recorre las preguntas
    for pregunta in preguntas:
        print(pregunta["pregunta"])
        for respuesta in pregunta["respuestas"]:
            print(respuesta)
            
        respuesta_usuario = input("eliige una opcion (a, b, c, d): ").strip().lower()
        if respuesta_usuario == pregunta["correcta"]:
            puntaje_total += 1
    print(f"\npuntaje total: {puntaje_total}")
    
    # asignar nota segun el puntaje total
    if puntaje_total == 3:
        print("nota: a (excelente)")
    elif puntaje_total == 2:
        print("nota: b (bueno)")
    elif puntaje_total == 1:
        print("nota: c (regular)")
    else:
        print("nota: d(insatisfactorio)")
        
def main():
    # verificar la mayoria de edad
    print("\n--- verificar si es mayor de edad ---")
    verificar_mayor_edad()
    
    #validar usuario y contraseña
    print("\n--- validacion de usuario y contraseña ---")
    validar_usuario_contraseña()
    
    # calcular el promedio de 3 notas
    print("\n--- calcular el promedio de 3 notas ---")
    calcular_promedio_notas()
    
    #PREGUNTAR SOBRE animales
    print("\n--- pregunta sobre animales ---")
    preguntar_sobre_animales()
    
    #presentar f0rmulario de preguntas
    print("\n--- formulario de preguntas ---")
    
 #ejecutar la funcion main
if __name__ == "__main__":
    main()
    