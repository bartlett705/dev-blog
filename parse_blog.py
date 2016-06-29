'''
Turn simple yaml-formatted journal entries into html.
29 Jun 2016
Ahmad Kanawi
'''


import yaml
from base_markup import header, footer, index_header, index_footer
input_file = 'blog.yaml'

inp = file(input_file, 'r')

data = yaml.load_all(inp)

toc = []
idx = 0
tag_dict = {}

index_markdown = index_header

for post in data: # Build a table of contents
    if post['publish']:
        output_file = ('-'.join(post['title'].split(' ')) + '.html').lower()
        toc.append((post['title'], output_file, post['timestamp'], post['body'], post['tags'], idx))
        idx += 1
        
print toc
for title, link, timestamp, body, tags, index in toc: # Traverse posts again to build individual pages
    previous_post_idx = index - 1
    if previous_post_idx < 0:
        previous_post_idx = len(toc) - 1
    next_post_idx = index + 1
    if next_post_idx == len(toc):
        next_post_idx = 0
    print previous_post_idx, next_post_idx
    marked_down = header
    marked_down += '<div class="entry">\n'
    marked_down += '\t<h1>' + title + '</h1>\n'
    marked_down += '\t<strong>Posted:</strong>' + timestamp + '\n'
    marked_down += '\t<p class="post-body">' + body + '\n'
    marked_down += '\t<div class="tags">' + '\n'
    for tag in tags:
        print tag
        marked_down += '\t\t<div class="tag">' + tag + '</div>\n'
        if tag in tag_dict:
            tag_dict[tag].append((title, link))
        else:
            tag_dict[tag] = [(title, link)]
    marked_down += '\t</div>\n</div>\n'
    marked_down += '<div class="navbar">\n'
    marked_down += '\t&laquo;<a href="'+ toc[previous_post_idx][1] + '">' + toc[previous_post_idx][0] + '</a> | <a href="index.html">Contents</a> |<a href="' + toc[next_post_idx][1] + '">' + toc[next_post_idx][0] + '</a> &raquo;\t'
    marked_down += '</div>'                                                                                                                                                     
    marked_down += footer

    index_markdown += '<li class="toc_entry">[' + timestamp + '] :\
    <a href="' + link + '"><strong>' + title + '</strong></a></li>'
    of = file(link, 'w')
    of.write(marked_down)
    of.close()

index_markdown += '<h2>Tags</h2><div class="tag-list"><ul>'
for tag in tag_dict:
    index_markdown += '<li class="tag-name">'+ tag + ' : <div class="tagged-posts">'
    for title, link in tag_dict[tag] :
        index_markdown += '<a href="' + link + '">' + title + '</a>, '
    index_markdown = index_markdown[:-2]
index_markdown += '</div></ul></div>'
index_markdown += index_footer
index_file = file('index.html', 'w')
index_file.write(index_markdown)
index_file.close()

print tag_dict
print '''
===============
=Happy Trails!=
===============
'''
