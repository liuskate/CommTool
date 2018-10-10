#!/bin/bash

# 索引名称
ALBUM="child_album"
TRACK="child_track"
MANUAL_EDIT="manual_edit"

# 默认ES集群的信息
HOST="szwg-vs-audio09.szwg01.baidu.com"
PORT=8200

# 不同环境下的ES集群信息
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

# 获取某个索引的mapping
function get_mapping() {
    local index="cloud_playlist"
    curl -H "Content-Type: application/json" -XGET "http://${HOST}:${PORT}/${index}/_mapping"
}

function get_all_mapping() {
    curl -H "Content-Type: application/json" -XGET "http://${HOST}:${PORT}/_mapping"
}

# 为某个索引添加mapping
function add_mapping() {
     local index="cloud_playlist"
     local doc_type="playlist"
     curl -H "Content-Type: application/json" -XPUT "http://${HOST}:${PORT}/${index}/${doc_type}/_mapping" -d '{
        "properties": {
            "keywords": {
                "type": "text",
                "similarity": "BM25",
                "analyzer": "ik_smart"
            }
        }
    }'
}


# 获取/设置某个索引的setting
function get_setting() {
    local index="cloud_playlist"
    curl -H "Content-Type: application/json" -XGET "http://${HOST}:${PORT}/${index}/_settings"
}

function get_cluster_setting() {
    curl -H "Content-Type: application/json" -XGET "http://${HOST}:${PORT}/_cluster/settings"
}

function set_all_setting() {
    curl -H "Content-Type: application/json" -XPUT "http://${HOST}:${PORT}/_all/_settings" -d '{
        "index.blocks.read_only_allow_delete": false
    }'
}

function set_setting() {
    # 设置索引的相关配置时，需要先关闭索引
    curl -H "Content-Type: application/json" -XPOST "http://${HOST}:${PORT}/cloud_playlist/_close"
    curl -H "Content-Type: application/json" -XPUT "http://${HOST}:${PORT}/cloud_playlist/_settings" -d '{
        "index.blocks.read_only_allow_delete": false,
        "index.translog.durability": "async",
        "index.translog.sync_interval": "30s",
        "index.translog.flush_threshold_size": "5m"
    }'
    curl -H "Content-Type: application/json" -XPOST "http://${HOST}:${PORT}/cloud_playlist/_open"
}


