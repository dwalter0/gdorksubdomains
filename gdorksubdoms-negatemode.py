import sys
import requests
import re
from urllib.parse import urlparse
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from random import randint
from time import sleep

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
    
def get_subdomain_list(urls):
    ret = []
    for url in urls:
        parsed_url = urlparse(url)
        ret.append(parsed_url.netloc.split('.')[0])
    return ret

def go(target_url):
    # Make the GET request to the website
    response = make_get_request(target_url)
    urls = (extract_urls(response))
    results = []
    for url in urls:
        results.append(remove_url_path(url))
    return results

def get_negations(subdomains):
    if len(subdomains) == 0:
        return ""
    else:
        return '+-'+'+-'.join(subdomains)

if __name__ == "__main__":
    
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    
    if len(sys.argv) == 3:
        pages = int(sys.argv[2])
        loops = 0
        results = pages * 10
        
        domains = []
        subdomains = []
        
        while loops < results:
            negations = get_negations(subdomains)
            target_url = f"https://www.google.com/search?q=site:{sys.argv[1]}+-www{negations}"       
            result_urls = go(target_url)
            non_google_result_urls = list(filter(lambda link: "google" not in link,result_urls))
            domains.extend(non_google_result_urls)
            domains = [x for i, x in enumerate(domains) if x not in domains[:i]]
            subdomains.extend(get_subdomain_list(domains))
            subdomains = [x for i, x in enumerate(subdomains) if x not in subdomains[:i]]
            loops += 10
            
        for item in domains:
            print(item)
    
    else:
        print("Usage: python3 gdorksubdoms.py <site> <pages of results to check>")
        print("eg. python3 gdorksubdoms.py tesla.com 4")



