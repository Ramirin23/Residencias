import os
import pymysql

# Conectar a la base de datos
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    db='notes',
    port=3307,
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

# Obtener una lista de archivos en el directorio
directorio = 'C:\Python\Interface\pruebas\otas_clinicas_corpus_distemist'
archivos = os.listdir(directorio)

# Iterar sobre los archivos y agregar el contenido a la base de datos
try:
    with connection.cursor() as cursor:
        for archivo in archivos:
            if archivo.endswith('.txt'):
                with open(os.path.join(directorio, archivo), 'r', encoding='utf-8') as f:
                    contenido = f.read()
                    sql = "INSERT INTO interface_narrativa (description) VALUES (%s)"
                    cursor.execute(sql, (contenido,))
    connection.commit()
finally:
    connection.close()
