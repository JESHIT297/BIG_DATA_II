import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

DB_ARCHIVO = 'ventas.db'

def analizar_datos():

    conexion = sqlite3.connect(DB_ARCHIVO)

    # Total de ventas por categoría
    print("\n--- Total de ventas por categoría ---")
    consulta_a = "SELECT category, SUM(total) as total_ventas FROM ventas GROUP BY category ORDER BY total_ventas DESC"
    df_a = pd.read_sql_query(consulta_a, conexion)
    print(df_a)

    # Top 5 productos más vendidos (por cantidad de unidades)
    print("\n--- Top 5 productos más vendidos ---")
    consulta_b = "SELECT product, SUM(quantity) as cantidad_total FROM ventas GROUP BY product ORDER BY cantidad_total DESC LIMIT 5"
    df_b = pd.read_sql_query(consulta_b, conexion)
    print(df_b)

    # Mes con mayor facturación
    print("\n--- Mes con mayor facturación ---")
    consulta_c = "SELECT STRFTIME('%Y-%m', date) as mes, SUM(total) as facturacion_total FROM ventas GROUP BY mes ORDER BY facturacion_total DESC LIMIT 1"
    df_c = pd.read_sql_query(consulta_c, conexion)
    print(df_c)
    
    conexion.close()

    # --- PASO 5: Visualización de datos ---
    sns.set_theme(style="whitegrid")

    # Gráfico de ventas por categoría
    plt.figure(figsize=(10,6))
    sns.barplot(data=df_a, x='total_ventas', y='category', palette='viridis')
    plt.title('Total de Ventas por Categoría')
    plt.xlabel('Total de Ventas')
    plt.ylabel('Categoría')
    plt.tight_layout()
    plt.savefig('grafico_ventas_por_categoria.png')
    plt.close()

    # Gráfico Top 5 productos más vendidos
    plt.figure(figsize=(10,6))
    sns.barplot(data=df_b, x='cantidad_total', y='product', palette='magma')
    plt.title('Top 5 Productos Más Vendidos')
    plt.xlabel('Cantidad Total Vendida')
    plt.ylabel('Producto')
    plt.tight_layout()
    plt.savefig('grafico_top5_productos.png')
    plt.close()

    # Gráfico Mes con mayor facturación
    plt.figure(figsize=(8,5))
    sns.barplot(data=df_c, x='mes', y='facturacion_total', palette='coolwarm')
    plt.title('Mes con Mayor Facturación')
    plt.xlabel('Mes')
    plt.ylabel('Facturación Total')
    plt.tight_layout()
    plt.savefig('grafico_mes_mayor_facturacion.png')
    plt.close()

    print("Las 3 imágenes se generaron exitosamente.")
    
if __name__ == "__main__":
    analizar_datos()