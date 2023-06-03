from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import csv

def scrape_carsales(html_content):

    soup = BeautifulSoup(html_content, 'html.parser')

    # print(soup)
    try:
        full_listings = soup.find_all('div', class_='listing-items')[0]
    except:
        print(soup)
        filename = f"html_content.txt"
        with open(filename, "w") as file:
            file.write(html_content)

    cars = full_listings.find_all('div', {"class":['listing-item card showcase', 'listing-item card standard']})
    print("Found ", len(cars), " cars")

    for car in cars:
        # print("------------------------------")
        # print(car)
        body = car.find('div', class_='card-body')
        # print(body)
        title_block = body.find('h3')
        title = title_block.text.strip()
        link_cell = title_block.a
        link = "https://www.carsales.com.au/" + link_cell.get('href')
        price = body.find('div', class_='price').text.replace(',', '')
        odo = body.find("li", attrs={"data-type": "Odometer"}).text
        transmission = body.find("li", attrs={"data-type": "Transmission"}).text
        body_style = body.find("li", attrs={"data-type": "Body Style"}).text
        engine = body.find("li", attrs={"data-type": "Engine"}).text

        footer = car.find('div', class_='card-footer')
        location = footer.find("div", attrs={"class": "seller-location d-flex"}).text

        images = car.find_all('img')
        # print(images)

        # print("odo = ", odo)
        listing = [title, transmission, price, odo, body_style, engine, location, link]
        listing_str = ', '.join(listing)
        listing_str = listing_str.replace('\n', '')
        print(listing_str)

        # Save the HTML to a text file

        # with open("Subaru_impreza.csv", "a") as file:
        #     file.write(listing)

        with open("Subaru_impreza.csv", 'a', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(listing)

        # print(price)

        car_list.append(title)

# Set up the Selenium WebDriver (make sure you have the appropriate driver installed)
driver = webdriver.Chrome()  # Change to the appropriate WebDriver for your browser

# Navigate to the initial page

page_default = "https://www.carsales.com.au/cars/subaru/impreza/?sort=~Price&offset={}"


# Perform your search and get the total number of pages
# Replace the following code with your own search criteria and logic

# print(driver)

# search_input = driver.find_element(By.ID, "search-input")
# search_input.send_keys("car")
# search_button = driver.find_element(By.ID, "search-button")
# search_button.click()

offset = 12  # Replace with the actual total number of pages for your search

# Loop through each page
car_list = []

for page_num in range(1000):
    # Get the current page HTML

    search_page = page_default.format(offset*page_num)

    print("Searching page: ", search_page)

    driver.get(search_page)
    page_html = driver.page_source

    scrape_carsales(page_html)

    # Save the HTML to a text file
    # filename = f"page_{page_num}.txt"
    # with open(filename, "w") as file:
    #     file.write(page_html)


# Close the browser
driver.quit()
