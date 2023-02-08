import os
import json
import codecs

def get_path_to_dict():
    return json.dumps(path_to_dict('app\\main\\')['children'], ensure_ascii=False)

def path_to_dict(path):
    d = {'name': os.path.basename(path)}
    if os.path.isdir(path):
        d['type'] = "directory"
        d['path'] = path
        d['children'] = [path_to_dict(os.path.join(path,x)) for x in os.listdir(path)]
    else:
        d['type'] = "file"
        d['data'] = codecs.open(path , "r", "utf-8").read()
        #d['data']  = codecs.open(os.path.basename(path), "r", "utf-8").read()
    return d


"""

js = json.loads( get_path_to_dict() )
#js = json.loads( get_path_to_dict() )['children']
print(js)
path = 'main4\Новая папка\Новая папка\Новая папка'
pathlist = path.split('\\')
print(pathlist)

chl = None
temp = js
for pth in pathlist:
    for tmp in temp:
        if tmp['name'] == pth:
            chl = tmp['children']
    temp = chl
    pass
print(temp)


"""