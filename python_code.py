# -*- coding: utf-8 -*-

# 读取多个json文件的内容
def read_json_file():
    filelist = ['title.json', 'body.json']
    for file in filelist:
        with open(file, 'r') as f:
            # 每次读取一行 避免占用过高内存
            for line in f.readlines():
                line = str(line).strip()
                if line.startswith('{') != True or line.endswith('}') != True:
                    print('is continue')
                    continue
                try:
                    linedata = json.loads(line)
                except Exception  as e:
                    print('except:', e)
                    print(len(line))
                    return
                finally:
                    pass

# 简单便利列表中的每一个值
all_file = list()
time_prefix = 'day_'
time_range = ['0.json', '1.json', '2.json']
[all_file.append(time_prefix + num) for num in time_range]
print(all_file)
# reesult ['day_0.json', 'day_1.json', 'day_2.json']