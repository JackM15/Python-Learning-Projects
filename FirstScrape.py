#import beautifulsoup4 as bs and urllib requests
import bs4 as bs
import urllib.request

#set a source page to scrape
source = urllib.request.urlopen("https://pythonprogramming.net/parsememcparseface/").read()

#now create the "soup".. aka the beautiful soup object, with the arguments of the url and format
soup = bs.BeautifulSoup(source,'html.parser')

################################################################################################
#Printing Section?

#title of the page
print(soup.title)
#page attributes
print(soup.title.name)
#page values
print(soup.title.string)
#beginning navigation
print(soup.title.parent.name)
#getting specific values, this finds a paragraph
print(soup.p)

#Finding all paragraphs!
print(soup.find_all('p'))

#iterating through paragraphs
for paragraph in soup.find_all('p'):
    print(paragraph.string)
    print(str(paragraph.text))

#We can also grab links!
for url in soup.find_all('a'):
    print(url.get('href'))

#we can also just grab text (using get.text())
print(soup.get_text())

