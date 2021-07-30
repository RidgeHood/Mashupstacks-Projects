from typing import List


color_dict = {'red':'#FF0000',
          'green':'#008000',
          'black':'#000000',
          'white':'#FFFFFF'}
keys=list(color_dict.keys())
values=color_dict.values()
keys.sort()

b={}
print(color_dict["red"])

for x in keys:
  b[f"{x}"] =color_dict[f"{x}"]
print('Sorted dictionary is:\n')
print(b)