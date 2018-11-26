# -*- coding: utf-8 -*-

def read_json_file():
    """
    读取多个json文件的内容
    """
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

def __listdir(slef, path):
    """
    获取指定文件夹下的所有文件
    """
    list_name = list()
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isdir(file_path):
            pass
        else:
            list_name.append(file_path)
    return list_name

def get_time_stamp(days):
    """
    获取指定日期的时间戳:例如 获取7天前0的时间戳
    """
    day = datetime.datetime.today().date() - datetime.timedelta(days=7)
    ts = int(time.mktime(time.strptime(str(day), '%Y-%m-%d')))
    return ts