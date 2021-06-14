# https://blog.csdn.net/NNnora/article/details/84137036
import sys
import traceback

try:
    raise KeyboardInterrupt('fky')
except KeyboardInterrupt as e:
    # 异常类 实例 tracback对象
    t, v, tb = sys.exc_info()
    print(traceback.extract_tb(tb, ))
    print(traceback.extract_tb(tb, 2))
