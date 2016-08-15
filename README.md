# python-hex-gradient-generator
*A simple hex color gradient generator with no dependencies.*

Takes lower and upper colors formated in hex with any number (N) of steps in between to generate a gradient.

`get_color` returns the color at fraction x/N between lower and upper colors of the gradient.

Example Usage
```python
N = 10
gradient = Gradient("#FF0000", 	"#808080", N)
gradient_colors = [ gradient.get_color(x) for x in range(N) ]

for color in gradient_colors:
  print(color)
```
Output
```
#FF0000
#F20C0C
#E51919
#D82626
#CC3333
#BF4040
#B24C4C
#A65959
#996666
#8C7373
```
