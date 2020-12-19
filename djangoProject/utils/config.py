import configparser
import os


class ReadConfig:
    def read_config(self,file_name,section,option):
        file = os.path.abspath(os.path.join(os.getcwd(),'..','confx',file_name))
        cf = configparser.ConfigParser()
        cf.read(file,encoding='utf-8')
        return cf.get(section,option)

if __name__ == '__main__':
    r = ReadConfig().read_config('confx.ini','add','version')
    print(r)
