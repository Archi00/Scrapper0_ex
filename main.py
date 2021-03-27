from bs4 import BeautifulSoup as soup
import urllib.request as req

my_url = req.urlopen('https://www.reddit.com/r/Awww/')
fd = open('./images.html', 'w')

def main():
  page = soup(my_url, 'html.parser')
  images = page.findAll(['img', 'src'])
  print(images['alt'])

  for each in images:
    url = each['src']
    fd.write("""
          <div>
            <img alt="" src="{}"
          </div>
        """.format(url))
  fd.close()

if __name__ == "__main__":
  main()