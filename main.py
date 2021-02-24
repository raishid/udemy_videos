from modules import udemy_class
import json
print('Bot Udemy realizado por @fededav')
udemy = udemy_class.udemy()
url_curso = input('Introduce la url del curso: ')
curso = udemy.Get_curso(url_curso)
print('OBTENIENDO LOS CAPITULOS DEL CURSO')
videos = udemy.Get_all_videos(curso)
for capitulo in videos:
    udemy.Descargar_video(curso, capitulo)


