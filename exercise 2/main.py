from bs4 import BeautifulSoup
import requests
import time

def find_jobs():
    html_text = requests.get('https://www.jobberman.com/jobs?q=python&_token=9o0rN5wlQWz6JeIVG0A6lXfuoLOcHI7S4ZkF49Ul&_method=GET').text
    #print(html_text)
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('div', class_= 'mx-5 md:mx-0 flex flex-wrap col-span-1 mb-5 bg-white rounded-lg border border-gray-300 hover:border-gray-400 focus-within:ring-2 focus-within:ring-offset-2 focus-within:ring-gray-500')
    for index, job in enumerate(jobs):
        job_published_date = job.find('p', class_ = 'ml-auto text-sm font-normal text-gray-700 text-loading-animate').text. replace('','')
        company_name = job.find('p', class_ = 'text-sm text-link-500').text.replace('', '')
        job_function = job.find('p', class_ = 'text-sm text-gray-500 text-loading-animate inline-block').text.replace('','')
        location = job.find('span', class_='mb-3 px-3 py-1 rounded bg-brand-secondary-100 mr-2 text-loading-hide').text.replace('','')
        with open('posts/{index}.txt', 'w') as f:
            f.write(f"Company Name:{company_name.strip()} \n")
            f.write(f"Location: {location.strip()} \n")
            f.write(f"{job_function.strip()} \n")
            f.write(f"Published date: {job_published_date.strip()} \n")
        print(f'File saved:{index}')


if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'Waiting {time_wait} minutes...')
        time.sleep(time_wait * 60)