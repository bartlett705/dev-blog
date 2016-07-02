# dev-blog: a minimalist YAML -> HTML formatter, via python script.

This script takes a simply-formatted YAML document, and inserts the posts contained therein in to a series of relatively read-able html documents, an index of all posts, and a list of tags with links to the posts they contain.  [Markdown](https://gitbookio.gitbooks.io/markdown/content/) formatting and code syntax highlighting are supported via [Pygments](http://pygments.org) and Waylan's python [markdown library](https://github.com/waylan/Python-Markdown). YAML interpretation is handled by [pYAML](http://pyyaml.org/wiki/PyYAML).  

## Installation on Linux

1. Clone this git repository, or download the zip and extract it somewhere that you'd like to keep it.
2. `easy_install pip` if you don't have it already.
3. `sudo pip install Pygments markdown pyaml`
4. Profit!

> This script is written for python 2.7.6, and will attempt to run using /usr/bin/python by default - to point to another interpreter path, edit the first line of format_blog.py, leaving the #! before the path.  This should work just fine with python3, however; if you want to give that a try, skip step 1 below and use pip3 (available in Ubuntu 12.10+ in the package 'python3-pip') in step 2.

## Input Format

A sample blog.yaml is included to demonstrate the format.  The first entry must contain the blog's name, as well as an attribution name and link:

-blog_name: my_blog_name
-org_name: super_cool_guy
-org_link: http://example.com

Each post entry must contain 5 fields:
- title: (no HTML)
- timestamp: (in DD-MMM-YYYY format)
- body: (HTML works, but you can break the pages if careless)
- tags: list in YAML or python format, i.e. ['cool stuff', 'rad times']
- publish: (posts will be skipped if set to False)

### Code Syntax Highlighting

The most reliable way to do code syntax highlighting in CodeHiLite seems to be to use fenced code blocks specifying the name of the language, like so:

```
	```python
		def some_func():
			pass
	```
```
Which will render as:
```python
	def some_func():
		pass
```
If you would like to check out all the options, however, see the [CodeHiLite docs](https://pythonhosted.org/Markdown/extensions/code_hilite.html)

## Usage

`./format_blog.py -in input_file.yaml  -out /path/to/document_root`

defaults are `blog.yaml` and the current working directory

>This script will only generate the html; if you want to use the included css,
>and you are using a different output directory than the one you installed this 
>package to, make sure to copy `./css` to `/your_directory/css`