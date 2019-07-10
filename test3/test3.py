"""
Solmir741
"""
time_ = '10-00', '10-30', '11-00', '11-30', '12-00', '12-30', '13-00', '13-30', '14-00', '14-30', '15-00', '15-30', '16-00', '16-30', '17-00', '17-30', '18-00'
cs = []
for i in range(5):
    c = []
    with open("c%d.txt" % i, "r") as f:
        for l in f:
            l = l.strip()
            if len(l) == 0:
                break
            d = float(l)
            c.append(d)
    cs.append(c)
ni = []
mi = -1
mds = 0.0
for i, ds in enumerate(zip(*cs)): # ищем максимальное значение
    if sum(ds) >= mds:
        if sum(ds) > mds:
            mds = sum(ds)
            mi = i
            ni = []
        # если несколько значений максимальны
        else:
            if len(ni) > 0:
                ni.append(i)
            else:
                ni.append(mi)
                ni.append(i)
            
if len(ni) > 0:
    for e, t in enumerate(ni):
        print(time_[t] + ' ' + time_[t+1])
else:
    print(time_[mi] + ' ' + time_[mi+1])

