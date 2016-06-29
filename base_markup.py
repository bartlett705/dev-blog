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
    <title>[codemosey.net developer blog]</title>
    <link href="https://fonts.googleapis.com/css?family=VT323|Fira+Mono:400,700" rel="stylesheet" type="text/css">
    <link href="css/style.css" rel="stylesheet" type="text/css">
  </head>
  <body>
    <h1>[codemosey.net developer blog]</h1>
    <h2>Posts</h2>
    
"""
footer = """
<div class='attribution'>(c) <a href="http://codemosey.net">codemosey.net</a> aka Ahmad</div>
"""

post_footer = """
    <a href="index.html">Back</a>
  </body>
</html>
""" + footer

index_header = header
index_footer = footer
