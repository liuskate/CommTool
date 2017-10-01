#!/bin/bash
# 从数据库中导出数据

if [ -f ./bin/functions.sh ]; then
. ./bin/functions.sh
else
. ./functions.sh
fi


echo $#
if [ $# -lt 3 ]; then
    ERROR "[Usage]: sh $0 sql output mysql_conf" && exit -1
fi


selectsql=$1
output=$2
mysql_conf=$3
source ${mysql_conf}

sql="use ${MYSQL_DB}; ${selectsql}"
echo "$sql"

if [ "${MYSQL_PASSED}" != "" ]; then
    mysql -h${MYSQL_HOST} -u${MYSQL_USER} -p"${MYSQL_PASSED}" -e"${sql}" > ${output}
else
    mysql -h${MYSQL_HOST} -u${MYSQL_USER} -e"${sql}" > ${output}
fi
if [ $? -ne 0 ]; then
    ERROR "exec ${sql} error" && exit -1
fi
INFO "exec ${sql} done."
