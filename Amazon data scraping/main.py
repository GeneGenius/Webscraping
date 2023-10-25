import requests
from bs4 import BeautifulSoup

url = "https://www.amazon.com/Amazfit-Android-Satellite-Positioning-Water-Resistant/product-reviews/B09X1NN4YS/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0',
    'Accept-Language': 'en-US, en;q=0.5'
}

response = requests.get(url, headers=HEADERS)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    reviews = []
    
    # Locate the HTML elements for reviewer names and reviews
    review_elements = soup.find_all('div', class_='a-section celwidget')
    for review in review_elements:
        reviewer_name = review.find('span', class_='a-profile-name').text
        review_text = review.find('span', class_='a-size-base review-text review-text-content')
        
        # Store the data in a dictionary
        review_data = {'Reviewer Name': reviewer_name, 'Review': review_text}
        reviews.append(review_data)

    # You can print the data or save it to a file
    for review in reviews:
        print(review)
#a-section a-spacing-none review-views celwidget'
else:
    print("Failed to retrieve the webpage.")
