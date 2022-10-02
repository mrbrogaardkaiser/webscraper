import requests
from bs4 import BeautifulSoup


# url from site
URL = 'https://www.it-jobbank.dk/jobsoegning/udvikling'

page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id='result_list_box')

# Variable contains the number of pages in the paginator
page_links = len(results.find_all('a', class_='page-link'))

# Looping through the pages extracting the data we need
for i in range(page_links):
    page = requests.get(URL+f'?page={str(i+1)}')
    soup = BeautifulSoup(page.content, "html.parser")
    page_data = soup.find(id='result_list_box')
    jobs = page_data.find_all('p', string=lambda text:'java' in text.lower())
    job_elements = [p_element.parent.parent for p_element in jobs]
    
    for job_element in job_elements:
        title_element = job_element.find("h3", class_="job-title")
        company_element = job_element.find('div', class_="job-company")
        location_element = job_element.find("span", class_="job-location")
        body_element = job_element.find("div", class_="job-body")
        print(title_element.text.strip())
        print(company_element.text.strip())
        print(location_element.text.strip())
        print(body_element.text.strip())
        print()
        link_url = job_element.find_all('a')[1]['href']
        print(f'Go to add: {link_url}\n')
