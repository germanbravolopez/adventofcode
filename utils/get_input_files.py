import requests
from bs4 import BeautifulSoup

def fetch_and_save_text(url, filename):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }

        # Send a GET request to the URL with headers
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Check for HTTP errors

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract text from the soup object
        text = soup.get_text()

        # Save the text to a file
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(text)

        print(f"Text from {url} has been saved to {filename}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        response = requests.get(url)
        print(f"Response Content: {response.text}")

# Example usage

url = 'https://adventofcode.com/2024/day/10/input'
filename = 'input.txt'
fetch_and_save_text(url, filename)


# # Replace these with the actual login URL and your credentials
# login_url = 'https://www.example.com/login'  # URL for the login form
# data_url = 'https://www.example.com/data'     # URL for the user-specific data
# username = 'your_username'
# password = 'your_password'

# # Create a session
# session = requests.Session()

# # Prepare the payload for login
# payload = {
#     'username': username,
#     'password': password
# }

# # Log in to the website
# response = session.post(login_url, data=payload)

# # Check if login was successful
# if response.ok:
#     print("Login successful!")

#     # Now access the user-specific content
#     data_response = session.get(data_url)

#     # Check if the request was successful
#     if data_response.ok:
#         # Parse the content
#         soup = BeautifulSoup(data_response.text, 'html.parser')
#         text = soup.get_text()

#         # Save the text to a file
#         with open('output.txt', 'w', encoding='utf-8') as file:
#             file.write(text)

#         print("User-specific content has been saved to output.txt")
#     else:
#         print("Failed to retrieve user-specific content.")
# else:
#     print("Login failed. Check your credentials.")