#!/usr/bin/python
import json
import os
#from screeninfo import get_monitors
import sys

script_dir = os.path.dirname(os.path.realpath(__file__))
json_file_path = os.path.join(script_dir, 'xulstore-example.json')
home_dir = os.path.expanduser("~")
firefox_profiles_dir = os.path.join(home_dir, '.mozilla', 'firefox')
xulstore_location = ''

if os.path.exists(firefox_profiles_dir) and os.path.isdir(firefox_profiles_dir):
	subdirectories = [subdir for subdir in os.listdir(firefox_profiles_dir) if os.path.isdir(os.path.join(firefox_profiles_dir, subdir))]
	
	for subdir in subdirectories:
		xulstore_path = os.path.join(firefox_profiles_dir, subdir, 'xulstore.json')
		if os.path.exists(xulstore_path) and os.path.isfile(xulstore_path):
			xulstore_location = xulstore_path
			break
			
	if xulstore_location == '':
		try:
			sys.exit(1)
		except SystemExit as e:
			print("could not find xulstore.json")

#monitors = get_monitors()

if os.path.exists(json_file_path):
	with open(json_file_path, 'r') as file:
		data = json.load(file)
	
	#primary_monitor = monitors[0]
	#screen_width = primary_monitor.width
	#screen_height = primary_monitor.height
	
	data['chrome://browser/content/browser.xhtml']['main-window']['screenX'] = 0
	data['chrome://browser/content/browser.xhtml']['main-window']['screenY'] = 0
	#data['chrome://browser/content/browser.xhtml']['main-window']['width'] = screen_width
	#data['chrome://browser/content/browser.xhtml']['main-window']['height'] = screen_height
	data['chrome://browser/content/browser.xhtml']['main-window']['width'] = 1920
	data['chrome://browser/content/browser.xhtml']['main-window']['height'] = 1080
	
	with open(xulstore_location, 'w') as file:
		json.dump(data, file)
	
else:
	print(f"The xulstore example file could not be found {json_file_path}")
