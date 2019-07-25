# DevOps
## batch_execution.py
### 用途 
批量通过ssh连接linux主机并执行命令，同时打印结果
### 依赖
sudo pip install paramiko
### 使用示例见注释

---
## log_search.sh
### 用途 
k8s集群上，过滤多个pod上的日志。适合还没有做统一日志管理，但pod副本数较多，日志难找（不知道日志在哪个pod上）的场景
### 依赖
k8s
### 使用示例
1. 将namespace、pod_name、以及log_path改为实际的
2. sh log_search.sh 需要搜索的关键字,比如sh log_serch.sh ERROR
