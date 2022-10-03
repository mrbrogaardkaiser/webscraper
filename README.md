# Webscraper
Web scraper with BeautifulSoup4. Scraping job adds for Java development 

Clone repository\
$ git clone https://github.com/mrbrogaardkaiser/webscraper.git

Cd in to directory\
$ cd webscraper

Build image based on repositorys Dockerfile\
$ docker build --tag kaiser/scraper .

Run container based on image\
$ docker run -it --rm -v ${PWD}:/docs kaiser/scraper ash
