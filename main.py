from bs4 import BeautifulSoup as soup
from urllib import request as req

my_url = req.urlopen('https://www.reddit.com/r/Awww/')
o_file = open('./images.txt', 'w')

def main():
    page = soup(my_url, 'html.parser')
    images = page.findAll(attrs={'alt': 'Post image'})
    vids = page.findAll('video', class_='_1EQJpXY7ExS04odI1YBBlj')

    for image in images:
        print()
        print(image['src'])
        
        o_file.write('[IMAGE]\n{}\n\n'.format(image['src']))
    
    o_file.write('\n\n')

    for vid in vids:
        print()
        print(vid.source['src'])

        o_file.write('[VID]\n{}\n\n'.format(vid['src']))
        

    o_file.close()
     
if __name__ == "__main__":
  main()
