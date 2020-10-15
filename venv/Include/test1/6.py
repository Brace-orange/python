from matplotlib import pyplot as pt

x = range(2, 10, 1)
y = [1,2,3,4,5,6, 0, 0]
# pt.figure(figsize=(20,80), dpi=80)
pt.xticks(range(25, 50))
p1 = pt.plot(x,y)
pt.savefig('.././aaa.png')

pt.show()