from django.shortcuts import render
from proxy.secondary_functions import download_hn_page


def download_page(request):
    requested_url = request.GET["url"]
    page_title = requested_url.split("https://news.ycombinator.com/")[1]
    page_filename = f"{page_title}.html"
    download_hn_page(request, requested_url, page_filename)
    return render(request, page_filename)


def get_main_page(request):
    requested_url = "https://news.ycombinator.com/"
    page_filename = "main.html"
    download_hn_page(request, requested_url, page_filename)
    return render(request, page_filename)



