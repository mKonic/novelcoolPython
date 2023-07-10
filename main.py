import requests
import bs4
import lxml
link = 'https://en.novelcool.com/category/popular.html'

novelcool =requests.get(link)

source = bs4.BeautifulSoup(novelcool.text,'lxml')

divs = source.find_all('div', class_="book-item")
for div in divs:
    div = str(div)
    
    soup = bs4.BeautifulSoup(div,'lxml')
    link = soup.find('a')
    cover = soup.find('img')
    type_ = soup.find('div', class_="book-type")
    name = soup.find('div', class_="book-name")
    modified = soup.find('div', class_="book-data-time")
    summary = soup.find('div', class_="book-summary-content")
    cover = str((str(cover).split(' '))).split('"')[7]
    soup = bs4.BeautifulSoup(str(link),'lxml')
    genres = soup.find_all('div', class_="book-tag")
    gen=[]
    for genre in genres:
        gen.append(genre.text)
    
    link = str((str(link).split(' '))).split('"')[1]
        
    book = {'link':link,'cover_ulr':cover,'type':type_.text,'tittle': name.text,'genres':gen,'summary':summary.text,'last_modified': modified.text}
    print(book) 