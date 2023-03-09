import random

titulo = "Hola vijero, Bienvenido a una nueva a ventira para tu persojae espero te guste, \n" \
         "Empezemos!"
fin = "HAS COMPLETADO LA MISION CON EXITO, FELICIDADES."

numero_random = random.randint(1, 100)

#INICIO DEL JUEGO
print("\n" + titulo + "\n" + "-" * len(titulo) + "\n")

print("Te encuentras en el lejano oeste con tu compañero de viaje, ambos, se encontraban camino al pequeño \n"
      "pueblo de Tombstone para realizar una entrega de un cargamento de tabaco. Sin embargo, cuando llegaron\n"
      "a la entrada de pueblo, un grupo de vandidos los asaltaron y secuestraron. Confundido despiertas en una\n"
      "habitacion oscura, por la cual solo entra un haz de luz a travez de una pequeña ventana en la parte superior\n"
      "de la pared atras tuyo. Estas solo, y decides escapar de la celda para encontrar a tu compañero, así como el\n"
      "cargamento.\n")

opcion = input("Decides mira a tu alrededor con el fin de encontra algo que te ayude  a salir de tu celda,\n"
                     "encuentras un plato de comida viejo, podria ser de utilidad para salir de tu celda.\n"
                     "¿Deseas recoger el plato de comida? (S/N): \n")

if opcion == "S":
    print("Recogiste el plato de comida y comiste parte de el, despues de unos minutos te empiezas a sentir mal,\n"
          "pides ayuda de algun guardia que te pueda brindar ayuda, sin embargo, nadie contesta y nadie acude a tu\n"
          "rescate. Terminas mueriendo por una intoxicacion.\n")

    print("FIN DEL JUEGO, PERDISTE")
    exit()

else:
    print("Decides dejar el plato de comida, no te sirve de nada\n")

    opcion = input("No encontraste nada apartentemente util que te pueda ayudar a salir de tu celda, sin embargo,\n"
                  "despues de un minucioso analisis a la habitacion, encuentras una aguja, ¿Quieres recogerla? (S/N): \n")

    if opcion == "N":
        print("Dejaste la aguja en el suelo, sin embargo no encontraste nada que e pudiera ayudar a salir de la celda,\n"
              "decides dormir un poco. Sin embargo, cuando despiertas, te encuentras con el mismo grupo de bandidos que\n"
              "te encarcelaron, y estos deciden acabar con tu vida.\n")

        print("FIN DEL JUEGO, PERDISTE\n")
        exit()

    else:
        print("Recogiste la aguja, decides utilizarla para abrir la puerta de tu celda y sales de ella.\n")

print("Cuando sales de tu celda, te percatas que te encontrabas en una carcel subterranea con multiples presos, \n"
      "sin embargo no hay guardias vigilandola; de seguro era una antigua estacion de policia desmantelada, ahora, \n"
      "usada por los bandidos para sus propios fines. Caminas hasta el final del pasillo, y subes las escaleras \n"
      "para acceder a la planta superior y abres la puerta que da al piso de arriba. Ves los restos de la antigua \n"
      "estacion de policia, esta abandonada y repleta de bandidos, es seguro que esa estacion se convirtio en la \n"
      "base de operaciones de una banda criminal.\n")

opcion = input("Rapidamente te escondes y encuentras una escopeta con pocas municiones, piensas que tal vez\n"
               "puedes recoger la escopeta para asesinar a los bandidos y salir de la estacion, sin embargo tambien \n"
               "contemplas la idea de escabullirte sigilosamente por la puerta de atras y salir a buscar a tu compañero\n"
               "y a el cargamento de tabaco. ¿Qué decides  hacer? (COGER ESCOPETA/SALIR SIGILOSAMENTE): \n")

if opcion == "COGER ESCOPETA":
    print("Sin pensarlo recoges la escopeta y empiezas a asesinar unos cuantos bandidos para poder salir del \n"
          "lugar, sin embargo, no tomaste encuenta el hecho de que la escopeta no tenia suficientes balas para \n"
          "que pudieses eliminar a todos los bandidos, por ende, se te acaban las balas y mueres en medio del tiroteo.\n")
    print("FIN DEL JUEGO, PERDISTE\n")
    exit()

else:
    print("Decides dejar la escopeta y salir de la estacion, te diriges hacia el centro del pueblo para averiguar \n"
          "informacion de donde podria estar tu amigo y sobre la identidad de los criminales. Cuando llegas \n"
          "al centro del puieblo encuentras una taberna, un lugar donde sabes circula mucha informacion sobre diversos \n"
          "temas, decides entrar y preguntas por la banda de bandidos; todos se quedan anonadados y deciden ignorarte \n"
          "para no meterse en problemas con los criminales. Sin embargo, una persona se acerca a ti y te toma del \n"
          "hombro, es un hombre encapuchado, tú, precavido le preguntas su nombre....\n\n"
          "El encapuchado se quita su tunica y resulta ser...   tu compañero.\n\n"
          "Despues de escuchar cómo tu compañero logro escapar de los ladrones, te cuenta que los bandidos son una \n"
          "banda criminal que tomaron el control del pueblo hace yavarios años, se dedican a aterrorizar a sus \n"
          "habitantes y extorsionarlos para financiar su organización criminal. Tu compañero te dice que los bandidos \n"
          "tienen un resguardo donde almacenan todas sus riquezas y, que es allí, donde tienen el cargamento de tabaco que tenian \n"
          "que entregar a un viejo amigo de la zona. Tu y tu compañero concuerdan en que tienen que deshacerse de la \n"
          "banda de bandidos para salvar a los haitantes del pueblo y devolverles su hogar. Asi es como empiezan a \n"
          "idear un plan para recuperar el pueblo.\n")

print("El plan es el siguiente: Tu amigo y tu se tienen que dividir, uno tiene que ir a la estacion de policia para \n"
      "liberar a los demas presos con el fin de que estos se unan a su causa; el otro, tendra que adentrarse en el \n"
      "resguardo de los bandidos: el ayuntamiento. Asi, uno eiminara a los bandidos en su totalida mientras el otro \n"
      "les roba sus recursos. Tu amigo tiene algunas herramientas que te podrian ser de utilidad: \n")

#Inventario del personaje

opcion = input("¿Coges la capucha? (S/N): \n")
capucha = False
if opcion == "S":
    print("Cogiste la capucha.\n")
    capucha = True
else:
    print("No cogiste la capucha.\n")

opcion = input("¿Te llevas el rifle con municion? (S/N): \n")
rifle = False
if opcion == "S":
    print("Cogiste el rifle con municion.\n")
    rifle = True
else:
    print("No cogiste el rifle.\n")

opcion = input("¿Te llevas la dinamita? (S/N): \n")
dinamita = False
if opcion == "S":
    print("Cogiste la dinamita.\n")
    dinamita = True
else:
    print("No cogiste la dinamita.\n")

#Sigue con la historia

opcion = input("Bien, ahora tienes que esocoger que parte del plan quieres llevar a cabo: (ESTACION DE POLICIA/AYUNTAMIENTO)\n")

if opcion == "ESTACION DE POLICIA":
    opcion = input("Decides encargarte de salvar a los presos para que te ayuden a combatir a los bandidos. Te diriges \n"
                   "a la estacion de policia, base central de los bandidos, notas que puedes entrar por la parte de \n"
                   "atras en sigilo, o entrar por la puerta principal y armar un tiroteo. ¿Que decides hacer?\n"
                   "(SIGILO/TIROTEO): \n")

    if opcion == "TIROTEO" and rifle == False:
        print("Decides entrar por la parte principal, pero no tienes ningun arma con la cual defenderte, los bandidos \n"
              "te disparan y mueres.\n")

        print("FIN DEL JUEGO, PERDISTE.")
        exit()

    elif opcion == "TIROTEO" and rifle == True:
        print("Decides entrar armando un tiroteo, matas a algunos bandidos y logras llegar a la armeria.\n")

    elif opcion == "SIGILO" and capucha == False:
        print("Intentaste entrar con sigilo pero sin la capucha, los bandidos lograron reconocerte facilmente,\n"
              "Te atrapan y te matan.\n")
        print("FIN DEL JUEGO, PERDISTE")
        exit()

    elif opcion == "SIGILO" and capucha == True:
        print("Decides ponerte la capucha y entrar por la puerta de atras para dirigirte al la armeria")


    operacion = float(input("Cuando llegas a la armeria tienes que hallar la clave, la cual esta dada por la \n"
                       "siguiente operacion: {} * {}: \n".format(2, numero_random)))

    if operacion == 2 * numero_random:
        print("Logras hallar la clave, abres la armeria y sacas las suficientes armas para armar a los presos.\n")
        print("Bajas a las celdas, las abres y liberas a los presos, les das las armas, y, junto a \n"
              "ellos, matan a todos los bandidos y liberan la estacion de policia, acabaste con las fuerzas de \n"
              "los bandidos.\n")
        print("Bien hecho, despues de acabar con los bandidos te encuentras con tu compañero quien ya devolvio \n"
              "todos los objetos de valor y dinero a los habitantes del pueblo, asi como ya tienen en su poder \n"
              "el cargamento que tenian que entregar. Se dirigen a entregar el paquete y una vez entregado, los \n"
              "habitantes del pueblo deciden pagarles por haber liberado al pueblo de control criminal de la \n"
              "banda de bandidos.Tu y tu compañeron deciden abandonar el pueblo para asi dirigirse hacia la siguiente aventura.\n")

        print("\n" + fin + "\n" + "-" * len(fin) + "\n")
        exit()

    else:
        print("Se te acaba el tiempo y un bandido te sorprende y te dispara en la cabeza, mueres al instante.\n")
        print("FIN DEL JUEGO PERDISTE")
        exit()

if opcion == "AYUNTAMIENTO":
    opcion = input("Bien, escogiste la opcion de recuperar toda la riqueza del pueblo asi como el cargamento que tenian que \n"
          "entregar tu y tu compañero, asi que te diriges al ayuntamiento de la ciudad. Al llegar puedes entrar \n"
          "por la puerta principal ya que no hay mucha seguridad, o puedes explotar la pared que da a la habitacion \n"
          "donde tienen todas las riquezas.¿Que haces?: (PUERTA/EXPLOCION): \n")

    if opcion == "PUERTA":
        operacion = float(input("Decides entra por la puerta principal ya que no hay guardias,sin embargo, tienes que \n"
                          "poner el digito que resulta de la siguiente operacion: 25 + 48 * {}\n".format(numero_random)))

        if operacion == 25 + 48 * numero_random:
            print("Logras acceder y llegas a la bobeda de los bandidos\n")
        else:
            print("La alarma se activa, los bandidos bienen por ti y te matan\n")
            print("FIN DEL JUEGO, PERDISTE")
            exit()

    elif opcion == "EXPLOCION" and dinamita == False:
        print("No tienes dinamita, por consiguiente, unos bandidos te encuentran y te asesinan.\n")
        print("FIN DEL JUEGO, PERDISTE")
        exit()

    elif opcion == "EXPLOCION" and dinamita == True:
        print("Usas la dinamita y accedes a la bobeda de los bandidos")

    print("Una vez dentro decides sacar todo el dinero y todas las cosas de valor, para cuando terminas, te encuentras \n"
          "con tu compañero, ambos lo han logrado, han salvado el pueblo y se han deshecho de los bandidos. \n"
          "Logras recuperar no solo el dinero de los habitantes del pueblo sino que, tabien logras recuperar el paquete \n"
          "que tenian que entragar. Tu y tu compañero se dirigen a entregar el encargo y una vez entregado, los \n"
          "habitantes del pueblo deciden pagarles por haber liberado al pueblo de control criminal de la banda de \n"
          "bandidos.Tu y tu compañeron deciden abandonar el pueblo para asi continuar con sus aventuras.\n")

    print("\n" + fin + "\n" + "-" * len(fin) + "\n")
    