#!/bin/bash
#coding=utf-8
# 构建索引，并且设置mapping

INDEX="cloud_playlist"
HOST="szwg-vs-audio09.szwg01.baidu.com"
PORT=8200

if [ "$1" = "yq" ]; then
    HOST="yq01-vs-audio562.yq01.baidu.com"
    PORT=8200
fi

if [ "$1" = "hn" ]; then
    HOST="gzns-audio-spil-server05.gzns.baidu.com"
    PORT=8200
fi

# 沙盒机器
if [ "$1" = "sandbox" ]; then
    HOST="yq01-audio-spil-server12.yq01.baidu.com"
    POST=8200
fi

function mapping() {
      curl -H "Content-Type: application/json" -XPUT "http://${HOST}:${PORT}/${INDEX}" -d '{
          "settings" : {
              "number_of_shards" : 1,
              "number_of_replicas" : 3
          },
          "mappings" : {
              "playlist" : {
                  "properties": {
                      "path": {
                          "type": "text",
                          "similarity": "BM25",
                          "analyzer": "ik_smart"
                      },
                      "keywords": {
                          "type": "text",
                          "similarity": "BM25",
                          "analyzer": "ik_smart"
                      },
                      "server_filename": {
                          "type": "text",
                          "similarity": "BM25",
                          "analyzer": "ik_smart"
                      },
                      "norm_filename": {
                          "type": "keyword"
                      },
                      "fs_id": {
                          "type": "keyword"
                      },
                      "parent_dirid": {
                          "type": "keyword"
                      },
                      "index": {
                          "type": "long"
                      },
                      "server_mtime" : {
                          "type" : "long"
                      },
                      "server_ctime" : {
                          "type" : "long"
                      },
                      "episode": {
                          "type": "keyword"
                      },
                      "user_id": {
                          "type": "keyword"
                      },
                      "id": {
                          "type": "keyword"
                      },
                      "upload_time": {
                          "type": "long"
                      },
                      "ancestors": {
                          "type": "keyword"
                      },
                      "ancestor_ids": {
                          "type": "keyword"
                      }
                  },
                  "_source": {
                      "enabled": true
                  },
                  "_all": {
                      "enabled": false
                  }
              }
          }
      }'
}
