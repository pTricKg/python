def print_all_links(page):
    while start_link == 1:
        url, endpos = get_next_target(page)
        if url:
            print(url)
            page = page[endpos:]
        else:
            return None, 0
