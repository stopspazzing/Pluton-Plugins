import socket
import sys
import random
import re
import urllib2
import json
import time
import platform
import os
import string
import HTMLParser
import ssl
url = 'https://api.github.com/repos/Notulp/Pluton/git/refs/heads/master'
plutongit = json.load(urllib2.urlopen(url))
commits = plutongit['object']['url']
commit = json.load(urllib2.urlopen(commits))
date = commit['committer']['date']
author = commit['committer']['name']
message = commit['message']
print "Pluton was last updated " +date+ " by " +author+ " with comment : " +message