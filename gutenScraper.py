import requests
from bs4 import BeautifulSoup
def go_gutenberg(file_format,book_no):
       url = "https://www.gutenberg.org/ebooks/"
       r =requests.get(url+str(book_no))
       r_html  = r.text
       soup = BeautifulSoup(r_html,"html.parser")
       for file in soup.find_all('a',class_="link"):
         if file_format in file.text:
           get_book=file.get('href')
           g = requests.get("https:"+get_book)

           with open("books"+str(book_no)+".txt",'wb') as open_file:
               for chunk in g.iter_content(10000):
                    open_file.write(chunk)


def main():
    go_gutenberg("Text",1000)

if __name__=="__main__":main()