import logging
import os
import datetime

class Loging(object):
    def __init__(self):
        self.logger=logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        #文件名称和创建日志文件
        base_path=os.path.abspath(os.path.dirname(__file__))
        file_name=datetime.datetime.now().strftime("%y-%m-%d_%H_%M")+".log"
        log_name=os.path.join(base_path,"../log/",file_name)
        # print(f"Log file path: {log_name}")
        self.file_handle = logging.FileHandler(log_name, "w", "utf-8")
        # print("File handler created.")
        self.file_handle.setLevel(logging.DEBUG)
        file_formatter=logging.Formatter("%(asctime)s-%(filename)s-%(levelname)s-%(message)s")
        self.file_handle.setFormatter(file_formatter)
        self.logger.addHandler(self.file_handle)

        # 添加控制台输出
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)  # 设置控制台日志级别
        console_formatter = logging.Formatter("%(levelname)s: %(message)s")  # 简化的格式化器适用于控制台
        console_handler.setFormatter(console_formatter)
        self.logger.addHandler(console_handler)  # 将控制台处理器添加到logger



    def get_log(self):
        return self.logger

    def close_handle(self):
        self.logger.removeHandler(self.file_handle)
        self.file_handle.close()


if __name__ =="__main__":
    test=Loging()
    test.get_log()
    test.get_log().debug("这是一个很严重的东西啊")
    test.close_handle()
