insert into test_table (name)
values ('xiaoming'),
       ('xiaoming'),
       ('xiaoming'),
       ('xiaoming'),
       ('xiaohong'),
       (null)

# https://blog.csdn.net/n950814abc/article/details/82284838
# https://blog.csdn.net/u013967628/article/details/88076520
# 重复数据
select name, count(1)
from test_table
group by name
having count(1) > 1
# 查询所有重复数据
select *
from test_table
where name in (select name from test_table group by name having count(name) > 1)
# 删除表中多余重复试题并且只留id最大的一条：

# 删除全部重复试题
delete
from test_table
where name in (select t.name from (select name from test_table group by name having count(name) > 1) as t)

# 删除重复数据，保留rowid最大的一行

delete
from test_table
where id not in (select t.id from (select max(id) as id from test_table group by name having count(name) > 1) as t)
  and name in (select t2.name from (select name from test_table group by name having count(name) > 1) as t2)

# 查询表中除了最小rowid的以外的重复数据
select *
from test_table
where name in (select name from test_table group by name having count(name) > 1)
  and id not in (select min(id) as id from test_table group by name having count(name) > 1)
