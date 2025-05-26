# Import the urllib3 library
import urllib3

def handle_redirects():
    # Create a PoolManager instance
    http = urllib3.PoolManager()

    # Define the initial URL that may redirect
    initial_url = 'https://github.com/frorth-aliceb/poison-cache/blob/main/True%20Identity.png'

    try:
        # Make a GET request with allow_redirects set to True
        response = http.request('GET', initial_url, redirect=True)

        # Check if the request was successful (status code 200)
        if response.status == 200:
            # Print the final response URL after following redirects
            print("Final Response URL:")
            print(response.geturl())
        else:
            # Print an error message if the request was not successful
            print(f"Error: Unable to fetch data. Status Code: {response.status}")

    except urllib3.exceptions.RequestError as e:
        print(f"Error: {e}")
