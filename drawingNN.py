from matplotlib.patches import Circle
import matplotlib.pyplot as plt
import fastdataing as fd
import numpy as np

def position(start,stop,dist,center,num_points):
	arr = np.linspace(center - (num_points - 1) / 2 * dist, center + (num_points - 1) / 2 * dist, num_points)
	return arr

def plotNN(nlayers,nneurons,radius=0.2,width_dist=3,height_dist=1.5,xlen=16,ylen=10,
	linewidth_circle=1,fill=False,color_circle="black",edgecolor="none",alpha=0.5,axis=False):
	"""
	Parameters:
	- nlayers: number of layers, int
	- nneurons: number of neurons, a list
	- radius: radius of neurons, float
	- width_dist: width distance between neurons, float
	- height_dist: height distance between neurons, float
	- xlen: Canvas x direction dimensions, float
	- ylen: Canvas y direction dimensions, float
	- linewidth_circle: linewidth of neurons, float
	- fill: Fill circle or not, bool
	- color_circle: color of neurons, string
	- alpha: Transparency of a circle, float
	- axis: Whether to draw coordinate axes, bool
	"""

	# 创建图和轴对象
	fig = fd.add_fig()
	ax = fd.add_ax(fig)
	xcenter = xlen*0.5
	ycenter = ylen*0.5
	max_value = max(nneurons)
	max_index = nneurons.index(max_value)
	layers = position(0+radius,xlen-radius,width_dist,xcenter,nlayers).tolist()
	circles_all = []
	for n in layers:
		ni = layers.index(n)
		if n == max_index:
			coord_neurons = position(0+radius,ylen-radius,height_dist,ycenter,nneurons[ni])
			circles = [(n, i) for i in coord_neurons]
		else:
			circles = [(n, i) for i in position(0,ylen,height_dist,ycenter,nneurons[ni])]
			circles_all.append(circles)
		for (x, y) in circles:
			circle = Circle((x, y), radius, fill=fill, 
				# edgecolor=edgecolor, 
				alpha=alpha,
				color=color_circle,linewidth=linewidth_circle)

			ax.add_artist(circle)
	for i in range(1,nlayers):
		for circle0 in circles_all[i-1]:
			for circle1 in circles_all[i]:
				(x0,y0),(x1,y1) = circle0,circle1
				ax.arrow(x0+radius, y0, x1-x0-radius*2, y1-y0, head_width=0.1, 
					head_length=0.1, fc='gray', ec='gray', 
					length_includes_head=True)

	# 设置坐标轴范围和显示效果
	ax.set_xlim(0, xlen)
	ax.set_ylim(0, ylen)
	if axis == False:
		plt.axis('off')
	plt.savefig("./3.png",dpi=300,transparent=False)

	# 显示图形
	plt.show()


if "__main__" == __name__:
	plotNN(
		nlayers=3,#5,
		nneurons=[5,10,1],#[5,8,10,6,1],
		radius=0.35,
		width_dist=3.5,
		height_dist=1.5,
		xlen=20,ylen=16,
		linewidth_circle=1,fill=False,
		color_circle="black",alpha=1.0,axis=False
		)
