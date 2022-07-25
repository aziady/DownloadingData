import pygal

# import Style class from pygal.style
from pygal.style import Style

# create a Style object
custom_style = Style(colors=('#FF0000', '#0000FF',
                             '#00FF00', '#000000',
                             '#FFD700'))
wm = pygal.maps.world.World(style
                            =custom_style)
wm.title = 'North, Central, and South America'

wm.add('North America', ['ca', 'mx', 'us'])
wm.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
wm.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf', 'gy', 'pe', 'py', 'sr', 'uy', 've'])

wm.render_to_file('america.svg')
