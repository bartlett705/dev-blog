# dev-blog: a minimalist YAML -> HTML formatter, via python script.

This script takes a simply-formatted YAML document, and inserts the posts contained therein in to a series of relatively read-able html documents, including an index of all posts, and a list of tags with links to the posts they contain.

A sample blog.yaml is included to demonstrate the format.  The first entry must contain the blog's name, as well as an attribution name and link.  Each post entry must contain a title, a timestamp in [DD-MMM-YYYY] format, a body, a list of tags in YAML or python format, and a 'Publish' field, which will only generate html for that post if it is not blank or set to False.

##Usage

./format_blog.py -in input_file.yaml  -out /path/to/document_root

defaults are blog.yaml and the current working directory

This script will only generate the html; if you want to use the included css and you are using a different output directory than the one you installed this package to, make sure to copy ./css/style.css to /your_directory/css/style.css
