1.进程拥有独立的内存空间 线程共享内存空间

2. 一个进程可以有多个内存

3. 进程是资源分配的i基本单位，通俗地说就是运行中的程序，线程是CPU调度的基本单元，

相较于线程，协程的调度则是由开发者控制的，协程可以不加锁

地访问全局变量

4.相比较于进程线程的上下文切换很快，资源开销更小


# 进程间通信IPC

https://mp.weixin.qq.com/s/mblyh6XrLj1bCwL0Evs-Vg

每个进程的用户地址空间都是独立的，一般而言是不能互相访问的，但内核空间是每个进程都共享，
所以进程之间要通信必须通过内核。
1.管道
就是shell命令中的竖线 |

先进先出的

linux中管道也是以文件的形式存在

优点是简单 缺点是通信方式效率低，不适合进程频繁交换资源

管道实际上是内核空间的一串缓存，一端读取一端写入，无格式且大小受限

2.消息队列

A进程把消息放消息队列就可以返回了 解决了管道通信效率低下的问题

本质上是内核中的消息链表

缺点是不及时，且消息大小受限，不适合传输大数据

3.共享内存

共享内存就是两个进程把各自的一部分虚拟内存 映射到相同的物理内存中

这样一个进程写入虚拟内存，另一个进程马上就能看到

4.信号量

信号量其实是一个整型计数器，为了同步和互斥多个进程对共享资源的访问，

5.信号

比如ctrl+c表示sigint 终止进程的意思

主要是异常情况用来通知工作进程

6.socket

用于跨网络不同主机间进程通信了