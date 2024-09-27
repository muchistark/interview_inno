import sqlite3


class Connection:

    def __init__(self):
        self.connection = sqlite3.connect("product.db")
        self.cursor = self.connection.cursor()

    def create_table(self):
        self.cursor.execute(
            """
        CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price INTEGER NOT NULL,
        rating REAL NOT NULL,
        availability BOOLEAN NOT NULL
    )

        """
        )

    def expensive_pro(self):
        self.cursor.execute(
            """
        SELECT 
            name,
            price,
            rating
        FROM 
            products 
        ORDER BY 
            price DESC 
        LIMIT 5;
        
        """
        )

    def available_products(self):
        self.cursor.execute("SELECT * from products WHERE availability=1")

    def show_table(self):
        self.cursor.execute("SELECT * from products")

    def report_data(self):
        self.cursor.execute(
            """    
            SELECT 
            COUNT(*) AS total_products,
            AVG(price) AS average_price,
            SUM(CASE WHEN availability = 0 THEN 1 ELSE 0 END) AS unavailable_products
            FROM 
                products;
            
        """
        )

    def delete_all(self):
        self.cursor.execute("delete  from products")

    def insert_value(self, data_list: list[dict]):

        if data_list:
            for data in data_list:
                name = data.get("name")
                price = data.get("price")
                rating = data.get("rating")
                availability = data.get("availability")
                query = f"INSERT INTO products (name, price, rating, availability) VALUES ('{name}',{price},{rating},{availability})"

                self.cursor.execute(query)

    def close_connect(self):
        self.connection.commit()
        self.connection.close()
