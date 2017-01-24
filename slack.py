#!/usr/bin/env python

import json
import requests
import sys, getopt

def main(argv):
   url = ''
   text = ''
   username = ''
   data = {}
   headers = {'Content-type': 'application/json'}
   try:
      opts, args = getopt.getopt(argv,"hu:t:n:c:i:",["url=","text=","name=","channel=","icon="])
   except getopt.GetoptError:
      print 'slack.py -u <slack webhook url> -t <text to send> -n <name of bot (optional)> -c <channel (optional)> -i <icon (optional)>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'slack.py -u <slack webhook url> -t <text to send> -n <name of bot (optional)> -c <channel (optional)> -i <icon (optional)>'
         sys.exit()
      elif opt in ("-u", "--url"):
         url = arg
      elif opt in ("-t", "--text"):
	 data['text'] = arg
      elif opt in ("-n", "--name"):
         data['username'] = arg
      elif opt in ("-c", "--channel"):
	 data['channel'] = "#" + arg
      elif opt in ("-i", "--icon"):
	 data['icon_emoji'] = ":" + arg + ":"
   jdata = json.dumps(data, ensure_ascii=False)
   r = requests.post(url, data=jdata, headers=headers)

if __name__ == "__main__":
   main(sys.argv[1:])

