class Pokemon:
    def __init__(self, nombre, nivel, tipo, subtipo=None):
        self.nombre = nombre
        self.nivel = nivel
        self.tipo = tipo
        self.subtipo = subtipo

class Entrenador:
    def __init__(self, nombre, torneos_ganados, batallas_perdidas, batallas_ganadas, pokemons):
        self.nombre = nombre
        self.torneos_ganados = torneos_ganados
        self.batallas_perdidas = batallas_perdidas
        self.batallas_ganadas = batallas_ganadas
        self.pokemons = pokemons

# Definición de entrenadores y sus datos
entrenadores = [
    Entrenador("Red", 5, 1, 110, [Pokemon("Pikachu", 88, "Eléctrico"), Pokemon("Blastoise", 84, "Agua"), Pokemon("Charizard", 84, "Fuego", "Volador")]),
    Entrenador("Cynthia", 4, 4, 182, [Pokemon("Spiritomb", 80, "Siniestro", "Fantasma"), Pokemon("Milotic", 80, "Agua"), Pokemon("Togekiss", 80, "Volador", "Normal")]),
    Entrenador("N", 2, 2, 3, [Pokemon("Politoed", 82, "Agua"), Pokemon("Lanturn", 82, "Agua", "Eléctrico"), Pokemon("Kabutops", 80, "Roca", "Agua")]),
]

def obtener_cantidad_pokemon(entrenador):
    return len(entrenador.pokemons)

def listar_entrenadores_mas_de_tres_torneos(entrenadores):
    return [entrenador.nombre for entrenador in entrenadores if entrenador.torneos_ganados > 3]

def pokemon_mayor_nivel_entrenador_mas_torneos(entrenadores):
    entrenador_mas_torneos = max(entrenadores, key=lambda e: e.torneos_ganados)
    pokemon_mayor_nivel = max(entrenador_mas_torneos.pokemons, key=lambda p: p.nivel)
    return pokemon_mayor_nivel

# a. obtener la cantidad de Pokémons de un determinado entrenador;
entrenador_red = next((entrenador for entrenador in entrenadores if entrenador.nombre == "Red"), None)
if entrenador_red:
    cantidad_pokemon = obtener_cantidad_pokemon(entrenador_red)
    print(f"El entrenador {entrenador_red.nombre} tiene {cantidad_pokemon} Pokémon.")
else:
    print("No se encontró el entrenador Red en la lista.")

# b. listar los entrenadores que hayan ganado más de tres torneos;
entrenadores_mas_tres_torneos = listar_entrenadores_mas_de_tres_torneos(entrenadores)
print("Entrenadores con más de tres torneos ganados:", entrenadores_mas_tres_torneos)

# c. el Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados;
pokemon_mayor_nivel_entrenador_mas_torneos = pokemon_mayor_nivel_entrenador_mas_torneos(entrenadores)
print(f"El Pokémon de mayor nivel del entrenador con más torneos ganados es {pokemon_mayor_nivel_entrenador_mas_torneos.nombre}, con nivel {pokemon_mayor_nivel_entrenador_mas_torneos.nivel}.")

def mostrar_datos_entrenador_pokemons(entrenador):
    print(f"Datos del entrenador {entrenador.nombre}:")
    print(f"Torneos ganados: {entrenador.torneos_ganados}")
    print(f"Batallas perdidas: {entrenador.batallas_perdidas}")
    print(f"Batallas ganadas: {entrenador.batallas_ganadas}")
    print("Pokémons:")
    for pokemon in entrenador.pokemons:
        print(f"  Nombre: {pokemon.nombre}")
        print(f"  Nivel: {pokemon.nivel}")
        print(f"  Tipo: {pokemon.tipo}")
        if pokemon.subtipo:
            print(f"  Subtipo: {pokemon.subtipo}")
        print()

def entrenadores_porcentaje_batallas_ganados_mayor_79(entrenadores):
    return [entrenador.nombre for entrenador in entrenadores if (entrenador.batallas_ganadas / (entrenador.batallas_ganadas + entrenador.batallas_perdidas)) > 0.79]

def entrenadores_con_pokemons_tipo_fuego_planta_aguavolador(entrenadores):
    tipo_subtipo_combinaciones = [("Fuego", "Planta"), ("Agua", "Volador")]
    entrenadores_resultado = []
    for entrenador in entrenadores:
        tiene_combinaciones = all(any(pokemon.tipo == tipo and (pokemon.subtipo == subtipo or subtipo is None) for pokemon in entrenador.pokemons) for tipo, subtipo in tipo_subtipo_combinaciones)
        if tiene_combinaciones:
            entrenadores_resultado.append(entrenador.nombre)
    return entrenadores_resultado

# d. mostrar todos los datos de un entrenador y sus Pokémos;(red como ejemplo)
entrenador_red = next((entrenador for entrenador in entrenadores if entrenador.nombre == "Red"), None)
if entrenador_red:
    mostrar_datos_entrenador_pokemons(entrenador_red)
else:
    print("No se encontró el entrenador Red en la lista.")

# e. mostrar los entrenadores cuyo porcentaje de batallas ganados sea mayor al 79 %;
entrenadores_porcentaje_mayor_79 = entrenadores_porcentaje_batallas_ganados_mayor_79(entrenadores)
print("Entrenadores con porcentaje de batallas ganadas mayor al 79%:", entrenadores_porcentaje_mayor_79)

# f. los entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador (tipo y subtipo);
entrenadores_tipo_fuego_planta_aguavolador = entrenadores_con_pokemons_tipo_fuego_planta_aguavolador(entrenadores)
print("Entrenadores con Pokémons de tipo fuego/planta o agua/volador:", entrenadores_tipo_fuego_planta_aguavolador)

def promedio_nivel_pokemons_entrenador(entrenador):
    total_niveles = sum(pokemon.nivel for pokemon in entrenador.pokemons)
    cantidad_pokemons = len(entrenador.pokemons)
    return total_niveles / cantidad_pokemons if cantidad_pokemons > 0 else 0

def contar_entrenadores_con_pokemon(entrenadores, nombre_pokemon):
    return sum(1 for entrenador in entrenadores if any(pokemon.nombre == nombre_pokemon for pokemon in entrenador.pokemons))

def entrenadores_con_pokemons_repetidos(entrenadores):
    entrenadores_repetidos = []
    for entrenador in entrenadores:
        nombres_pokemons = [pokemon.nombre for pokemon in entrenador.pokemons]
        if len(nombres_pokemons) != len(set(nombres_pokemons)):
            entrenadores_repetidos.append(entrenador.nombre)
    return entrenadores_repetidos

# g. el promedio de nivel de los Pokémons de un determinado entrenador;(en el ejemplo es Red)
entrenador_red = next((entrenador for entrenador in entrenadores if entrenador.nombre == "Red"), None)
if entrenador_red:
    promedio_nivel = promedio_nivel_pokemons_entrenador(entrenador_red)
    print(f"El promedio de nivel de los Pokémons del entrenador {entrenador_red.nombre} es {promedio_nivel:.2f}.")
else:
    print("No se encontró el entrenador Red en la lista.")

# Determinar cuántos entrenadores tienen un determinado Pokémon (por ejemplo, "Pikachu")
nombre_pokemon_buscado = "Pikachu"
cantidad_entrenadores_con_pokemon = contar_entrenadores_con_pokemon(entrenadores, nombre_pokemon_buscado)
print(f"{cantidad_entrenadores_con_pokemon} entrenador(es) tienen al Pokémon {nombre_pokemon_buscado}.")

# i. mostrar los entrenadores que tienen Pokémons repetidos;
entrenadores_pokemons_repetidos = entrenadores_con_pokemons_repetidos(entrenadores)
print("Entrenadores con Pokémon repetidos:", entrenadores_pokemons_repetidos)

#  j. determinar los entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Terrakion o Wingull;
nombre_pokemon_buscado = "Tyrantrum", "Terrakion", "Wingull"
cantidad_entrenadores_con_pokemon = contar_entrenadores_con_pokemon(entrenadores, nombre_pokemon_buscado)
print(f"{cantidad_entrenadores_con_pokemon} entrenador(es) tienen al Pokémon {nombre_pokemon_buscado}.")

# h. determinar cuántos entrenadores tienen a un determinado Pokémon;
def entrenador_tiene_pokemon(entrenador, nombre_pokemon):
    return any(pokemon.nombre == nombre_pokemon for pokemon in entrenador.pokemons)

# Mostrar datos de un entrenador y sus Pokémon
def mostrar_datos_entrenador_pokemons(entrenador):
    print(f"Datos del entrenador {entrenador.nombre}:")
    print(f"Torneos ganados: {entrenador.torneos_ganados}")
    print(f"Batallas perdidas: {entrenador.batallas_perdidas}")
    print(f"Batallas ganadas: {entrenador.batallas_ganadas}")
    print("Pokémons:")
    for pokemon in entrenador.pokemons:
        print(f"  Nombre: {pokemon.nombre}")
        print(f"  Nivel: {pokemon.nivel}")
        print(f"  Tipo: {pokemon.tipo}")
        if pokemon.subtipo:
            print(f"  Subtipo: {pokemon.subtipo}")
        print()

# Solicitar al usuario el nombre del entrenador y del Pokémon a buscar
nombre_entrenador_buscado = input("Ingrese el nombre del entrenador: ")
nombre_pokemon_buscado = input("Ingrese el nombre del Pokémon: ")

# Encontrar el entrenador en la lista
entrenador_buscado = next((entrenador for entrenador in entrenadores if entrenador.nombre == nombre_entrenador_buscado), None)

# f. determinar si un entrenador “X” tiene al Pokémon “Y”, tanto el nombre del entrenador
#como del Pokémon deben ser ingresados; además si el entrenador tiene al Pokémon se deberán mostrar los datos de ambos;
if entrenador_buscado and entrenador_tiene_pokemon(entrenador_buscado, nombre_pokemon_buscado):
    print(f"El entrenador {nombre_entrenador_buscado} tiene al Pokémon {nombre_pokemon_buscado}.")
    mostrar_datos_entrenador_pokemons(entrenador_buscado)
elif entrenador_buscado:
    print(f"El entrenador {nombre_entrenador_buscado} no tiene al Pokémon {nombre_pokemon_buscado}.")
else:
    print(f"No se encontró el entrenador {nombre_entrenador_buscado} en la lista.")

