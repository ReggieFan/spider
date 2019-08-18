import json
import jsonlines
tom='\ntonm\n'
tom=tom.replace('\n','')
print(tom)

with open("d:\wlw360.jl", "r+", encoding="utf8") as f:
    for item in jsonlines.Reader(f):
        print(item)