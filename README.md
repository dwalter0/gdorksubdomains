# gdorksubdomains

Python script that does the following search on google `sitename:<input> -www` and scrapes results to find subdomains.

There will be some google links in your results that you'll need to filter out.

HTTPs errors are suppressed for complications in proxying.

Usage: python3 gdorksubdoms.py \<site\> \<pages of results to check\><br>
eg. python3 gdorksubdoms.py tesla.com 4
