'''
Turn simple yaml-formatted journal entries into html.
29 Jun 2016
Ahmad Kanawi
'''


import yaml
from base_markup import post_header, post_footer, index_header, index_footer
input_file = 'blog.yaml'

inp = file(input_file, 'r')

data = yaml.load_all(inp)

toc = []
idx = 0
tag_dict = {}
unpublished = 0

index_markdown = index_header

for post in data: # Build a table of contents
    print 'Extracting data from ' + input_file + '...'
    if post['publish']:
        output_file = ('-'.join(post['title'].split(' ')) + '.html').lower()
        toc.append((post['title'], output_file, post['timestamp'], post['body'], post['tags'], idx))
        idx += 1
    else:
        unpublished += 1
        
for title, link, timestamp, body, tags, index in toc: # Traverse posts again to build individual pages
    print 'Generating Post Pages...'
    previous_post_idx = index - 1
    if previous_post_idx < 0:
        previous_post_idx = len(toc) - 1
    next_post_idx = index + 1
    if next_post_idx == len(toc):
        next_post_idx = 0
    marked_down = post_header
    marked_down += '<div class="entry">'
    marked_down += '\t<h1>' + title + '</h1>'
    marked_down += '\t<p class="timestamp">[' + timestamp + ']</p>'
    marked_down += '\t<p class="post-body">' + body + '</p>'
    marked_down += '</div>'
    marked_down += '\t<div class="tags">' + '\n'
    for tag in tags:
        marked_down += '\t\t<div class="tag">' + tag + '</div>'
        if tag in tag_dict:
            tag_dict[tag].append((title, link))
        else:
            tag_dict[tag] = [(title, link)]
    marked_down += '\t\n</div>'
    marked_down += '<br><hr><div class="navbar">'
    marked_down += '\t&laquo; <a href="'+ toc[previous_post_idx][1] + '">' + toc[previous_post_idx][0] + '</a> | <a href="index.html">Contents</a> |<a href="' + toc[next_post_idx][1] + '">' + toc[next_post_idx][0] + '</a> &raquo;\t'
    marked_down += '</div>'                                                                                                                                                     
    marked_down += post_footer

    index_markdown += '<li class="toc_entry">[' + timestamp + '] :\
    <a href="' + link + '"><strong>' + title + '</strong></a></li>'
    of = file(link, 'w')
    of.write(marked_down)
    of.close()

print 'Generating index...'

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

print 'Posts (unpublished):', len(toc), '(', unpublished, ')'
print 'Tags:', tag_dict.keys()
print '''
===============
=Happy Trails!=
===============
'''
