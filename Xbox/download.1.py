
from bs4 import BeautifulSoup

soup = ""

def soup_the_file():
    global soup
    file = open("webpage1","r")
    soup = BeautifulSoup("webpage1", "html.parser")
    file.close()
    
    

def main():
    soup_the_file()
    print(soup.get_text())
    
    

    
    
    
    
    
    
    
main()