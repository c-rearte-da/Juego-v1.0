import random
print('*' * 68)
print('Dr. Sheldon Cooper, presenta: Piedra, Papel, Tijera, Lagarto, Spock.')
print('*' * 68)
opciones = ('piedra', 'papel', 'tijera', 'lagarto', 'spock')
contador_usuario = 0
contador_computadora = 0
contador_partidas = 0
nombre_usuario = input('Por favor ingrese su nombre =>')
partidas = int(input('Cuantas partidas quieres jugar? =>'))

while partidas % 2 == 0:
    print('Por favor digita una cantidad de partidas impar')
    partidas = int(input('Cuantas partidas quieres jugar? =>'))

while contador_partidas < partidas:
    contador_partidas += 1
    print('-' * 68)
    print('Partida numero = ', contador_partidas)
    print('-' * 68)
    eleccion_usuario = input('Digita tu opcion: piedra, papel, tijera, lagarto o spock =>')
    eleccion_usuario.lower()
    eleccion_computadora = random.choice(opciones)

    if not eleccion_usuario in opciones:
        print('Esa opcion no es valida')
        eleccion_usuario = input('Digita tu opcion: piedra, papel, tijera, lagarto o spock =>')
        eleccion_usuario.lower()

    print('Usted selecciono => ', eleccion_usuario)
    print('La computadora selecciono => ', eleccion_computadora)

    if eleccion_usuario == eleccion_computadora:
        print('Bazinga!! Fue un empate!!')
        print('Puntajes: ',nombre_usuario,' =>',contador_usuario,'Computadora =>',contador_computadora)
    elif eleccion_usuario == 'piedra':
        if eleccion_computadora == 'tijera':
            print('Piedra aplasta a tijera')
            print('Gana el usuario')
            contador_usuario += 1
            print('Puntajes: ',nombre_usuario,' =>',contador_usuario,'Computadora =>',contador_computadora)
        elif eleccion_computadora == 'papel':
            print('Papel tapa a piedra')
            print('Gana la computadora')
            contador_computadora += 1
            print('Puntajes: ',nombre_usuario,' =>',contador_usuario,'Computadora =>',contador_computadora)
        elif eleccion_computadora == 'lagarto':
            print('Piedra aplasta a lagarto')
            print('Gana el usuario')
            contador_usuario += 1
            print('Puntajes: ',nombre_usuario,' =>',contador_usuario,'Computadora =>',contador_computadora)
        else:
            print('Spock vaporiza la piedra')
            print('Gana la computadora')
            contador_computadora += 1
            print('Puntajes: ',nombre_usuario,' =>',contador_usuario,'Computadora =>',contador_computadora)
    elif eleccion_usuario == 'papel':
        if eleccion_computadora == 'tijera':
            print('Tijera corta papel')
            print('Gana la computadora')
            contador_computadora += 1
            print('Puntajes: ',nombre_usuario,' =>',contador_usuario,'Computadora =>',contador_computadora)
        elif eleccion_computadora == 'piedra':
            print('Papel tapa a piedra')
            print('Gana el usuario')
            contador_usuario += 1
            print('Puntajes: ',nombre_usuario,' =>',contador_usuario,'Computadora =>',contador_computadora)
        elif eleccion_computadora == 'lagarto':
            print('Lagarto devora papel')
            print('Gana la computadora')
            contador_computadora += 1
            print('Puntajes: ',nombre_usuario,' =>',contador_usuario,'Computadora =>',contador_computadora)
        else:
            print('Papel desautoriza a Spock')
            print('Gana el usuario')
            contador_usuario += 1
            print('Puntajes: ',nombre_usuario,' =>',contador_usuario,'Computadora =>',contador_computadora)
    elif eleccion_usuario == 'tijera':
        if eleccion_computadora == 'papel':
            print('Tijera corta papel')
            print('Gana el usuario')
            contador_usuario += 1
            print('Puntajes: ',nombre_usuario,' =>',contador_usuario,'Computadora =>',contador_computadora)
        elif eleccion_computadora == 'piedra':
            print('Piedra aplasta tijera')
            print('Gana la computadora')
            contador_computadora += 1
            print('Puntajes: ',nombre_usuario,' =>',contador_usuario,'Computadora =>',contador_computadora)
        elif eleccion_computadora == 'lagarto':
            print('Tijera decapita al lagarto')
            print('Gana el usuario')
            contador_usuario += 1
            print('Puntajes: ',nombre_usuario,' =>',contador_usuario,'Computadora =>',contador_computadora)
        else:
            print('Spock rompe tijera')
            print('Gana la computadora')
            contador_computadora += 1
            print('Puntajes: ',nombre_usuario,' =>',contador_usuario,'Computadora =>',contador_computadora)
    elif eleccion_usuario == 'lagarto':
        if eleccion_computadora == 'tijera':
            print('Tijera decapita al lagarto')
            print('Gana la computadora')
            contador_computadora += 1
            print('Puntajes: ',nombre_usuario,' =>',contador_usuario,'Computadora =>',contador_computadora)
        elif eleccion_computadora == 'piedra':
            print('Piedra aplasta al lagarto')
            print('Gana la computadora')
            contador_computadora += 1
            print('Puntajes: ',nombre_usuario,' =>',contador_usuario,'Computadora =>',contador_computadora)
        elif eleccion_computadora == 'papel':
            print('Lagarto devora papel')
            print('Gana el usuario')
            contador_usuario += 1
            print('Puntajes: ',nombre_usuario,' =>',contador_usuario,'Computadora =>',contador_computadora)
        else:
            print('Lagarto envenena a Spock')
            print('Gana el usuario')
            contador_usuario += 1
            print('Puntajes: ',nombre_usuario,' =>',contador_usuario,'Computadora =>',contador_computadora)
    elif eleccion_usuario == 'spock':
        if eleccion_computadora == 'tijera':
            print('Spock rompe tijera')
            print('Gana el usuario')
            contador_usuario += 1
            print('Puntajes: ',nombre_usuario,' =>',contador_usuario,'Computadora =>',contador_computadora)
        elif eleccion_computadora == 'piedra':
            print('Spock vaporiza la piedra')
            print('Gana el usuario')
            contador_usuario += 1
            print('Puntajes: ',nombre_usuario,' =>',contador_usuario,'Computadora =>',contador_computadora)
        elif eleccion_computadora == 'lagarto':
            print('Lagarto envenena a Spock')
            print('Gana la computadora')
            contador_computadora += 1
            print('Puntajes: ',nombre_usuario,' =>',contador_usuario,'Computadora =>',contador_computadora)
        else:
            print('Papel desautoriza a Spock')
            print('Gana la computadora')
            contador_computadora += 1
            print('Puntajes: ',nombre_usuario,' =>',contador_usuario,'Computadora =>',contador_computadora)

print('*' * 68)
print('Fin del juego')
if contador_computadora > contador_usuario:
    print('Computadora gano!!!')
elif contador_computadora == contador_usuario:
    print('Fue un empate')
else:
    print('Felicitaciones ',nombre_usuario,' gano!!!')
print('*' * 68)