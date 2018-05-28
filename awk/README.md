# 如何写一些awk的公共处理函数，通过include的方式导入使用
参考： https://stackoverflow.com/questions/28462821/include-library-of-functions-in-awk

举例说明：
$ ls lib
prims.awk

$ cat lib/prims.awk
function abs(num) { return (num > 0 ? num : -num) }
function max(a,b) { return (a > b ? a : b) }
function min(a,b) { return (a < b ? a : b) }

$ export AWKPATH="$PWD/lib"

$ awk -f prims.awk --source 'BEGIN{print min(4,7), abs(-3)}'
4 3
