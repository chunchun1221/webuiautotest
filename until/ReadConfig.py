#用来读取配置的一个类,先默认这个项目用的是json吧，
#先打开文件，然后再读取json
import json
import os.path

import yaml
from trio import open_file


class ReadConfig(object):
    """读取配置的一些操作"""
    def __init__(self,file_path:str=None,file_name: str=None):
        current_dir = os.path.abspath(os.path.dirname(__file__))
        base_path = os.path.join(current_dir, "..", "config")
        if file_path is None and file_name is None:
            self.file_path=os.path.join(base_path,"base_data.json")
        elif file_path is None and file_name is not None:
            self.file_path=os.path.join(base_path,file_name)
        else:
            self.file_path=os.path.join(file_path+file_name)

    def open_file(self,loader):
        """打开文件"""
        try:
            with open(self.file_path,"r",encoding="utf-8") as f:
                return loader(f)
        except  Exception as e:
            print(e)
        except FileNotFoundError:
            print(f"文件未找到：{self.file_path}")
            return None
        except IOError as e:
            print(f"读取文件时发生错误：{e}")
            return None

    def read_json(self):
        return self.open_file(json.load)


    def read_yaml(self):
        return self.open_file(yaml.safe_load)





if __name__=="__main__":
    f=ReadConfig(file_name="base_data.yaml").read_yaml()
    print(f)

