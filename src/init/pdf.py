import urllib.request
import db.mysql.repository as mysql_repository

def download_pdf(pdf_url):
    urllib.request.urlretrieve(pdf_url, f"./pdf/{pdf_url.split('/')[-1]}")

def pdf_to_text(pdf_url):
    return "This is a text from pdf"

def initialize_pdf(mysql_db):
    forum_list = mysql_repository.find_all_forum(mysql_db)
    print(len(forum_list))
    for forum in forum_list[:2]:
        pdf_url = forum["pdf"]
        download_pdf(pdf_url)
        
    
