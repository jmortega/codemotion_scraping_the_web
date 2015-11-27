#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from lxml import html
import getpass

username = raw_input ("Username: ")
password = getpass.getpass()

LOGIN_URL = "https://bitbucket.org/account/signin/?next=/"
URL = "https://bitbucket.org/dashboard/overview"

def main():
    session_requests = requests.session()

    # Get login csrf token
    result = session_requests.get(LOGIN_URL)
    tree = html.fromstring(result.text)
    authenticity_token = list(set(tree.xpath("//input[@name='csrfmiddlewaretoken']/@value")))[0]

    # Create payload
    payload = {
        "username": username, 
        "password": password, 
        "csrfmiddlewaretoken": authenticity_token
    }

    # Perform login
    result = session_requests.post(LOGIN_URL, data = payload, headers = dict(referer = LOGIN_URL))

    # Scrape url
    result = session_requests.get(URL, headers = dict(referer = URL))
    tree = html.fromstring(result.content)
    bucket_elems = tree.findall(".//a[@class='execute']")
    bucket_names = [bucket_elem.text_content().replace("\n", "").strip() for bucket_elem in bucket_elems]

    print bucket_names

if __name__ == '__main__':
    main()