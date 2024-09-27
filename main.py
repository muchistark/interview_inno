from web_scrapper_tool import scrape_page
from database_tools import *
from connection import Connection

scraped_data: list[dict] = scrape_page("https://www.simplytek.lk/collections/speakers")
if scraped_data:
    connection: Connection = Connection()
    store_data(connection, scraped_data)  # Inserting the Scrappd Data
    data_in_table: list[tuple] = get_data(connection)  # get values frm table

    available_pro: list[tuple] = get_available_products(
        connection
    )  # Prodcuts which has stock

    expensive_pro: list[tuple] = top_products(connection)  # get expensive Products

    get_summart_report(connection)  # this generates the Summary Report
    connection.close_connect()
else:
    print("No Data available")
