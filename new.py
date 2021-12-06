from datetime import datetime, timedelta
import re
import os
import sys
import subprocess

date = datetime.now() - timedelta(hours = 1)

name = input('What\'s the title of your blog post?')
# categories = input(
#     'What categories is this post in (separated by a comma)?')
# series = input(
#     'What series is this post in (separated by a comma)?')
# tags = input(
#     'What tags does this post have (separated by a comma)?')

title_name = re.sub('[^a-zA-Z\s\d]', '', name)
title_name = re.sub('\s', '-', title_name).lower()

title = date.strftime('%Y-%m-%d') + '-' + title_name + '.md'

# check year dir exists

yearPath = os.getcwd() + '/content/posts/' + str(date.year) + '/'

if not os.path.exists(yearPath):
    os.mkdir(yearPath)

# check month dir exists

if date.month < 10:
    monthPath = yearPath + '0' + str(date.month) + '/'
else:
    monthPath = yearPath + str(date.month) + '/'

if not os.path.exists(monthPath):
    os.mkdir(monthPath)

path = monthPath + title
if not os.path.exists(path):
    open(path, 'w')

if os.path.exists(path):
    f = open(path, 'a')
    f.write('---\n')
    f.write('date: \"' + date.strftime('%Y-%m-%d') +
            'T' + date.strftime('%H:%M:%S') + 'Z\"\n')
    # TODO: make this take an env variable
    f.write('author: Ted Slocum\n')
    f.write('title: \"' + name + '\"\n')
#     if len(categories) > 0:
#         f.write('categories:\n')
#         for cat in categories.split(", "):
#             f.write('- ' + cat + '\n')
#     if len(series) > 0:
#         f.write('series: [\"' + series + '\"]\n')
#     if len(tags) > 0:
#         f.write('tags:\n')
#         for cat in tags.split(", "):
#             f.write('- ' + cat + '\n')
    f.write('---\n')
