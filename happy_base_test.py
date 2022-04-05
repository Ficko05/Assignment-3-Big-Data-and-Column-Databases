# import happybase as hp
import asyncio
import xml
from thrift.protocol import TCompactProtocol  # Notice the import: TCompactProtocol [!]
from thrift.transport.TTransport import TFramedTransport  # Notice the import: TFramedTransport [!]
from thrift.transport import TSocket
import hbase
#import aiohappybase as happybase

import happybase


def get_connected():

        connection = happybase.Connection("localhost", 9090)
        # connection = hp.Connection("localhost",49189)
        connection.open()

        print(connection.tables() )
        # print(hbase_cnxn.tables())
        # return connection
        connection.close()



def put_data_in():
    connection = get_connected()
    table = connection.table('foods')
    input_file = xml.read(open("./data/Food_Display_Table.xml"))


# for row in input_file:

def put_data_test_connection():
    connection = get_connected()
    table = connection.table('foods')
    table.put(b'row-key', {b'family:qual1': b'value1',
                           b'family:qual2': b'value2'})


    # put_data()

    # connection.create_table(
    #     'mytable',
    #     {'cf1': dict(max_versions=10),
    #      'cf2': dict(max_versions=1, block_cache_enabled=False),
    #      'cf3': dict(),  # use defaults
    #      }
    # )


if __name__ == '__main__':
    #tr()
    get_connected()
