from bs4 import BeautifulSoup

soup = BeautifulSoup(open("sina_index.html"))
a_tag_list = soup.find_all("a")
for a_tag in a_tag_list:
    if len(a_tag.contents)>0:
        print a_tag.contents[0]
    if "href" in a_tag.attrs:
        print a_tag["href"]
