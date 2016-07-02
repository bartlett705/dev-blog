#!/usr/bin/python2
#Turn simple yaml-formatted journal entries into html.
#29 Jun 2016
#Ahmad Kanawi
#

import yaml, sys, markdown


def format_blog(input_file, output_path):

    from base_markup import post_header, post_footer, index_header, index_footer

    print ('========================================================')
    print ('====== dev-blog - a lightweight web-log formatter ======')
    print ('========================================================')

    toc = []
    idx = 0
    tag_dict = {}
    unpublished = 0

    inp = file(input_file, 'r')

    data = yaml.load_all(inp)

    # The first entry in the YAML file is the blog's info
    blog_info =  next(data)

    # Insert relevant info into templates
    post_header = post_header.replace('{% blog_name %}', blog_info['blog_name'])
    index_header = index_header.replace('{% blog_name %}', blog_info['blog_name'])
    post_footer = post_footer.replace('{% org_name %}', blog_info['org_name']).replace('{% org_link %}', blog_info['org_link'])
    index_footer = index_footer.replace('{% org_name %}', blog_info['org_name']).replace('{% org_link %}', blog_info['org_link'])

    index_markup = index_header

    print ('Extracting posts for [' + blog_info['blog_name'] + '] from ' + input_file + '...')
    for post in data: # Build a table of contents
        if post['publish']:
            output_file = ('-'.join(post['title'].split(' ')) + '.html').lower()
            toc.append((post['title'], output_file, post['timestamp'], post['body'], post['tags'], idx))
            idx += 1
        else:
            unpublished += 1
            
    for title, link, timestamp, body, tags, index in toc: # Traverse posts again to build individual pages
        try:
            print ('Generating Post Page ['+ title + ']...')
            previous_post_idx = index - 1
            if previous_post_idx < 0:
                previous_post_idx = len(toc) - 1
            next_post_idx = index + 1
            if next_post_idx == len(toc):
                next_post_idx = 0
            marked_up = post_header
            marked_up += '<div class="entry">\n'
            marked_up += '\t<h1>' + title + '</h1>\n'
            marked_up += '\t<p class="timestamp">[' + timestamp + ']</p>\n'
            marked_up += '\t<div class="post-body">' + markdown.markdown(unicode(body, "ascii"), output_format="html5", extensions=['markdown.extensions.codehilite', 'markdown.extensions.fenced_code']) + '</div>\n'
            marked_up += '</div>'
            marked_up += '\t<div class="post-tags">' + '\n'
            for tag in tags:
                marked_up += '\t\t<div class="post-tag">' + tag + '</div>\n'
        # These next four lines assemble a dictionary of links to pages with each tag
                if tag in tag_dict:
                    tag_dict[tag].append((title, link))
                else:
                    tag_dict[tag] = [(title, link)]
            marked_up += '\t\n</div>\n'
            marked_up += '<br><hr><div class="navbar">\n'
            marked_up += '\t&laquo; <a href="'+ toc[previous_post_idx][1] + '">' + toc[previous_post_idx][0] + '</a> | <a href="index.html">Contents</a> |<a href="' + toc[next_post_idx][1] + '">' + toc[next_post_idx][0] + '</a> &raquo;\n'
            marked_up += '</div>\n'                                                                                                                                                     
            marked_up += post_footer

            index_markup += '<li class="toc_entry">[' + timestamp + '] :\
            <a href="' + link + '"><strong>' + title + '</strong></a></li>\n'
            of = file(output_path + link, 'w')
            of.write(marked_up)
            of.close()
        except (TypeError, ValueError):
            print ('**ERROR**')
            print ('There seems to be some incorrectly-formatted data in file [' + input_file + '], in post [' + title + '].')
            print ('Please check the documentation for a template.')
            exit(1)

    print ('Processing Tags...')
    tag_dict = sorted(tag_dict.items(), key=lambda t: len(t[1]), reverse=True)

    print ('Generating index in ' + output_path + '...')
    index_markup += '<h2>Tags</h2>\n<div class="tag-list">\n<ul>\n'
    for tag, post_list in tag_dict:
        index_markup += '<li class="tag-name">'+ tag + ' <div class="tagged-posts">: '
        for title, link in post_list :
            index_markup += '<a href="' + link + '">' + title + '</a>, '
        index_markup = index_markup[:-2]
    index_markup += '\n</div>\n</ul>\n</div>\n'
    index_markup += index_footer
    index_file = file(output_path + 'index.html', 'w')
    index_file.write(index_markup)
    index_file.close()

    print ('Posts (unpublished):'), len(toc), ('('), unpublished, (')')
    print ('Tags:'),
    for tag in tag_dict:
        print tag[0] + (' '),
    print ('''

    ===============
    =Happy Trails!=
    ===============
    ''')

# I didn't really write this boilerplate:
def main():
    args = sys.argv[1:]


  
    input_file = 'blog.yaml'
    output_path = ''

    for idx in range(len(args)):
        if args[idx] == '--usage':
            print ('--------------------------------------------------------')
            print ('usage:  -in input_file.yaml  -out /path/to/document_root')
            print ('defaults are blog.yaml and the current working directory')
            print ('--------------------------------------------------------\n\n')
            sys.exit(0)
        if args[idx] == '--help' or args[idx] == '-?' or args[idx] == '/?' or args[idx] == '-help':
            print ('========================================================')
            print ('====== dev-blog - a lightweight web-log formatter ======')
            print ('========================================================')
            print ('Turn simple yaml-formatted journal entries into html.')
            print ('--------------------------------------------------------')            
            print ('usage:  -in input_file.yaml  -out /path/to/document_root')
            print ('defaults are blog.yaml and the current working directory')
            print ('see blog.yaml in this directory for an example blog file')
            print ('--------------------------------------------------------')
            print ('More? There should be a README.md file in this directory')            
            print ('--------------------------------------------------------\n\n')
            sys.exit(0)
        if args[idx] == '-in':
            input_file = args[idx + 1]
        elif args[idx] == '-out':
            output_path = args[idx + 1]
            # Check for trailing slash and add if needed
            if output_path[-1] != '/':
                output_path += '/'

    format_blog(input_file, output_path)

if __name__ == '__main__':
    main()