#!/bin/bash
remote=/mnt/origin-story/var/www/portfolio/dev-blog
echo Copying to $remote...
cp *.html $remote
cp css/*.css $remote/css
echo All done!
