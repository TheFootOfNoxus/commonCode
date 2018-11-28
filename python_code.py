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

def print_memory_info():
    """
    打印已占用内存数
    :return:
    """
    import psutil

    info = psutil.virtual_memory()
    print u'内存使用：', psutil.Process(os.getpid()).memory_info().rss // 1024 #单位为Kb
    print u'总内存：', info.total // 1048576 #单位为Mb
    print u'内存占比：', info.percent
    print u'cpu个数：', psutil.cpu_count()

def today_timestamp():
    """
    当日0点时间戳
    :return:
    """
    now = datetime.datetime.utcfromtimestamp(now_timestamp - now_timestamp % 86400)
    return now

def last_week_timestamp():
    """
    获取上周时间戳
    :return:
    """
    last_week_start = int(time.mktime((now - datetime.timedelta(days=now.weekday() + 7)).timetuple()))
    last_week_end = int(time.mktime((now - datetime.timedelta(days=now.weekday() + 1)).timetuple()))

    return {'last_week_start': last_week_start, 'last_week_end': last_week_end}

def json_encode_cn():
    """
    json格式化中文
    :return:
    """
    f = open('../data/click/data.json', 'w')
    json_list = list()
    for item in items:
        word_list = utils.analyze(item['content'])
        if word_list:
            json_list += word_list
    f.write(json.dumps(json_list, ensure_ascii=False))
    f.close()

def check_contain_chinese(check_str):
    """
    检查字符串中是否包含中文
    :return:
    """
    for ch in check_str.decode('utf-8'):
        if u'\u4e00' <= ch <= u'\u9fff':
            return True
    return False