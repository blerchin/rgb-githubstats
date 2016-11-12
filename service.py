#!/usr/bin/python

import draw
import time
from daemon import Daemon

class drawstats(Daemon):
    def run(self):
	time.sleep(30) #wait for net interface to load
        draw.loop()

proc = drawstats('/tmp/rgb-githubstats.pid')
proc.start()
