# -*- coding: utf-8 -*-
inrow = [3008, u'大立光',"3,805.00","3,810.00","3,780.00","3,795.00"]
outrow = []
for item in inrow:
    if type(item) is str and  "," in item:
        item = float(item.replace(",", ""))
    outrow.append(item)
print outrow