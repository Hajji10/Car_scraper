import requests
from bs4 import BeautifulSoup

def scrape_car_data(desired_make, desired_model, max_price):
    # Construct the search URL using the input parameters
    search_url = f"https://www.bilbasen.dk/brugt/bil?IncludeEngrosCVR=true&PriceTo={max_price}&includeLeasing=false&free={desired_make}%20{desired_model}"


    
    response = requests.get(search_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        car_data = []

        # Find the elements containing car data from the search results
        car_elements = soup.find_all("div", class_="car-item")

        for car_element in car_elements:
            # Extract car make, model, year, and price (adjust the HTML structure based on the website)
            make = car_element.find("span", class_="car-make").text
            model = car_element.find("span", class_="car-model").text
            year = car_element.find("span", class_="car-year").text
            price = car_element.find("span", class_="car-price").text

            car_data.append({"make": make, "model": model, "year": year, "price": price})

        return car_data
    else:
        print(f"Error: Failed to fetch data from {search_url}")
        return []

def main():
    # User input: Desired car make, model, and maximum price
    desired_make = input("Enter desired car make: ")
    desired_model = input("Enter desired car model: ")
    max_price = float(input("Enter maximum price: "))

    # Scrape car data based on user's search criteria
    car_data = scrape_car_data(desired_make, desired_model, max_price)

    # Display the scraped car data on the console
    for car in car_data:
        print(f"Make: {car['make']}, Model: {car['model']}, Year: {car['year']}, Price: {car['price']}")

if __name__ == "__main__":
    main()
