##page = <some website>
##start_link = page.find('<a href=')
##start_quote = page.find('"', start_link)
##end_quote = page.find('"', start_quote + 1)
##url = page[start_quote + 1 : end_quote]
##start_link = page.find('<a href=')

def print_all_links(page):
    while True:
        url, endpos = get_next_target(page)
        if url:
            print(url)
            page = page[endpos:]
        else:
            break
print_all_links("http://ptrickg.com")
