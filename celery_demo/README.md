# celery
celery是一个分布式任务调度系统

https://github.com/SpiderClub/weibospider/wiki/%E5%A6%82%E4%BD%95%E6%9E%84%E5%BB%BA%E4%B8%80%E4%B8%AA%E5%88%86%E5%B8%83%E5%BC%8F%E7%88%AC%E8%99%AB%EF%BC%9A%E7%90%86%E8%AE%BA%E7%AF%87

1. broker：翻译过来叫做中间人。它是一个消息传输的中间件，可以理解为一个邮箱。每当应用程序调用celery的异步任务的时候，会向broker传递消息，而后celery的worker将会取到消息，执行相应程序。这其实就是消费者和生产者之间的桥梁。
2. backend: 通常程序发送的消息，发完就完了，可能都不知道对方时候接受了。为此，celery实现了一个backend，用于存储这些消息以及celery执行的一些消息和结果。
3. worker: Celery类的实例，作用就是执行各种任务。注意在celery3.1.25后windows是不支持celery worker的！
4. producer: 发送任务，将其传递给broker
5. beat: celery实现的定时任务。可以将其理解为一个producer，因为它也是通过网络调用定时将任务发送给worker执行。注意在windows上celery是不支持定时任务的！


1. celery如何解决worker丢失任务问题

