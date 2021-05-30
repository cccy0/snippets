pymysql,pymssql都不是线程安全的

https://stackoverflow.com/questions/47163438/is-pymysql-connection-thread-safe-is-pymysql-cursor-thread-safe


https://stackoverflow.com/questions/7182425/segfault-with-pymssql-when-cannot-connect-to-server-on-multiple-threads


所以一个解决办法就是一个线程一个connection就好啦

使用DBUtils也是一个解决办法

https://www.cnblogs.com/zhuminghui/p/10930846.html

安装DButils

https://blog.csdn.net/qq_14809913/article/details/113608341