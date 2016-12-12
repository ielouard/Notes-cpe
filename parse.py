import urllib.request 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

def getNotes(fichier):
		browser = webdriver.Chrome(executable_path=r"C:\Users\ibrahim\Downloads\chromedriver_win32\chromedriver.exe")
		html=browser.get('https://oga.cpe.fr/notes.php')
		user = browser.find_element_by_name("username")
		password = browser.find_element_by_name("password")
		user.clear()
		user.send_keys("ibrahim.elouard@cpe.fr") #adresse mail @cpe.fr
		password.clear()
		password.send_keys("squierj-bass1995") #mot de passe cpe
		browser.find_element_by_name("submit").click()



		soup=BeautifulSoup(browser.page_source)
		fichier = open(fichier, "w")
		fichier.write(str(soup.findAll("td", { "class" : "blanc" })))
		fichier.close()
		browser.close()

