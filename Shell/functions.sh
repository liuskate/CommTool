#!/bin/bash
#coding=utf-8
# 一些常见的公共函数库



# 日志打印
function INFO() {
    now=`date "+%Y-%m-%d %H:%M:%S"`
    message=$1
    echo "$now [INFO]: $message"
}

function ERROR() {
    now=`date "+%Y-%m-%d %H:%M:%S"`
    message=$1
    echo "$now [ERROR]: $message"
}

function TODAY() {
    today=$(date "+%Y%m%d")
    return $today
}


# 邮件告警
function mail() {
    echo "send mail to reporter"
}
