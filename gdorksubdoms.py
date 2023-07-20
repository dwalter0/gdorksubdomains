import sys
import requests
import re
from urllib.parse import urlparse
from requests.packages.urllib3.exceptions import InsecureRequestWarning

def make_get_request(url):
    try:
        response = requests.get(url, verify=False)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Print the content of the response (HTML content for a website)
            return response.text
        else:
            print(f"Request failed with status code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

def extract_urls(text):
    pattern = r'https?://\S+'  # This regex pattern matches URLs starting with "http://" or "https://" and followed by non-space characters.
    urls = re.findall(pattern, text)
    return urls

def remove_url_path(url):
    parsed_url = urlparse(url)
    scheme = parsed_url.scheme
    netloc = parsed_url.netloc
    return f"{scheme}://{netloc}"

def go(target_url):
    # Make the GET request to the website
    response = make_get_request(target_url)
    urls = (extract_urls(response))
    results = []
    for url in urls:
        results.append(remove_url_path(url))
    return results


if __name__ == "__main__":
    
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    
    if len(sys.argv) == 3:
        pages = sys.argv[2]
        loops = 0
        results = pages * 10
        
        domains = []
        
        while loops < results:
            # Replace this URL with the website you want to access
            target_url = f"https://www.google.com/search?q=site:{sys.argv[1]}+-www&start={loops}"       
            domains.extend(go(target_url))
            loops += 10
            
        unique_list = [x for i, x in enumerate(domains) if x not in domains[:i]]
        for item in unique_list:
            print(item)
    
    else:
        print("Usage: python3 gdorksubdoms.py <site> <pages of results to check>")
        print("eg. python3 gdorksubdoms.py tesla.com 4")



