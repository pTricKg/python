##page = <some website>
##start_link = page.find('<a href=')
##start_quote = page.find('"', start_link)
##end_quote = page.find('"', start_quote + 1)
##url = page[start_quote + 1 : end_quote]
##print url
##start_link = page.find('<a href=')
##page = page[end.quote : ]
##start_link// .......multi-assign <name>.2.3.. = <expression>.2.3...

## a, b = 1, 2
##url , endpos = get_next_target(page)

def get_next_target(page):
    start_link = page.find('<a href=')
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1 : end_quote]
    return url, end_quote
##print(get_next_target('this is a <a href="http://ptrickg.com">link!</a>'))
url, endpos = get_next_target('this is a <a href="http://ptrickg.com">link!</a>')
print(url)
