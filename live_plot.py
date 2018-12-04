from bokeh.io import curdoc
from bokeh.models import ColumnDataSource, Legend
from bokeh.plotting import Figure

POINTS_TO_KEEP = 50

doc = curdoc()
source = ColumnDataSource(dict(x=[], avg_fitness=[], min_fitness=[]))

fig = Figure(tools="", title="Mean and minimum fitness value of each generation", plot_width=800)
fig.title.text_font_size = "12pt"
fig.title.align = "center"
fig.background_fill_color = "beige"
fig.background_fill_alpha = 0.5

l1 = fig.line(source=source, x="x", y="avg_fitness", line_width=2, alpha=0.85, color="red")
l2 = fig.line(source=source, x="x", y="min_fitness", line_width=2, alpha=0.85, color="blue",)
fig.xaxis.axis_label = "Generation"
fig.yaxis.axis_label = "Fitness Value"

legend = Legend(items=[
    ("Mean fitness value"   , [l1]),
    ("Minimum fitness value" , [l2]),
], location=(0, 0))

fig.add_layout(legend, 'right')

# Create or overwrite existing tmp file
f = open("tmp_data.txt", "w")
f.close()

# Open tmp file for reading
f = open("tmp_data.txt", "r")

def update_data():
    global f, source
    line = f.readline().strip().split(",")

    if line[0] != "" and line[0] != "clear":
        new_data = dict(x = [int(line[0])], avg_fitness = [float(line[1])], min_fitness = [float(line[2])])
        source.stream(new_data, POINTS_TO_KEEP)

doc.add_root(fig)
doc.add_periodic_callback(update_data, 50)