import requests
from bs4 import BeautifulSoup

filename = 'website_output.txt'
login_url = 'https://centrocomercio.sierranevada.es/auth/login'
data_url = 'https://centrocomercio.sierranevada.es/tienda-invierno'

# Create a session
session = requests.Session()
username = 'gebralo@hotmail.com'
password = input("Enter your password: ")

# Prepare the payload for login
payload = { 'username': username, 'password': password }

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
           (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

# Log in to the website
response = session.post(login_url, data=payload)
with open('login_response_log.txt', 'w', encoding='utf-8') as file:
    file.write(response.text)

if response.ok:
    print("Login successful!")

    # Now access the user-specific content
    data_response = session.get(data_url, headers=headers)
    with open('data_response_log.txt', 'w', encoding='utf-8') as file:
        file.write(data_response.text)

    # Check if the request was successful
    if data_response.ok:
        # Parse the content and save to a file
        soup = BeautifulSoup(data_response.text, 'html.parser')
        text = soup.get_text()
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(text)
        print(f"Text from {data_url} has been saved to {filename}")
    else:
        print("Failed to retrieve user-specific content.")
else:
    print("Login failed. Check your credentials.")
