from IPython.display import display
from bqplot import (Figure, Map, Mercator, Orthographic, ColorScale, ColorAxis,
                    AlbersUSA, topo_load, Tooltip)
def_tt = Tooltip(fields=['id', 'name'])
map_mark = Map(scales={'projection': Mercator()}, tooltip=def_tt)
map_mark.interactions = {'click': 'select', 'hover': 'tooltip'}
fig = Figure(marks=[map_mark], title='Interactions Example')
display(fig)
