import logging

log_file_name = r'F:\Log\123.log'

logging.basicConfig(level=logging.DEBUG,
                    format='%(levelname)s\t%(asctime)s %(filename)s[line:%(lineno)d] %(funcName)s\t%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    # 配置日志文件路径
                    filename=log_file_name,
                    filemode='a')

