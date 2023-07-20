# gdorksubdomains

Python script that does the following search on google `site:<input> -www` and scrapes results to find subdomains.

HTTPs errors are suppressed for complications in proxying.

Usage: python3 gdorksubdoms.py \<site\> \<pages of results to check\><br>
eg. python3 gdorksubdoms.py tesla.com 4

# gdorksubdomains-negatemode

A colleague gave me the idea for this addition. Does the same thing but instead of looking through pages, adds negations of found subdomains for each subsequent search. Generally more results are given with this but I've seen the gdorksubdomains version return some results that negatemode doesn't for the same number of requests.

Usage: python3 gdorksubdoms-negatemode.py \<site\> \<number of searches to run\><br>
eg. python3 gdorksubdoms-negatemode.py tesla.com 4
<hr>
You may get some 429 Too Many Requests responses if you choose too high a number on the end.<br>
This won't work if you're looking for subdomains of google because it filters out google links.
