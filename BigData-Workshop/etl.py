import sqlite3
import pandas as pd

# Definimos los nombres que usaremos en el script para no cometer errores
DB_ARCHIVO = 'ventas.db'
TABLA_NOMBRE = 'ventas'
CSV_ARCHIVO = 'sales.csv'
TAMANO_BLOQUE = 10000

def ejecutar_etl():
    # Esto crea el archivo .db si no existe y se conecta a él
    conexion = sqlite3.connect(DB_ARCHIVO)
    cursor = conexion.cursor()

    cursor.execute(f'''
    CREATE TABLE IF NOT EXISTS {TABLA_NOMBRE} (
        id INTEGER PRIMARY KEY,
        date TEXT NOT NULL,
        product TEXT NOT NULL,
        category TEXT NOT NULL,
        price REAL NOT NULL,
        quantity INTEGER NOT NULL,
        total REAL NOT NULL
    );
    ''')
    conexion.commit()
    print("Base de datos y tabla listas para recibir los datos.")

    #Insertar datos en bloques (chunks)
    iterador_de_bloques = pd.read_csv(CSV_ARCHIVO, chunksize=TAMANO_BLOQUE)
    
    # Recorremos cada bloque y lo insertamos en la base de datos
    for i, bloque in enumerate(iterador_de_bloques):
        bloque.to_sql(TABLA_NOMBRE, conexion, if_exists='append', index=False)
        print(f" -> Bloque {i + 1} cargado exitosamente en la base de datos.")
        
    conexion.close()

if __name__ == "__main__":
    ejecutar_etl()