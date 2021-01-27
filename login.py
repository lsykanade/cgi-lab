#!/usr/bin/env python3

import os 
import sys
import json
import secret
import templates

method = os.environ.get("REQUEST_METHOD", 0)
if method == "GET":
	print('Content-Type: text/html')
	print()
	print(templates.login_page())

else:
	posted_bytes = os.environ.get("CONTENT_LENGTH", 0)
	posted = sys.stdin.read(int(posted_bytes))
	data = posted.splitlines()[0].split("&")
	username = data[0].split("=")[1]
	password = data[1].split("=")[1]
	if username == secret.username and password == secret.password:
		print('Content-Type: text/html')

		# From https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie#examples 2021/1/27
		print('Set-Cookie: '+secret.username+"="+secret.password)
		print()
		print(templates.secret_page(secret.username, secret.password))
	else:
		print('Content-Type: text/html')
		print()
		print(templates.after_login_incorrect())