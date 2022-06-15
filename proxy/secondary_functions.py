from django.shortcuts import render
from bs4 import BeautifulSoup
from django.http import HttpResponse
import requests
from fake_useragent import UserAgent
import os
import string


USERAGENT = UserAgent().random
HEADERS = {"User-Agent": USERAGENT}


def get_edited_string(raw_string):
    elements = raw_string.split()
    new_elements = []
    special_symbol = "™"
    for element in elements:
        last_symbol = element[-1]
        first_symbol = element[0]
        if len(element) == 7 and last_symbol in string.punctuation:
            element = element.strip(last_symbol)
            new_element = f"{element}{special_symbol}{last_symbol}"
            new_elements.append(new_element)
        elif len(element) == 7 and first_symbol in string.punctuation:
            element = element.strip(first_symbol)
            new_element = f"{first_symbol}{element}{special_symbol}"
            new_elements.append(new_element)
        elif len(element) == 8 and first_symbol in string.punctuation and last_symbol in string.punctuation:
            element = element.strip(first_symbol).strip(last_symbol)
            new_element = f"{first_symbol}{element}{special_symbol}{last_symbol}"
            new_elements.append(new_element)
        elif len(element) == 6 and element.isalpha():
            new_element = f"{element}{special_symbol}"
            new_elements.append(new_element)
        else:
            new_elements.append(element)
    edited_string = " ".join(new_elements)
    return edited_string



def include_static(html_markup):
    stylesheet = html_markup.find("link", rel="stylesheet")
    stylesheet["href"] = "{% static 'news.css' %}"
    shortcut_icon = html_markup.find("link", rel="shortcut icon")
    shortcut_icon["href"] = "{% static 'favicon.ico' %}"
    logo = html_markup.find(
        "a", href="https://news.ycombinator.com").find("img")
    logo["src"] = "{% static 'y18.gif' %}"
    site_js = html_markup.find("script", type="text/javascript")
    site_js["src"] = "{% static 'hn.js' %}"
    s_gif = html_markup.find("img", src="s.gif")
    s_gif["src"] = "{% static 's.gif' %}"


def download_hn_page(request, requested_url, page_name):
    page_directory = "pages"
    response = requests.get(requested_url, HEADERS)
    response.raise_for_status()
    html_markup = BeautifulSoup(response.text, "lxml")
    tags = html_markup.find_all()
    include_static(html_markup)
    for tag in tags:
        tag_string = tag.string
        if tag_string == None:
            continue
        tag.string = get_edited_string(tag.string)
    update_hackernews_urls_tags(html_markup)
    file_name = os.path.join(page_directory, page_name)
    with open(file_name, "w", encoding="utf-8") as file:
        file.write(str(html_markup))
    with open(file_name, "r", encoding="utf-8") as file:
        source = file.readlines()
        static_tag = ["{% load static %}"]
        static_tag = ''.join(static_tag) + '\n' + '\n'
        source.insert(0, static_tag)
        with open(file_name, "w", encoding="utf-8") as file:
            file.writelines(source)


def update_hackernews_urls_tags(html_markup):
    site_urls = ["https://news.ycombinator.com", "newest", "front",
                 "newcomments", "ask", "show", "jobs",
                 "newsguidelines.html", "newsfaq.html", "lists", "security.html", ]


    urls_tags = html_markup.find_all("a")
    main_page_url = site_urls[0]
    for url_tag in urls_tags:
        if url_tag["href"] == main_page_url:
            pass
        elif url_tag["href"] == "submit":
            url_tag["href"] = f"{main_page_url}/submit"
        elif url_tag["href"] in site_urls:
            url_tag["href"] = "{% url 'download_page' %}" + \
                "?url=https://news.ycombinator.com/{}".format(url_tag["href"])
