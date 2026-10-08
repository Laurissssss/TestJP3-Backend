from django.core.management.base import BaseCommand
from trivia.models import Categoria, Pregunta, Opcion

class Command(BaseCommand):
    help = 'Carga datos iniciales para el juego de trivia'

    def handle(self, *args, **kwargs):
        # Limpiar datos existentes
        Categoria.objects.all().delete()
        
        # 1. Cultura General
        cat_cultura = Categoria.objects.create(nombre='Cultura General', descripcion='Preguntas variadas sobre el mundo.')
        p1 = Pregunta.objects.create(texto='¿Cuál es el océano más grande del mundo?', categoria=cat_cultura)
        Opcion.objects.create(texto='Océano Atlántico', es_correcta=False, pregunta=p1)
        Opcion.objects.create(texto='Océano Índico', es_correcta=False, pregunta=p1)
        Opcion.objects.create(texto='Océano Pacífico', es_correcta=True, pregunta=p1)
        Opcion.objects.create(texto='Océano Ártico', es_correcta=False, pregunta=p1)

        p2 = Pregunta.objects.create(texto='¿En qué año llegó el hombre a la Luna?', categoria=cat_cultura)
        Opcion.objects.create(texto='1965', es_correcta=False, pregunta=p2)
        Opcion.objects.create(texto='1969', es_correcta=True, pregunta=p2)
        Opcion.objects.create(texto='1971', es_correcta=False, pregunta=p2)
        Opcion.objects.create(texto='1959', es_correcta=False, pregunta=p2)

        # 2. Genshin Impact
        cat_genshin = Categoria.objects.create(nombre='Genshin Impact', descripcion='Preguntas sobre el popular juego de HoYoverse.')
        p3 = Pregunta.objects.create(texto='¿Cuál es el nombre del Arconte Anemo?', categoria=cat_genshin)
        Opcion.objects.create(texto='Zhongli', es_correcta=False, pregunta=p3)
        Opcion.objects.create(texto='Raiden Shogun', es_correcta=False, pregunta=p3)
        Opcion.objects.create(texto='Venti', es_correcta=True, pregunta=p3)
        Opcion.objects.create(texto='Nahida', es_correcta=False, pregunta=p3)

        p4 = Pregunta.objects.create(texto='¿Cómo se llama el continente donde se desarrolla la historia?', categoria=cat_genshin)
        Opcion.objects.create(texto='Teyvat', es_correcta=True, pregunta=p4)
        Opcion.objects.create(texto='Eorzea', es_correcta=False, pregunta=p4)
        Opcion.objects.create(texto='Azeroth', es_correcta=False, pregunta=p4)
        Opcion.objects.create(texto='Hyrule', es_correcta=False, pregunta=p4)

        # 3. Minecraft
        cat_minecraft = Categoria.objects.create(nombre='Minecraft', descripcion='Preguntas sobre el juego de bloques.')
        p5 = Pregunta.objects.create(texto='¿Qué material se necesita para hacer un portal al Nether?', categoria=cat_minecraft)
        Opcion.objects.create(texto='Piedra', es_correcta=False, pregunta=p5)
        Opcion.objects.create(texto='Obsidiana', es_correcta=True, pregunta=p5)
        Opcion.objects.create(texto='Diamante', es_correcta=False, pregunta=p5)
        Opcion.objects.create(texto='Cuarzo', es_correcta=False, pregunta=p5)

        p6 = Pregunta.objects.create(texto='¿Qué mob explota al acercarse al jugador?', categoria=cat_minecraft)
        Opcion.objects.create(texto='Zombie', es_correcta=False, pregunta=p6)
        Opcion.objects.create(texto='Esqueleto', es_correcta=False, pregunta=p6)
        Opcion.objects.create(texto='Enderman', es_correcta=False, pregunta=p6)
        Opcion.objects.create(texto='Creeper', es_correcta=True, pregunta=p6)

        # 4. Mitología Griega
        cat_mitologia = Categoria.objects.create(nombre='Mitología Griega', descripcion='Mitos y leyendas de la antigua Grecia.')
        p7 = Pregunta.objects.create(texto='¿Quién es el dios griego de los océanos?', categoria=cat_mitologia)
        Opcion.objects.create(texto='Zeus', es_correcta=False, pregunta=p7)
        Opcion.objects.create(texto='Hades', es_correcta=False, pregunta=p7)
        Opcion.objects.create(texto='Apolo', es_correcta=False, pregunta=p7)
        Opcion.objects.create(texto='Poseidón', es_correcta=True, pregunta=p7)

        p8 = Pregunta.objects.create(texto='¿Qué héroe griego era invulnerable excepto en su talón?', categoria=cat_mitologia)
        Opcion.objects.create(texto='Hércules', es_correcta=False, pregunta=p8)
        Opcion.objects.create(texto='Aquiles', es_correcta=True, pregunta=p8)
        Opcion.objects.create(texto='Teseo', es_correcta=False, pregunta=p8)
        Opcion.objects.create(texto='Perseo', es_correcta=False, pregunta=p8)

        # 5. Medicina
        cat_medicina = Categoria.objects.create(nombre='Medicina', descripcion='Conocimientos básicos del cuerpo y la salud.')
        p9 = Pregunta.objects.create(texto='¿Cuál es el órgano más grande del cuerpo humano?', categoria=cat_medicina)
        Opcion.objects.create(texto='Hígado', es_correcta=False, pregunta=p9)
        Opcion.objects.create(texto='Piel', es_correcta=True, pregunta=p9)
        Opcion.objects.create(texto='Cerebro', es_correcta=False, pregunta=p9)
        Opcion.objects.create(texto='Corazón', es_correcta=False, pregunta=p9)

        p10 = Pregunta.objects.create(texto='¿Qué célula sanguínea se encarga de transportar el oxígeno?', categoria=cat_medicina)
        Opcion.objects.create(texto='Glóbulo blanco', es_correcta=False, pregunta=p10)
        Opcion.objects.create(texto='Plaqueta', es_correcta=False, pregunta=p10)
        Opcion.objects.create(texto='Glóbulo rojo', es_correcta=True, pregunta=p10)
        Opcion.objects.create(texto='Plasma', es_correcta=False, pregunta=p10)

        # 6. Roblox
        cat_roblox = Categoria.objects.create(nombre='Roblox', descripcion='Todo sobre la plataforma de juegos Roblox.')
        p11 = Pregunta.objects.create(texto='¿En qué año fue lanzado Roblox oficialmente?', categoria=cat_roblox)
        Opcion.objects.create(texto='2004', es_correcta=False, pregunta=p11)
        Opcion.objects.create(texto='2006', es_correcta=True, pregunta=p11)
        Opcion.objects.create(texto='2008', es_correcta=False, pregunta=p11)
        Opcion.objects.create(texto='2010', es_correcta=False, pregunta=p11)

        p12 = Pregunta.objects.create(texto='¿Cómo se llama la moneda virtual oficial de Roblox?', categoria=cat_roblox)
        Opcion.objects.create(texto='Tix', es_correcta=False, pregunta=p12)
        Opcion.objects.create(texto='Minecoins', es_correcta=False, pregunta=p12)
        Opcion.objects.create(texto='V-Bucks', es_correcta=False, pregunta=p12)
        Opcion.objects.create(texto='Robux', es_correcta=True, pregunta=p12)

        # 7. Cultura Pop
        cat_culturapop = Categoria.objects.create(nombre='Cultura Pop', descripcion='Música, cine, series y tendencias.')
        p13 = Pregunta.objects.create(texto='¿Qué artista es mundialmente conocida como la "Reina del Pop"?', categoria=cat_culturapop)
        Opcion.objects.create(texto='Britney Spears', es_correcta=False, pregunta=p13)
        Opcion.objects.create(texto='Lady Gaga', es_correcta=False, pregunta=p13)
        Opcion.objects.create(texto='Madonna', es_correcta=True, pregunta=p13)
        Opcion.objects.create(texto='Beyoncé', es_correcta=False, pregunta=p13)

        p14 = Pregunta.objects.create(texto='¿En qué aclamada serie de televisión aparecen Walter White y Jesse Pinkman?', categoria=cat_culturapop)
        Opcion.objects.create(texto='The Walking Dead', es_correcta=False, pregunta=p14)
        Opcion.objects.create(texto='Game of Thrones', es_correcta=False, pregunta=p14)
        Opcion.objects.create(texto='Stranger Things', es_correcta=False, pregunta=p14)
        Opcion.objects.create(texto='Breaking Bad', es_correcta=True, pregunta=p14)

        # 8. Literatura
        cat_literatura = Categoria.objects.create(nombre='Literatura', descripcion='Clásicos de la literatura mundial y autores famosos.')
        p15 = Pregunta.objects.create(texto='¿Quién es el autor de la famosa novela "Cien años de soledad"?', categoria=cat_literatura)
        Opcion.objects.create(texto='Mario Vargas Llosa', es_correcta=False, pregunta=p15)
        Opcion.objects.create(texto='Julio Cortázar', es_correcta=False, pregunta=p15)
        Opcion.objects.create(texto='Gabriel García Márquez', es_correcta=True, pregunta=p15)
        Opcion.objects.create(texto='Jorge Luis Borges', es_correcta=False, pregunta=p15)

        p16 = Pregunta.objects.create(texto='¿Cuál de estos libros narra las aventuras de un hidalgo caballero y su escudero Sancho Panza?', categoria=cat_literatura)
        Opcion.objects.create(texto='Don Quijote de la Mancha', es_correcta=True, pregunta=p16)
        Opcion.objects.create(texto='El Cantar de mio Cid', es_correcta=False, pregunta=p16)
        Opcion.objects.create(texto='La Divina Comedia', es_correcta=False, pregunta=p16)
        Opcion.objects.create(texto='La Odisea', es_correcta=False, pregunta=p16)

        # 9. Deporte
        cat_deporte = Categoria.objects.create(nombre='Deporte', descripcion='Reglas, eventos e historia deportiva.')
        p17 = Pregunta.objects.create(texto='¿Cada cuántos años se celebran los Juegos Olímpicos de Verano?', categoria=cat_deporte)
        Opcion.objects.create(texto='2', es_correcta=False, pregunta=p17)
        Opcion.objects.create(texto='4', es_correcta=True, pregunta=p17)
        Opcion.objects.create(texto='5', es_correcta=False, pregunta=p17)
        Opcion.objects.create(texto='8', es_correcta=False, pregunta=p17)

        p18 = Pregunta.objects.create(texto='¿En qué deporte se utiliza una pelota con forma ovalada?', categoria=cat_deporte)
        Opcion.objects.create(texto='Baloncesto', es_correcta=False, pregunta=p18)
        Opcion.objects.create(texto='Voleibol', es_correcta=False, pregunta=p18)
        Opcion.objects.create(texto='Tenis', es_correcta=False, pregunta=p18)
        Opcion.objects.create(texto='Rugby', es_correcta=True, pregunta=p18)

        # 10. Anime
        cat_anime = Categoria.objects.create(nombre='Anime', descripcion='Cultura de la animación japonesa.')
        p19 = Pregunta.objects.create(texto='¿Cuál es el nombre del protagonista del anime "Naruto"?', categoria=cat_anime)
        Opcion.objects.create(texto='Sasuke Uchiha', es_correcta=False, pregunta=p19)
        Opcion.objects.create(texto='Kakashi Hatake', es_correcta=False, pregunta=p19)
        Opcion.objects.create(texto='Naruto Uzumaki', es_correcta=True, pregunta=p19)
        Opcion.objects.create(texto='Itachi Uchiha', es_correcta=False, pregunta=p19)

        p20 = Pregunta.objects.create(texto='En "Dragon Ball Z", ¿qué raza alienígena es Goku?', categoria=cat_anime)
        Opcion.objects.create(texto='Namekiano', es_correcta=False, pregunta=p20)
        Opcion.objects.create(texto='Saiyajin', es_correcta=True, pregunta=p20)
        Opcion.objects.create(texto='Terrícola', es_correcta=False, pregunta=p20)
        Opcion.objects.create(texto='Majin', es_correcta=False, pregunta=p20)

        # 11. WW2 (Segunda Guerra Mundial)
        cat_ww2 = Categoria.objects.create(nombre='WW2 (Segunda Guerra Mundial)', descripcion='Eventos históricos del mayor conflicto global.')
        p21 = Pregunta.objects.create(texto='¿En qué año comenzó la Segunda Guerra Mundial?', categoria=cat_ww2)
        Opcion.objects.create(texto='1914', es_correcta=False, pregunta=p21)
        Opcion.objects.create(texto='1939', es_correcta=True, pregunta=p21)
        Opcion.objects.create(texto='1941', es_correcta=False, pregunta=p21)
        Opcion.objects.create(texto='1945', es_correcta=False, pregunta=p21)

        p22 = Pregunta.objects.create(texto='¿Qué evento provocó la entrada directa de Estados Unidos al conflicto?', categoria=cat_ww2)
        Opcion.objects.create(texto='El asesinato del Archiduque Francisco Fernando', es_correcta=False, pregunta=p22)
        Opcion.objects.create(texto='El desembarco de Normandía', es_correcta=False, pregunta=p22)
        Opcion.objects.create(texto='La batalla de Stalingrado', es_correcta=False, pregunta=p22)
        Opcion.objects.create(texto='El ataque a Pearl Harbor', es_correcta=True, pregunta=p22)

        # 12. Pregunta tipo ICFES
        cat_icfes = Categoria.objects.create(nombre='Pregunta tipo ICFES', descripcion='Desafía tu pensamiento lógico y analítico.')
        p23 = Pregunta.objects.create(texto='Si un cultivo de bacterias se duplica cada hora y comienza con 10, ¿cuántas habrá luego de 3 horas?', categoria=cat_icfes)
        Opcion.objects.create(texto='30', es_correcta=False, pregunta=p23)
        Opcion.objects.create(texto='40', es_correcta=False, pregunta=p23)
        Opcion.objects.create(texto='60', es_correcta=False, pregunta=p23)
        Opcion.objects.create(texto='80', es_correcta=True, pregunta=p23)

        p24 = Pregunta.objects.create(texto='Lee: "El cielo está muy oscuro y con nubes negras, por lo tanto, lloverá". ¿Qué tipo de argumento es?', categoria=cat_icfes)
        Opcion.objects.create(texto='Deductivo', es_correcta=False, pregunta=p24)
        Opcion.objects.create(texto='Inductivo', es_correcta=True, pregunta=p24)
        Opcion.objects.create(texto='Analógico', es_correcta=False, pregunta=p24)
        Opcion.objects.create(texto='Abductivo', es_correcta=False, pregunta=p24)

        # 13. Geografía
        cat_geografia = Categoria.objects.create(nombre='Geografía', descripcion='Países, capitales y maravillas naturales.')
        p25 = Pregunta.objects.create(texto='¿Cuál es el río más largo del mundo?', categoria=cat_geografia)
        Opcion.objects.create(texto='Río Nilo', es_correcta=False, pregunta=p25)
        Opcion.objects.create(texto='Río Amazonas', es_correcta=True, pregunta=p25)
        Opcion.objects.create(texto='Río Yangtsé', es_correcta=False, pregunta=p25)
        Opcion.objects.create(texto='Río Misisipi', es_correcta=False, pregunta=p25)

        p26 = Pregunta.objects.create(texto='¿Cuál es la capital de Australia?', categoria=cat_geografia)
        Opcion.objects.create(texto='Sídney', es_correcta=False, pregunta=p26)
        Opcion.objects.create(texto='Melbourne', es_correcta=False, pregunta=p26)
        Opcion.objects.create(texto='Canberra', es_correcta=True, pregunta=p26)
        Opcion.objects.create(texto='Brisbane', es_correcta=False, pregunta=p26)

        # 14. Matemáticas
        cat_matematicas = Categoria.objects.create(nombre='Matemáticas', descripcion='Cálculos, operaciones y lógica numérica.')
        p27 = Pregunta.objects.create(texto='¿Cuál es el resultado de la operación: 5 + 3 x 2?', categoria=cat_matematicas)
        Opcion.objects.create(texto='16', es_correcta=False, pregunta=p27)
        Opcion.objects.create(texto='11', es_correcta=True, pregunta=p27)
        Opcion.objects.create(texto='10', es_correcta=False, pregunta=p27)
        Opcion.objects.create(texto='15', es_correcta=False, pregunta=p27)

        p28 = Pregunta.objects.create(texto='¿Cuál es la raíz cuadrada de 144?', categoria=cat_matematicas)
        Opcion.objects.create(texto='12', es_correcta=True, pregunta=p28)
        Opcion.objects.create(texto='14', es_correcta=False, pregunta=p28)
        Opcion.objects.create(texto='16', es_correcta=False, pregunta=p28)
        Opcion.objects.create(texto='18', es_correcta=False, pregunta=p28)

        self.stdout.write(self.style.SUCCESS('¡Base de datos poblada exitosamente con 14 categorías!'))
