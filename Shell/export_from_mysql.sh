#!/bin/bash
# 载入数据到数据库中

if [ -f ./bin/functions.sh ]; then
. ./bin/functions.sh
else
. ./functions.sh
fi


if [ $# -lt 2 ]; then
    ERROR "[Usage]: sh $0 sql output [database]"
    ERROR "    default database: data_center]" && exit -1
fi

MYSQL_HOST='10.102.1.1'
MYSQL_USER='user'
MYSQL_PASSED='password'
MYSQL_DB="database"

selectsql=$1
output=$2
if [ $# -gt 2 ]; then
    MYSQL_DB=$3
fi
sql="use ${MYSQL_DB}; ${selectsql}"
echo "$sql"

mysql -h${MYSQL_HOST} -u${MYSQL_USER} -p${MYSQL_PASSED} -e"${sql}" > ${output}
if [ $? -ne 0 ]; then
    ERROR "exec ${sql} error" && exit -1
fi
INFO "exec ${sql} done."
