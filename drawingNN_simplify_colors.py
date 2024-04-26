from matplotlib.patches import Circle
import matplotlib.pyplot as plt
import fastdataing as fd
import numpy as np

def position(start,stop,dist,center,num_points):
	arr = np.linspace(center - (num_points - 1) / 2 * dist, center + (num_points - 1) / 2 * dist, num_points)
	return arr

def plotNN(nlayers,nneurons,radius=0.2,width_dist=3,height_dist=1.5,xlen=16,ylen=10,ninputs=15,
	linewidth_circle=1,fill=False,color_circle="black",color_fill="lightblue",edgecolor="none",
	alpha=0.5,axis=False):
	"""
	Parameters:
	- nlayers: number of layers, int
	- nneurons: number of neurons, a list
	- radius: radius of neurons, float
	- width_dist: width distance between neurons, float
	- height_dist: height distance between neurons, float
	- xlen: Canvas x direction dimensions, float
	- ylen: Canvas y direction dimensions, float
	- ninputs: number of input paramenters, int
	- linewidth_circle: linewidth of neurons, float
	- fill: Fill circle or not, bool
	- color_circle: color of neurons circle, string
	- color_fill: color of neurons fill, string
	- alpha: Transparency of a circle, float
	- axis: Whether to draw coordinate axes, bool
	"""
	fig = fd.add_fig()
	ax = fd.add_ax(fig)
	xcenter = xlen*0.5
	ycenter = ylen*0.5
	max_value = max(nneurons)
	max_index = nneurons.index(max_value)
	layers = position(0+radius,xlen-radius,width_dist,xcenter,nlayers).tolist()
	circles_all = []
	labels_layers = ["Input layer","Hidden layer (s)","Output layer"]
	for n in layers:
		# print(n)
		ni = layers.index(n)
		if ni == max_index:
			coord_neurons = position(0+radius,ylen-radius,height_dist,ycenter,nneurons[ni])
			circles = [(n, i) for i in coord_neurons]
		else:
			circles = [(n, i) for i in position(0,ylen,height_dist,ycenter,nneurons[ni])]

		if ni in [i for i in range(nlayers-1)]:
			dotcenter = circles[2]
			del circles[2]
			x, y = dotcenter[0],dotcenter[1]
			for yi in [y-radius*1.6,y,y+radius*1.6]:
				dots = Circle((x,yi),radius*0.25,fill=True,alpha=0.7,
					color=color_fill
					)
				ax.add_artist(dots)
		circles_all.append(circles)
		# plot circles
		if ni in [i for i in range(1,nlayers-1)]:
			for (x, y) in circles:
				circle = Circle((x, y), radius, fill=True, 
					# edgecolor=edgecolor, 
					alpha=alpha,
					color=color_fill,linewidth=linewidth_circle)
				ax.add_artist(circle)
		else:
			for (x, y) in circles:
				circle = Circle((x, y), radius, fill=fill, 
					# edgecolor=edgecolor, 
					alpha=alpha,
					color=color_circle,linewidth=linewidth_circle)
				ax.add_artist(circle)
		# if ni == 0:
		# 	ty = circles[-1][1]
		# 	tx = circles[-1][0]-radius*3.5
		# 	ax.text(tx+radius*4.6,ty-radius*26,"Activation function",fontsize=15,color="gray")
		# 	ax.text(tx-radius*2.0,ty-radius*16,f"{ninputs} input parameters",fontsize=15,rotation=90)

		# elif ni == 1:
		# 	tx = circles[-1][0]-radius*4.8
		# 	ax.text(tx+radius*6.2,ty-radius*26,"Activation function",fontsize=15,color="gray")

		# elif ni == 2:
		# 	tx = circles[-1][0]-radius*4.6
		# 	ax.text(tx+radius*6,ty-radius*11.2,"1 output parameter",fontsize=15)

		# ax.text(tx,ty+radius*4,labels_layers[ni],fontsize=15)

	for i in range(1,nlayers):
		for circle0 in circles_all[i-1]:
			for circle1 in circles_all[i]:
				(x0,y0),(x1,y1) = circle0,circle1
				ax.arrow(x0+radius, y0, x1-x0-radius*2, y1-y0, head_width=0.05, 
					head_length=0.05, fc='gray', ec='gray', 
					length_includes_head=True)
	ax.set_xlim(0, xlen)
	ax.set_ylim(0, ylen)
	if axis == False:
		plt.axis('off')
	plt.savefig(f"./imgs/simplify_colors_{nlayers}.png",dpi=300,transparent=True)

	plt.show()


if "__main__" == __name__:
	color_fills = [
	"tan","coral","lightcoral","salmon",
	"sage","darkseagreen","cyan","deepskyblue",
	"steelblue","lightblue","pink"
	]
	color_fill = color_fills[2]
	plotNN(
		nlayers=4,#5,
		nneurons=[6,10,9,1],#[5,8,10,6,1],
		radius=0.35,
		width_dist=5,
		height_dist=1.5,
		xlen=20,ylen=16,ninputs=11,
		linewidth_circle=1,fill=False,
		color_circle=color_fill,
		color_fill=color_fill,
		alpha=1.0,axis=False
		)
