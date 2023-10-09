import os
import requests
from bs4 import BeautifulSoup

# Define the parameters for the loop
start_page = 0

while start_page <= 1600:
    # Create the URL for the current page
    page_url = f'https://universe.roboflow.com/llama/bowler-detection-u0brx/browse?queryText=class%3AScoreCards&pageSize=200&startingIndex={start_page}&browseQuery=true'
    
    # Send an HTTP GET request to the webpage
    response = requests.get(page_url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the webpage using BeautifulSoup
        soup = BeautifulSoup(response.content, "html.parser")

        # Directory to save downloaded images
        download_directory = 'downloaded_images'
        os.makedirs(download_directory, exist_ok=True)

        # Counter for naming downloaded files
        counter = 1

        # Find all image tags (e.g., <img src="...">) on the webpage
        img_tags = soup.find_all("img")
        print(soup)
        for img_tag in img_tags:
            # Get the image URL from the "src" attribute
            image_url = img_tag.get("src")

            if image_url:
                # Download the image
                image_response = requests.get(image_url)

                if image_response.status_code == 200:
                    # Determine the file extension (e.g., jpg, png)
                    file_extension = image_url.split(".")[-1]

                    # Save the image to the download directory
                    with open(os.path.join(download_directory, f'image{counter}.{file_extension}'), 'wb') as f:
                        f.write(image_response.content)
                    print(f"Downloaded image{counter}.{file_extension}")
                    counter += 1
                else:
                    print(f"Failed to download {image_url}")
    else:
        print(f"Failed to retrieve content from {page_url}")

    start_page += 200
