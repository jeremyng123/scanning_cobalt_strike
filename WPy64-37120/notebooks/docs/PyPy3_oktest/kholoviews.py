import numpy as np
image = np.zeros((1024, 1536), dtype = np.uint8)

#from pylab import imshow, show
import matplotlib.pyplot as plt
from timeit import default_timer as timer

# with %%cython -a , full C-speed lines are shown in white, slowest python-speed lines are shown in dark yellow lines 
# ==> put your cython rewrite effort on dark yellow lines
def create_fractal_cython(min_x, max_x, min_y, max_y, image, iters , mandelx):
  height = image.shape[0]
  width = image.shape[1]
  pixel_size_x = (max_x - min_x) / width
  pixel_size_y = (max_y - min_y) / height
    
  for x in range(width):
    real = min_x + x * pixel_size_x
    for y in range(height):
      imag = min_y + y * pixel_size_y
      color = mandelx(real, imag, iters)
      image[y, x] = color

def mandel_cython(x, y, max_iters):
  #i = 0 
  #cdef double   cx, cy , zx, zy
  cx , cy = x, y 
  zx , zy =0 ,0 
  for i in range(max_iters):
    zx , zy = zx*zx - zy*zy + cx , zx*zy*2 + cy
    if (zx*zx + zy*zy) >= 4:
      return i
  return max_iters
#Cython speed
start = timer()
create_fractal_cython(-2.0, 1.0, -1.0, 1.0, image, 20 , mandel_cython) 
dt = timer() - start

fig = plt.figure()
print ("Mandelbrot created by cython in %f s" % dt)
plt.imshow(image)
plt.show()

# temporary warning removal
import warnings
import matplotlib as mpl
warnings.filterwarnings("ignore", category=mpl.cbook.MatplotlibDeprecationWarning)
# Holoviews
# for more example, see http://holoviews.org/Tutorials/index.html
import numpy as np
import holoviews as hv
hv.extension('matplotlib')
dots = np.linspace(-0.45, 0.45, 11)
fractal = hv.Image(image)

layouts = {y: (fractal * hv.Points(fractal.sample([(i,y) for i in dots])) +
               fractal.sample(y=y) )
            for y in np.linspace(0, 0.45,11)}

hv.HoloMap(layouts, kdims=['Y']).collate().cols(2)
