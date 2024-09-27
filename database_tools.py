import os
import csv
import datetime


file_path = os.path.join(os.path.dirname(__file__), "report.csv")


def get_data(connection):
    connection.show_table()
    inserted_values = connection.cursor.fetchall()

    return inserted_values


def get_available_products(connection):
    connection.available_products()
    avai_pro = connection.cursor.fetchall()

    return avai_pro


def get_summart_report(connection):

    connection.report_data()
    total_products, average_price, out_of_stock = connection.cursor.fetchall()[0]

    with open(file_path, "w", newline="") as file:
        field_names = ["Date", "Total_Prodcuts", "Average_Price", "Total_out_of_stock"]

        writer = csv.DictWriter(file, fieldnames=field_names)
        writer.writeheader()

        data = [
            {
                "Date": datetime.date.today(),
                "Total_Prodcuts": total_products,
                "Average_Price": int(average_price),
                "Total_out_of_stock": out_of_stock,
            }
        ]
        writer.writerows(data)


def top_products(connection):
    connection.expensive_pro()
    expensive_pro = connection.cursor.fetchall()

    return expensive_pro


def store_data(connection, data):
    connection.create_table()
    connection.insert_value(data)
