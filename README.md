# dev-blog: a minimalist YAML -> HTML formatter, via python script.

This script takes a simply-formatted YAML document, and inserts the posts contained therein in to a series of relatively read-able html documents, including an index of all posts, and a list of tags with links to the posts they contain.

A sample blog.yaml is included to demonstrate the format.  The first entry must contain the blog's name, as well as an attribution name and link:

-blog_name: my_blog_name
-org_name: super_cool_guy
-org_link: http://example.com

Each post entry must contain 5 fields:
- title: (no HTML)
- timestamp: (in [DD-MMM-YYYY] format)
- body: (HTML works, but you can break the pages if careless)
- tags: list in YAML or python format, i.e. ['cool stuff', 'rad times']
- publish: (posts will be skipped if set to False)

##Usage

./format_blog.py -in input_file.yaml  -out /path/to/document_root

defaults are blog.yaml and the current working directory

This script will only generate the html; if you want to use the included css and you are using a different output directory than the one you installed this package to, make sure to copy ./css/style.css to /your_directory/css/style.css
