#!/usr/bin/env python3
import sys
import os
import urllib.parse

print("Content-Type: text/html")
print()

method = os.environ.get('REQUEST_METHOD', 'GET')
content_type = os.environ.get('CONTENT_TYPE', '')

print(f"<h1>CGI Test Results</h1>")
print(f"<p><strong>Method:</strong> {method}</p>")
print(f"<p><strong>Content-Type:</strong> {content_type}</p>")

if method == 'POST':
    content_length = int(os.environ.get('CONTENT_LENGTH', 0))
    print(f"<p><strong>Content-Length:</strong> {content_length}</p>")
    
    if content_length > 0:
        post_data = sys.stdin.read(content_length)
        print(f"<p><strong>Raw POST Data:</strong></p>")
        print(f"<pre>{post_data}</pre>")
        
        # Try to parse form data
        if content_type == 'application/x-www-form-urlencoded':
            try:
                parsed_data = urllib.parse.parse_qs(post_data)
                print("<p><strong>Parsed Form Data:</strong></p>")
                print("<ul>")
                for key, values in parsed_data.items():
                    for value in values:
                        print(f"<li>{key}: {value}</li>")
                print("</ul>")
            except Exception as e:
                print(f"<p>Error parsing form data: {e}</p>")
    else:
        print("<p>No POST data received</p>")
else:
    print("<p>This is a GET request</p>")

# Print all environment variables
print("<h2>Environment Variables</h2>")
print("<ul>")
for key, value in sorted(os.environ.items()):
    if key.startswith('HTTP_') or key in ['REQUEST_METHOD', 'CONTENT_TYPE', 'CONTENT_LENGTH', 'QUERY_STRING']:
        print(f"<li><strong>{key}:</strong> {value}</li>")
print("</ul>")
