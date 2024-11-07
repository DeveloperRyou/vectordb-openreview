import urllib.request
import pymupdf4llm
import pathlib
import db.mysql.repository as mysql_repository

def download_pdf(key, pdf_url):
    urllib.request.urlretrieve(pdf_url, f"./pdf/{key}.pdf")

def pdf_to_text(key, pdf_url):
    download_pdf(key, pdf_url)
    md_text = pymupdf4llm.to_markdown(f"./pdf/{key}.pdf")
    return md_text

def save_md_text(key, md_text):
    pathlib.Path(f"./pdf/{key}.md").write_bytes(md_text.encode())


def initialize_pdf(mysql_db):
    forum_list = mysql_repository.find_all_forum(mysql_db)
    print(len(forum_list))
    for forum in forum_list[:20]:
        pdf_url = forum["pdf"]
        pdf_key = forum["pdf"].split("/")[-1].split(".")[0]
        md_text = pdf_to_text(pdf_key, pdf_url)
        save_md_text(pdf_key, md_text)
        
