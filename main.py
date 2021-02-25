from modules import udemy_class
from modules import alert_codigo
import json
print('Bot Udemy realizado por @fededav')
udemy = udemy_class.udemy()
url_curso = alert_codigo.Solicitar_codigo()
curso = udemy.Get_curso(url_curso)
print('OBTENIENDO LOS CAPITULOS DEL CURSO')
videos = udemy.Get_all_videos(curso)
count = 1
for capitulo in videos:
    udemy.Descargar_video(curso, capitulo)
    count += 1