#!bin/bash/python
# ^ Not really, though.  This is just a place to store html.  
# As a python module.  For fun.
# Seriously, though - this is a part of ahmad@codemosey.net's super-minimalist
# yaml -> html parser, used to format his developer blog.  
# I can't imagine why you might be reading this.

header = """
<!doctype html>
<html>
  <head>
    <title>{% blog_name %}</title>
    <link href="https://fonts.googleapis.com/css?family=VT323|Fira+Mono:400,700" rel="stylesheet" type="text/css">
    <link href="css/style.css" rel="stylesheet" type="text/css">
  </head>
  <body>
    <h1>{% blog_name %}</h1>   
"""
footer = """
<hr><br>
<div class='attribution'>(c) <a href='{% org_link %}'>{% org_name %}</a></div>
  </body>
</html>
"""

post_header = header

post_footer = footer


index_header = header + """
    <h2>Posts</h2>
"""

index_footer = footer
