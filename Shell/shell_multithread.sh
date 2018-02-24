#!/bin/bash
#coding=utf-8
#shell的多线程操作方式

function test() {
    SEND_THREAD_NUM=3
    tmp_fifofile="/tmp/$$.fifo"
    mkfifo "$tmp_fifofile"
    exec 6<>"$tmp_fifofile"
    for ((i=0;i<$SEND_THREAD_NUM;i++))
    do
        echo
    done >&6

    # 下面的操作是多线程执行的；根据自己的需求修改即可
    for file in $(ls input/*); do
        read -u6
    {
        echo $file
        sleep 5
        echo >&6
    }&
    done
    wait
}

test
