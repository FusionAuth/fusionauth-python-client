imgid=`docker container ls|grep fusiona|awk '{print $1}'`

cnt=`docker logs $imgid 2>&1|grep 'Server startup' |wc -l`

while [ $cnt != "1" ]; do
  echo "waiting $cnt $imgid";
  sleep 2;
  cnt=`docker logs $imgid 2>&1|grep 'Server startup' |wc -l`;
done

