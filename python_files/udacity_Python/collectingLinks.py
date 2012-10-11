##collecting links
def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote

##def print_all_links(page):
##    while True:
##        url, endpos = get_next_target(page)
##        if url:
##            print url
##            page = page[endpos:]
##        else:
##            break


def get_all_links(page):
    links = []
    while True:
        url, endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links

def crawl_web(seed):
	tocrawl = [seed]
	crawled = [ ]
	while tocrawl:
		page = tocrawl.pop()
		if page not in crawled:
			#update tocrawl and crawled
			#should only be two lines
	return crawled
