#Cinema.py
"""This class is good"""
from bs4 import BeautifulSoup as bs
import requests as r

class Cinemaparser:
    """Something about cinema"""
    def __init__(self, city):
        """This function saves information about city name"""
        self.city = city
        self.content = None

    def extract_raw_content(self):
        """This function extracts raw content"""
        main_page_url = "https://msk.subscity.ru"
        get_main_page_response = r.get(main_page_url)
        self.content = bs(get_main_page_response.text, "html.parser")

    def print_raw_content(self):
        """This function displays self.content on the screen"""
        return self.content.prettify()

    def get_films_list(self):
        """This function return list of films"""
        list_of_all_films = list()
        all_films = self.content.find_all("div", class_="movie-plate")
        i = 0
        for film in all_films:
            i = i + 1
            if i != 1:
                list_of_all_films.append(film["attr-title"])
        return list_of_all_films[1:-1]
