#!/usr/bin/env python3

import os 
import json
import templates


print('Content-Type: application/json')
print()
print(json.dumps(dict(os.environ), indent=2))

# print('Content-Type: text/html')
# print()
# print("""<!DOCTYPE html> 
# <html>
# <body>
# <h1>HELLO I AM HTML</h1>
# """)
# print("<ul>")
# print(f"<p> QUERY_STRING={os.environ['QUERY_STRING']} </p >")
# print(f"<p> HTTP_USER_AGENT={os.environ['HTTP_USER_AGENT']} </p>")
# print("""
# </ul>
# """)
# print("""
# </ul>
# </body>
# </html>
# """)

