import re
string = "ite/ms/campfire_deployed"
string = re.findall(r'[^/]+$', string)
string = re.sub('[\[\]_\']', '', str(string))
print string