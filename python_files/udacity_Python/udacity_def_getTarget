def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1:
        return None, 0
    else:
        ##start_link = page.find('<a href=')
        start_quote = page.find('"', start_link)
        end_quote = page.find('"', start_quote + 1)
        url = page[start_quote + 1 : end_quote]
        return url, end_quote

##print(get_next_target('this is a <a href="http://ptrickg.com/links">link!</a>'))

##url, endpos = get_next_target('gobberlobler')
##print(url)

def print_all_links(page):
    while True:
        url, endpos = get_next_target(page)
        if url:
            print(url)
            page = page[endpos:]
        else:
            break
print_all_links("http://ptrickg.com/links")

##url, endpos = get_next_target('this is a <a href="http://ptrickg.com">link!</a>')
##print url
