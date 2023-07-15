#!/usr/bin/python3

import sys
import os
import re

if len(sys.argv) < 3:
    print("Usage: ./markdown2html.py <input_file> <output_file>", file=sys.stderr)
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

if not os.path.isfile(input_file):
    print(f"Missing {input_file}", file=sys.stderr)
    sys.exit(1)

with open(input_file, 'r') as f:
    markdown_content = f.read()

# Heading parsing
markdown_content = re.sub(r'^(#{1,6}) (.*)$', r'<\1>\2</\1>', markdown_content, flags=re.MULTILINE)

# Unordered listing parsing
markdown_content = re.sub(r'^- (.*)$', r'<ul>\n<li>\1</li>\n</ul>', markdown_content, flags=re.MULTILINE)

# Ordered listing parsing
markdown_content = re.sub(r'^\* (.*)$', r'<ol>\n<li>\1</li>\n</ol>', markdown_content, flags=re.MULTILINE)

# Paragraph parsing
markdown_content = re.sub(r'^(?!\s*$)(.*)', r'<p>\n\1\n</p>', markdown_content, flags=re.MULTILINE)

# Bold parsing
markdown_content = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', markdown_content)
markdown_content = re.sub(r'__(.*?)__', r'<em>\1</em>', markdown_content)

with open(output_file, 'w') as f:
    f.write(markdown_content)

sys.exit(0)
