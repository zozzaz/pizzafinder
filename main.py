from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import re
import time

def count_pizza(url, lang):
    try:
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--enable-unsafe-swiftshader")
        chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
        
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(url)
        time.sleep(5)
        html = driver.page_source
        driver.quit()

        soup = BeautifulSoup(html, 'html.parser')

        for script in soup(["script", "style"]):
            script.decompose()

        all_text = soup.get_text()
        if lang == "eng":
            pizza_count = len(re.findall(r'pizzas?', all_text, re.IGNORECASE))
        else:
            pizza_count = len(re.findall(r'пицц[а-яё]*', all_text, re.IGNORECASE))

        for tag in soup.find_all():
            for attr in ['alt', 'title', 'aria-label']:
                if tag.has_attr(attr):
                    attr_text = tag[attr]
                    if lang == "eng":
                        pizza_count += len(re.findall(r'pizzas?', all_text, re.IGNORECASE))
                    else:
                        pizza_count += len(re.findall(r'пицц[а-яё]*', all_text, re.IGNORECASE))
        return pizza_count
    
    except Exception as error:
        print(f"Error: {error}")
        return 0

pizza_art = """
                              ░░░░░░░░░░░░░░
                            ░░░░██████████░░░░
                          ░░░░██░░░░░░░░████░░░░
                        ░░░░██░░░░░░░░░░░░████░░░░░░░░░░░░░░░░░░
                      ░░░░██░░░░░░░░██████░░██████████████████░░░░░░░░
                    ░░░░██░░░░░░░░▓▓██░░  ░░░░░░░░░░░░░░░░░░██████████░░░░░░░░░░
                  ░░░░██░░░░░░▒▒▒▒██    ░░▓▓▓▓▓▓▓▓▓▓░░░░░░░░▒▒▒▒░░░░██████████░░
                ░░░░██░░░░▒▒▒▒░░████  ▓▓▓▓▒▒░░░░░░░░▓▓  ░░░░▒▒░░░░░░░░░░▒▒░░██░░░░░░░░░░░░
              ░░░░██░░░░░░▒▒██████▓▓▓▓▓▓░░░░░░░░░░▒▒▓▓  ░░░░▒▒▒▒░░░░░░░░░░▒▒████████████░░░░░░
            ░░░░██░░░░▒▒▒▒▒▒██░░▓▓▒▒▒▒▒▒░░░░░░░░▒▒▒▒▓▓    ░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░  ░░██████░░
          ░░░░██░░░░▒▒░░░░████░░▓▓▒▒░░░░░░░░░░▒▒▒▒▓▓      ░░░░    ░░░░░░            ░░░░  ██░░
        ░░░░██░░░░▒▒▒▒██████    ▓▓░░░░▒▒░░▒▒▒▒▒▒▓▓        ░░░░        ░░              ░░  ██░░
      ░░░░██▒▒░░░░▒▒▒▒██░░    ░░░░▓▓▒▒▒▒▒▒▒▒▓▓▓▓░░░░        ░░              ░░░░          ██░░
    ░░░░██▒▒▒▒▒▒▒▒▒▒████░░      ░░░░▓▓▓▓▓▓▓▓            ░░░░            ░░░░░░██████████████░░
  ░░░░██▒▒▒▒▒▒▒▒▒▒▓▓██░░░░▒▒▒▒▒▒    ░░░░░░░░                            ▓▓▓▓▓▓▒▒▒▒▒▒▒▒████░░░░
  ░░██▒▒░░░░░░░░▒▒██  ▒▒░░░░░░                          ████      ██████▒▒░░▒▒████████░░░░░░
░░░░██░░░░░░░░░░████  ░░▒▒▒▒              ██████        ██░░██████▒▒▒▒▒▒▒▒██████░░░░░░░░
░░██▒▒▓▓▓▓▓▓▓▓▒▒██░░  ░░░░░░            ░░██▒▒██      ░░██░░▒▒▒▒▒▒░░████████░░░░░░
░░████░░▒▒▒▒██████      ██████    ████████▒▒░░██░░    ░░████████████░░░░░░░░░░
░░██▒▒▒▒██▒▒▒▒██        ██▒▒▒▒████▒▒▒▒▒▒▒▒▒▒░░██░░░░░░░░██░░░░░░░░░░░░
░░██▒▒▒▒██████████      ▓▓▒▒▒▒░░░░░░░░░░████████░░░░░░░░██░░
░░░░██░░██░░░░▒▒██░░░░░░░░██▒▒▒▒████████░░░░░░░░████████░░░░
  ░░░░██▒▒▒▒▒▒▒▒██░░░░░░░░░░████░░░░░░░░░░    ░░░░░░░░░░░░
    ░░░░████████████░░░░░░░░██░░░░
      ░░▒▒░░░░▒▒░░░░▓▓░░░░██░░░░
        ░░    ░░░░░░░░████░░░░
                    ░░▓▓▓▓░░
"""
if __name__ == "__main__":

  print(pizza_art)
  print("Welcome to the super duper hacker pizza counter!")
  print("                  ███████╗██████╗ ██╗███████╗███████╗ █████╗ ")
  print("                  ██╔════╝██╔══██╗██║╚══███╔╝╚══███╔╝██╔══██╗")
  print("                  █████╗  ██████╔╝██║  ███╔╝   ███╔╝ ███████║")
  print("                  ██╔══╝  ██╔═══╝ ██║ ███╔╝   ███╔╝  ██╔══██║")
  print("                  ██║     ██║     ██║███████╗███████╗██║  ██║")
  print("                  ╚═╝     ╚═╝     ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝\n") #пик смеха, почему вы не смеётесь?

  try:
      choice = input("Start searching pizzas to eat? Y/N\n>>>")
      if choice == "Y":
          print("Select website's language: \n1. English\n2. Russian")
          lang_sel = input(">>>")
          if lang_sel == "1":
              lang = "eng"
          elif lang_sel == "2":
              lang = "rus"
          url = input('Enter website URL (e.g., "https://dodopizza.ru/moscow"):\n')
          if not url.startswith(("https://", "http://")):
              url = "https://" + url
          print("Analyzing website... Please wait.")
          count = count_pizza(url, lang)
          print(f"\nAnalysis result:\nWord 'pizza' mentions {count} times. Ready to have a meal? :P")
      elif choice == "N":
          print("See you next time.")
      else:
          print("Wrong choice")
  except ValueError:
      print("Wrong symbol")
