import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(levelname)s\t%(asctime)s %(filename)s[line:%(lineno)d] %(funcName)s\t%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    # 配置日志文件路径
                    filename=r'F:\Log\123.log',
                    filemode='a')

logging.debug("this is debug message")
logging.info('This is info message')
logging.warning('This is warning message')