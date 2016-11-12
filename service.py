#!/usr/bin/python

import draw
from daemon import Daemon

class drawstats(Daemon):
    def run(self):
        draw.loop()

proc = drawstats('/tmp/rgb-githubstats.pid')
proc.start()
