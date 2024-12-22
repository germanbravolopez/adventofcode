import requests
from bs4 import BeautifulSoup

filename = 'input.txt'
login_url = 'https://adventofcode.com/auth/login'
data_url = 'https://adventofcode.com/2024/day/10/input'
username = 'germanbravolopez'
password = 'xofjok-caswyM-vomby1'

# Create a session
session = requests.Session()

# Prepare the payload for login
payload = {
    'username': username,
    'password': password
}

headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

# Log in to the website
response = session.post(login_url, data=payload)
print(response.text)

# Check if login was successful
if response.ok:
    print("Login successful!")

    # Now access the user-specific content
    data_response = session.get(data_url, headers=headers)

    print(f"Response Content: {data_response.text}")

    # Check if the request was successful
    if data_response.ok:
        # Parse the content
        soup = BeautifulSoup(data_response.text, 'html.parser')
        text = soup.get_text()

        # Save the text to a file
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(text)
        print(f"Text from {data_url} has been saved to {filename}")

        print("User-specific content has been saved to output.txt")
    else:
        print("Failed to retrieve user-specific content.")
else:
    print("Login failed. Check your credentials.")