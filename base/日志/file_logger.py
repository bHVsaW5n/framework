import logging
import logging.handlers


class Logger:
    def __init__(self, name=__name__):
        # 创建一个loggger
        self.__name = name
        self.logger = logging.getLogger(self.__name)
        self.logger.setLevel(logging.DEBUG)

        # 创建一个handler，用于写入日志文件
        logname = "/mnt/d/MyImgProject/framework/logs/前端参数记录.log"  # 指定输出的日志文件名, 路径自定义
        fh = logging.handlers.RotatingFileHandler(logname, mode='a', maxBytes=52428800, backupCount=2,
                                                  encoding='utf-8')  # 不拆分日志文件，a指追加模式,w为覆盖模式
        fh.setLevel(logging.DEBUG)

        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s-[line:%(lineno)d]-%(levelname)s-[日志信息]: %(message)s')
        fh.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(fh)

    @property
    def get_log(self):
        """定义一个函数，回调logger实例"""
        return self.logger


file_logger = Logger().get_log
