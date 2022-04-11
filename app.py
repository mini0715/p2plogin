# 初始化日志配置
import logging

from utils import BASE_URL


def init_log_config():
    #创建日志器
    logger=logging.getLogger()
    #设置日志级别
    logger.setLevel(logging.INFO)
    #创建控制台处理器
    sh = logging.StreamHandler()
    #创建文件处理器
    log_path = BASE_URL + "/log/p2p.log"
    fh = logging.handlers.TimedRotatingFileHandler(log_path, when='M', interval=1, backupCount=7, encoding='utf-8')
    # 4.设置格式化器：打印日志时的格式内容（日志器名称、打印日志的函数名称、模块函数、代码行数、日志消息等）
    fmt = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)]-%(message)s"
    formatter = logging.Formatter(fmt)
    # 格式化日志添加到处理器
    sh.setFormatter(formatter)
    fh.setFormatter(formatter)
    # 添加日志
    logger.addHandler(sh)
    logger.addHandler(fh)
#TimedRotatingFileHandler