# https://www.cnblogs.com/fnlingnzb-learner/p/8136187.html
insert into test_table1 (name)
values ('xiaoming'),
       ('fky')
select * from test_table t1 inner join test_table1 t2 on t1.name=t2.name
select * from test_table t1 left join test_table1 t2 on t1.name=t2.name
select * from test_table t1 right join test_table1 t2 on t1.name=t2.name
