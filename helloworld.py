import os
import math
import cairo

def draw_border(context, w, h, border, dotted = False):
	context.rectangle(border, border, w-2*border, h-2*border)
	if dotted:
		context.set_dash([30, 20],1)
	context.stroke ()
	context.set_dash([1,0],0)
	return context

def draw_rectangle(context, x, y, w, h, dotted = False):
	context.rectangle(x, y, w, h)
	if dotted:
		context.set_dash([30, 20],1)
	context.stroke ()
	context.set_dash([1,0],0)
	return context

def draw_circle(context, x, y, r, dotted = False):
	context.arc(x, y, r, 0, 2*math.pi)
	context.fill()
	return context

def draw_LED(context, x, y, dotted = False):
	draw_circle(context, x * LEDINCREMENT, y * LEDINCREMENT, LEDRADIUS)
	return context

WIDTH, HEIGHT = 2400, 800
BORDER1, BORDER2, = 10, 30
BWIDTH = WIDTH-2*BORDER2
BHEIGHT= HEIGHT-2*BORDER2
SCROLLHEIGHT = 100
LEDHEIGHT = int((BHEIGHT-2*SCROLLHEIGHT)/2)
TOPLEDX= BORDER2
TOPLEDY= BORDER2
TOPSCROLLX= BORDER2
TOPSCROLLY= LEDHEIGHT+BORDER2
BOTLEDX= BORDER2
BOTLEDY= LEDHEIGHT+BORDER2+SCROLLHEIGHT
BOTSCROLLX= BORDER2
BOTSCROLLY= BORDER2+BHEIGHT-SCROLLHEIGHT
NUMLEDSHIGH = 12
LEDBORDER = 40
LEDRADIUS = int((LEDHEIGHT-2*LEDBORDER)/NUMLEDSHIGH)
LEDINCREMENT = LEDRADIUS*2

surface = cairo.ImageSurface (cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
ctx = cairo.Context (surface)
ctx.set_source_rgb (0, 0, 0) # Solid color
ctx.set_line_width (5)

draw_border(ctx, WIDTH, HEIGHT, BORDER1, True)
draw_border(ctx, WIDTH, HEIGHT, BORDER2)

draw_rectangle(ctx, TOPSCROLLX, TOPSCROLLY, BWIDTH, SCROLLHEIGHT)
draw_rectangle(ctx, BOTSCROLLX, BOTSCROLLY, BWIDTH, SCROLLHEIGHT)

draw_LED(ctx,5,5)
draw_LED(ctx,5,6)

surface.write_to_png ("example.png") # Output to PNG
os.system("start chrome example.png")


