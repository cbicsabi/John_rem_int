# All info was taken from
# http://www.mactech.com/articles/mactech/Vol.26/26.02/IntroductiontoGnuplot/index.html


import Gnuplot

gp = Gnuplot.Gnuplot()

# drawing the sin(x)*cos(x) function
gp.plot('sin(x)*cos(x)')
gp('set xrange [-2*pi:2*pi]')
gp('replot')

#  using -2*pi and +2*pi as our x-axis boundaries
gp("set title 'An example for MacTech'")
gp("set xlabel 'x-axis: from -2*pi to +2*pi'")
gp("set ylabel 'Setting the y-axis label'")
gp('replot')

# adding some text to the output
gp("set xtics ('0' 0, '-180' -pi, '-90' -pi/2, '90' pi/2, '180' pi)")
gp("set ytics ('0' 0, '0.5' 0.5, '-0.5' -0.5)")
gp("set grid")
gp('replot')

# MORE ADVANCED EXAMPLES
# adding gridlines to the gnuplot output
gp('plot x*x, 1/(x*x)')

# plotting many functions in multiplot mode
gp('set xrange [-1:1]')
gp('set size 1,1')
gp('set origin 0,0')
gp('set multiplot')

gp('set size 0.5,0.5')
gp('set origin 0,0.5')
gp('plot (x*x)')

gp('set size 0.5,0.5')
gp('set origin 0.5,0.5')
gp('plot sin(x)')

gp('set size 0.5,0.5')
gp('set origin 0,0')
gp('plot (1/x)')

gp('set size 0.5,0.5')
gp('set origin 0.5,0')
gp('plot (x*x*x)')

gp('unset multiplot')
# the reset command causes all graph-related options that can
# be set with the set command to take on their default values
gp('reset')

# ~~~Gnuplot and Python~~~
# import Gnuplot
# gp = Gnuplot.Gnuplot()

gp('set term png')
gp('set output "mactech.png"')
g5 = Gnuplot.Func('sin(x)')
gp.plot(g5)

input('Please press return to exit...')
