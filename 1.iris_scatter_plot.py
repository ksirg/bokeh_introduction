from bokeh.sampledata.iris import flowers
from bokeh.plotting import figure, show, output_file, output_notebook

colormap = {'setosa': 'red', 'versicolor': 'green', 'virginica': 'blue'}
flowers['color'] = flowers['species'].map(lambda x: colormap[x])

#output_file("iris.html", title="iris.py example")
output_notebook()

p = figure(title = "Iris Morphology")
p.xaxis.axis_label = 'Petal Length'
p.yaxis.axis_label = 'Petal Width'

p.circle(flowers["petal_length"], flowers["petal_width"],
        color=flowers["color"], fill_alpha=0.2, size=10, )

show(p)