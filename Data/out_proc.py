import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

input_path = 'toy_output.asc'
output_path = 'out.png'

pic = np.loadtxt(input_path, skiprows=6)
pic[pic == 0] = -1
plt.imshow(pic)

yellow = mpatches.Patch(color='#ffff00', label='hot')
green = mpatches.Patch(color='#009999', label='cold')
plt.legend(handles=[yellow, green])

plt.savefig(output_path)
