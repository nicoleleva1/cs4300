import requests

# uses the requests package to make an HTTP GET request
# and returns the status code from the response
def get_status_code(url):
    response = requests.get(url)
    return response.status_code