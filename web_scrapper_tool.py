from selenium import webdriver
from scrapper import Scrapper
import time
import re


def scrape_page(url):

    main_url = url
    driver = webdriver.Firefox()
    scrapper = Scrapper(driver)

    def _get_scrape_link():
        scrapper.load(main_url)
        time.sleep(3)
        links = [main_url]
        links_to_scrape = scrapper.findall("//span[contains(@class,'page ')]/a[@href]")
        links.extend(ele.get_attribute("href") for ele in links_to_scrape if links_to_scrape)
        return links

    scrapped_data = []
    links = _get_scrape_link()
    if links:
        for link in links:
            scrapper.load(link)
            time.sleep(3)

            product_list = scrapper.findall("//li[@class='column']/product-card")
            if product_list:
                for product_ele in product_list:
                    product_name_ele = scrapper.find(product_ele,".//a[@title][@href]")
                    pro_name = product_name_ele.get_attribute("title") if product_name_ele else None

                    pro_price_ele = scrapper.find(product_ele,".//span[@class='price']//ins/span")
                    pro_price =  pro_price_ele.get_attribute("innerText") if pro_price_ele else None

                    pro_price = int(re.search(r"(\d+)",pro_price.replace(",","")).group(1)) if pro_price else None

                    rating_ele = scrapper.find(product_ele,".//div[@class='star-rating']")
                    rating = rating_ele.get_attribute("innerText") if rating_ele else None
                    if not rating:
                        rating = 0

                    sold_out_ele = scrapper.find(product_ele,".//span[contains(text(),'Sold out')]")
                    availability = False if sold_out_ele else True
                    data = {
                        'name':pro_name,
                        'price':pro_price,
                        'rating': rating,
                        'availability':availability
                    }
                    scrapped_data.append(data)
            else:
                print("products list not found")

    driver.quit()

    return scrapped_data
