import Gnuplot

# read arguments directly from command line. See:
# http://stackoverflow.com/questions/11604653/add-command-line-arguments-with-flags-in-python3

x = []
plot = []
origin = []

# insert supported file associations here:
file_associations = ['txt', 'csv']

file = input("Please insert file name: ")

try:
    if file.split(".")[-1] in file_associations:
        fhand = open(file)
    else:
        print("File type not supported")
        exit()
except:
    print("Please restart and insert a correct file with association")
    exit()

flag = True
for line in fhand:
    line = line.strip().split(',')
    for i in range(len(line)):
        if flag:
            x.append([])
        try:
            x[i].append(float(line[i]))
        except:
            name = line
    flag = False

gp = Gnuplot.Gnuplot()

gp.title('My graph')
gp.xlabel("X Coordinates")
gp.ylabel("Y Coordinates")

gp('set xrange [0:%s]' % max(x[0]))
gp('set size 1,1')
gp('set origin 0,0')
gp('set multiplot')

# think of a way to make dinamic origins for >4 or <4 plots on the same window
for i in [0, 0.5]:
    for j in [0, 0.5]:
        origin.append((i, j))

for i in range(1, len(x)):
    plot.append(Gnuplot.Data(x[0], x[i], with_="linespoint", title=name[i]))
    gp.xlabel("%s" % name[0])
    gp.ylabel("%s" % name[i])
    # gnuplot prints all plots on one window only if there are exactly 4 plots
    # ^ to be refactored at line 45
    if i == 5:
        continue
    gp('set size 0.5,0.5')
    gp('set origin %s, %s' % origin[i-1])
    gp.plot(plot[i-1])
    input('Press return to continue...')

gp('unset multiplot')
gp('reset')
gp.plot(*plot)

for i in range(0, len(plot)):
    gp('set term png')
    gp('set output "plot%s.png"' % (i+1))
    gp.plot(plot[i])

fhand.close()

input('Please press return to exit...')
