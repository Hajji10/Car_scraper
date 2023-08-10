import requests
from bs4 import BeautifulSoup

def scrape_car_links(desired_make, desired_model, max_price):
    # Construct the search URL using the input parameters
    search_url = f"https://www.bilbasen.dk/brugt/bil?IncludeEngrosCVR=true&PriceTo={max_price}&includeLeasing=false&free={desired_make}%20{desired_model}"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    
    response = requests.get(search_url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        car_links = []

        # Find the elements containing car data from the search results
        car_elements = soup.find_all("div", class_="car-item")

        for car_element in car_elements:
            # Extract the link for each car listing
            car_link = car_element.find("a", class_="car-link")["href"]
            car_links.append(car_link)

        return car_links
    else:
        print(f"Error: Failed to fetch data from {search_url}")
        return []

def main():
    # User input: Desired car make, model, and maximum price
    desired_make = input("Enter desired car make: ")
    desired_model = input("Enter desired car model: ")
    max_price = float(input("Enter maximum price: "))

    # Scrape car links based on user's search criteria
    car_links = scrape_car_links(desired_make, desired_model, max_price)

    # Display the scraped car links on the console
    for link in car_links:
        print(link)

if __name__ == "__main__":
    main()