## hash
1. hash仅能满足= in 和<=>查询，不能使用范围查询
2. 由于hash值不一定和hash运算前的值完全一样，所以mysql无法利用索引数据避免任务排序操作
3. 在hash冲突的情况下，性能不一定比b-tree好，因为要根据实际值进行表查询
4. 时间复杂度是o(1)

## b-tree
1. 时间复杂度是o(logn)
2. 只是范围查询

