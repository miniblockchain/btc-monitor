# coding= utf-8
import json
import sys
import os
from datetime import datetime,timedelta
import json
import os.path
import time
#import MySQLdb
import Cookie
import random
import sqlite3
import base64

if __name__ == '__main__':

    jsondata = file("./b.out");
    s = json.load(jsondata)
    print s['result']

    command = '''curl --user dylan:123456 --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getblock", "params": ["%s", 2] }' -H 'content-type: application/json;' 1.119.143.222:18332 > c.out'''%(s['result'])    
    print command
    os.system(command)
