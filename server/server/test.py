import configparser
import os
import sys
if __name__ == '__main__':
    my_config = configparser.ConfigParser()
    my_config.read('./db.conf')
    print(my_config.get('DB','HOST'))
    print(sys.path)
    print(sys.executable)
    print(sys.prefix)