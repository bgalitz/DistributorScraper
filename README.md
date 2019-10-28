# DistributorScraper
Web Scraper in Python to pull current onhand qtys

We changed distribution to Medline and they claim it's not possible to provide a daily file with their onhand qty's of the stock they are supposed to be keeping for our hospital.
They do provide us access to view these thru their website but only if we view an item one-at-a-time.
We need to pull this data daily to forecast any issues.
The scraper takes the DED list and pulls each item up in their website and scrapes the onhand qty.
It then puts it into a separate file that is emailed to our Supervisor team.

In a nutshell:
1) Log into Medline website
2) Open DED file
3) Loop thru DED file one item at a time
4) Search item on the website
5) Find ONHAND QTY in page
6) Copy to file
7) Repeat until file completely read
8) End loop and close files
9) Send file to leadership team
