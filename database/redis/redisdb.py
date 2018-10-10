#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# redis的常见API封装类


import sys
import redis
import json
import traceback

class RedisDB():
    ''' 封装的访问redis的类
    '''

    def __init__(self, host='127.0.0.1', port=6379, passwd=''):
        try:
            pool = redis.ConnectionPool(host = host, port = port, password = passwd)
            self.conn = redis.StrictRedis(connection_pool=pool)
            #print("succ")
        except Exception:
            traceback.print_exc()
            sys.exit(-1)

    def delete(self, key):
        if self.conn is None:
            return False
        self.conn.delete(key)
        return True

    def set(self, key, value, timeout=-1):
        if not key or not value:
            return False
        if not isinstance(timeout, int):
            print('timeout parameter is not int type')
                        timeout = -1
        try:
            self.conn.set(key, value)
            if timeout != -1:
                self.conn.expire(key, timeout)
        except Exception as e:
            traceback.print_exc()
            return False
        return True

    def get(self, key=''):
        ret = None
        if not key or not self.conn.exists(key):
            return None
        try:
            ret = self.conn.get(key)
        except:
            return None
        finally:
            return ret

    def hmset(self, head, valdict):
        if self.conn is None:
            return False
        if not isinstance(valdict, dict):
            return False
        for key, val in valdict.iteritems():
            if not isinstance(val, str) and not isinstance(val, unicode):
                valdict[key] = json.dumps(val)
        self.conn.hmset(head, valdict)
        return True

    def hmget(self, head, key, format="json"):
        rstval = None
        if not self.conn.exists(head):
            return rstval
        value = self.conn.hmget(head, key)[0]
        if value is None:
            return rstval
        try:
            if format == "json":
                print(value)
                value = json.loads(value)
                print(value)
        except:
            pass
        finally:
            return value

    def hdel(self, head, key):
        if not self.conn.exists(head):
            return False
        try:
            return self.conn.hdel(head, key)
        except:
            return False
           
def test_hmset():
    host = "10.23.241.237"
    port = "4300"
    r = RedisDB(host=host, port=port)

    # set childstory alias
    key = "spil_database_35e81f22_childstory_alias"
    alias_map = {
        "album_大头儿子小头爸爸" : "大头儿子和小头爸爸",
        "test2" : "test2"
    }
    #r.hmset(key, alias_map)
    #print(r.hmget(key, "album_大头儿子小头爸爸"))

    # set user cloud_pan playlist
    key = "spil_database_35e81f22_cloud_playlist"
    user_cloud_playlist = {
        "3451825659": {
            "folder_name": [
                "小猪佩奇",
                "第1季",
                "第2季",
                "第3季",
                "第三季（上）",
                "第三季（下）"
            ],
            "file_name": [
                "恐龙丢了",
                "泥坑",
                "爸爸的眼镜不见了",
                "下雪了",
                "化装舞会",
                "猪妈妈在工作",
                "最好的朋友",
                "放风筝",
                "捉迷藏",
                "自行车",
                "小猪佩奇 - 片头曲",
                "小猪佩奇 - 片尾曲"
            ]
        }
    }
    #for key, val in user_cloud_playlist.items():
    #    user_cloud_playlist[key] = json.dumps(val, ensure_ascii = False)
    #print(r.hmget(key, "test_user"))
    #r.hmset(key, user_cloud_playlist)
    user_id = "1939456087"
    user_id = "1720079728"
    user_id = "test_id"
    user_id = "3451825659"
    print(r.hmget(key, user_id))


    # get
    #key = "spil_database_35e81f22_childstory_alias"
    #key = "spil_database_35e81f22_manual_edit"
    #value = r.hmget(key, "56830465667")
    #print "test1: ", value
    #print(value)

if __name__ == "__main__":
    test_hmset()
