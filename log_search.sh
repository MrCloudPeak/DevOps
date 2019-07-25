to_find=$1
pods=`kubectl -n namespace get po |grep pod_name|awk '{print $1}'|`
for pod in $pods
do
  echo $pod
  kubectl -n namespace exec $pod grep "$to_find" /home/server/logs/*
done
