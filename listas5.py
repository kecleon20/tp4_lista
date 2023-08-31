superheroes = [
    {
        'nombre': 'Spider-Man',
        'año_aparicion': 1962,
        'casa_comic': 'Marvel',
        'biografia': 'Peter Parker fue un joven mordido por una araña radioactiva la cual le dio superpoderes',
    },
    {
        'nombre': 'Superman',
        'año_aparicion': 1938,
        'casa_comic': 'DC',
        'biografia': 'Superman o como es conocido en la Tierra, Clark Kent, es un alienígena proveniente de Krypton',
    },
    {
        'nombre': 'Linterna Verde',
        'año_aparicion': 1940,
        'casa_comic': 'DC',
        'biografia': 'Harold Jordan era un piloto de avión el cual un anillo intergaláctico le concedió poderes',
    },
    {
        'nombre': 'Wolverine',
        'año_aparicion': 1974,
        'casa_comic': 'Marvel',
        'biografia': 'James Howlett es un mutante que perdió la memoria en el proyecto "Arma X" e intenta recuperarla junto a los X-Men ',
    },
    {
        'nombre': 'Dr. Strange',
        'año_aparicion': 1963,
        'casa_comic': 'DC',
        'biografia': 'Stephen Vincent Strange era un cirujano el cual sufrió un accidente, para recuperarse viaja al Tibet donde descubre sus poderes de hechicería',
    },
    {
        'nombre': 'Capitana Marvel',
        'año_aparicion': 1968,
        'casa_comic': 'Marvel',
        'biografia': 'Carol Denvers era una agente de inteligencia de la Fuerza Aérea la cual en una misión se volvió una híbrido Humano-Kree',
    },
    {
        'nombre': 'Mujer Maravilla',
        'año_aparicion': 1941,
        'casa_comic': 'DC',
        'biografia': 'La princesa amazona Diana de Themyscira, cuenta la historia que fue moldeada en arcilla por su madre Hipólita, que los dioses le dieron vida y que creció en una sociedad libre de hombres',
    },
    {
        'nombre': 'Star Lord',
        'año_aparicion': 1976,
        'casa_comic': 'Marvel',
        'biografia': 'Peter Jason Quill es un joven de treinta y dos años procedente de la Tierra, aunque no es completamente humano. Es el hijo mestizo del emperador JSon del planeta Spartax',
    }
]

def eliminar_superheroe(nombre):
    global superheroes
    superheroes = [heroe for heroe in superheroes if heroe['nombre'] != nombre]

def obtener_aparicion(nombre):
    for heroe in superheroes:
        if heroe['nombre'] == nombre:
            return heroe['año_aparicion']
    return None

def cambiar_casa_comic(nombre, nueva_casa):
    for heroe in superheroes:
        if heroe['nombre'] == nombre:
            heroe['casa_comic'] = nueva_casa

# a. Eliminar a Linterna Verde
eliminar_superheroe('Linterna Verde')

# b. Obtener el año de aparición de Wolverine
fecha_wolverine = obtener_aparicion('Wolverine')
print(f'El año de aparición de Wolverine es: {fecha_wolverine}')

# c. Cambiar la casa de Dr. Strange a Marvel
cambiar_casa_comic('Dr. Strange', 'Marvel')

print(superheroes)  # Imprimir la lista de superhéroes actualizada

# d. Mostrar los superhéroes con "traje" o "armadura" en su biografía
def superheroes_con_traje_o_armadura():
    relevant_superheroes = []
    for heroe in superheroes:
        if 'traje' in heroe['biografia'].lower() or 'armadura' in heroe['biografia'].lower():
            relevant_superheroes.append(heroe['nombre'])
    return relevant_superheroes

# e. Mostrar los superhéroes con fecha de aparición anterior a 1963
def superheroes_anteriores_a_1963():
    relevant_superheroes = []
    for heroe in superheroes:
        if heroe['año_aparicion'] < 1963:
            relevant_superheroes.append({'nombre': heroe['nombre'], 'casa_comic': heroe['casa_comic']})
    return relevant_superheroes

# f. Mostrar la casa de Capitana Marvel y Mujer Maravilla
def obtener_casa_por_nombre(nombre):
    for heroe in superheroes:
        if heroe['nombre'] == nombre:
            return heroe['casa_comic']
    return None

nombre_capitana_marvel = 'Capitana Marvel'
nombre_mujer_maravilla = 'Mujer Maravilla'

casa_capitana_marvel = obtener_casa_por_nombre(nombre_capitana_marvel)
casa_mm = obtener_casa_por_nombre(nombre_mujer_maravilla)

print(f'La casa de {nombre_capitana_marvel} es: {casa_capitana_marvel}')
print(f'La casa de {nombre_mujer_maravilla} es: {casa_mm}')

print("Superhéroes con 'traje' o 'armadura' en su biografía:", superheroes_con_traje_o_armadura())
print("Superhéroes anteriores a 1963:", superheroes_anteriores_a_1963())

# g. Mostrar la información de Flash y Star-Lord
def obtenernombre(nombre):
    for heroe in superheroes:
        if heroe['nombre'] == nombre:
            return heroe
    return None

nombre_flash = 'Flash'
nombre_starlord = 'Star-Lord'

info_flash = obtenernombre(nombre_flash)
info_starlord = obtenernombre(nombre_starlord)

if info_flash:
    print(f'Información de {nombre_flash}:')
    print(info_flash)
else:
    print(f'{nombre_flash} no encontrado.')

if info_starlord:
    print(f'Información de {nombre_starlord}:')
    print(info_starlord)
else:
    print(f'{nombre_starlord} no encontrado.')

# h. Listar los superhéroes que comienzan con B, M y S
def superheroes_por_inicial(letra_inicial):
    relevant_superheroes = []
    for heroe in superheroes:
        if heroe['nombre'][0].lower() == letra_inicial.lower():
            relevant_superheroes.append(heroe['nombre'])
    return relevant_superheroes

letras_iniciales = ['B', 'M', 'S']

for letra in letras_iniciales:
    superheroes_letra = superheroes_por_inicial(letra)
    print(f"Superhéroes que comienzan con '{letra}': {superheroes_letra}")

# i. Determinar cuántos superhéroes hay de cada casa de comic
def contar_superheroes_por_casa():
    casa_count = {'Marvel': 0, 'DC': 0}
    for heroe in superheroes:
        casa_count[heroe['casa_comic']] += 1
    return casa_count

contador_casas = contar_superheroes_por_casa()
print("Cantidad de superhéroes por casa de comic:")
for casa, count in contador_casas.items():
    print(f'{casa}: {count}')
