#!/usr/bin/python
import math
import json
import subprocess
import time
config_data = open('config.json').read()
config = json.loads(config_data)
REFRESH_INTERVAL = config['refresh_interval']
MATRIX_SIZE = 32

def run(matrix):
	data = json.loads(subprocess.check_output("./get_stats.rb", shell=True))

	ROW_SIZE = len(data)
	PIXEL_SIZE = MATRIX_SIZE / ROW_SIZE
	PADDING = (MATRIX_SIZE % ROW_SIZE) / 2

	colors = [0x9999999, 0xD6E685, 0x8CC665, 0x44A340, 0x1e6823] 
	def drawbox(row, col, color):
	    for x in range(PIXEL_SIZE):
		for y in range(PIXEL_SIZE):
		    matrix.SetPixel(
			row * PIXEL_SIZE + x + PADDING, 
			col * PIXEL_SIZE + y + PADDING,
			(color >> 16) 	& 0xFF ,
			(color >> 8) 	& 0xFF,
			color 		& 0xFF
			)

	for row in range(7):
	    for col in range(7):
		point = data[row][col]
		if point['score'] == -1:
		    color = 0x000000 
		else:
		    color = colors[point['quartile']]
		drawbox(row, col, color)
def loop():
	from rgbmatrix import Adafruit_RGBmatrix
	matrix = Adafruit_RGBmatrix(MATRIX_SIZE,1) 
	while(True):
	    run(matrix)
	    time.sleep(REFRESH_INTERVAL)
	    matrix.Clear()


if __name__ == '__main__':
    loop()
