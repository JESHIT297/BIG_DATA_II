import csv 
import datetime
import random

CURREN_YEAR = 2025

catgories = ["Ropa", "Hogar", "Electronica"]
products = [
    "Televisor", "Celular", "Laptop", "Camisa", "Pantalon", "Zapatos", "Sofa", "Mesa", "Silla"
]

with open("BigData-Workshop/sales.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow([
        "id", "date", "product", "category", "price", "quantity", "total"
    ]) 

    for i in range(1, 100001):
        date = datetime.date(CURREN_YEAR, random.randint(1,12),random.randint(1,28))
        product = random.choice(products)
        catgory = "Electronica" if product in ["Televisor", "Celular", "Laptop"] else "Ropa" if product in ["Camisa", "Pantalon", "Zapatos"] else "Hogar"
        price = round(random.uniform(10, 2000), 2)
        quantity = random.randint(1,10)
        total = round(price * quantity, 2)
        writer.writerow([i, date, product, catgory, price, quantity, total])
    
print("Archivo 'sales.csv' generado con 100,000 registros.")