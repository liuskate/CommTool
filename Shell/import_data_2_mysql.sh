#!/bin/bash
# 载入数据到数据库中

if [ -f ./bin/functions.sh ]; then
. ./bin/functions.sh
else
. /functions.sh
fi


if [ $# -lt 2 ]; then
    ERROR "[Usage]: sh $0 music_data_file  music_table" && exit -1
fi

input=$1
table=$2

MYSQL_HOST='10.100.1.1'
MYSQL_USER='user'
MYSQL_PASSED='password'
MYSQL_DB="database"

sql="use ${MYSQL_DB}; LOAD DATA LOCAL INFILE \"${input}\" REPLACE INTO TABLE ${table} FIELDS TERMINATED BY \"\t\""

mysql -h${MYSQL_HOST} -u${MYSQL_USER} -p${MYSQL_PASSED} -e"${sql}"
if [ $? -ne 0 ]; then
    ERROR "load $input to ${MYSQL_DB}.${table} error" && exit -1
fi
INFO "load $input to ${MYSQL_DB}.${table} done."
