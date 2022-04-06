# Assignment-3-Big-Data-and-Column-Databases

## How to run 

run this in th DB folder :

```
docker-compose -f docker-compose-distributed-local.yml up -d 
```

(to get it down)

```
docker-compose -f docker-compose-distributed-local.yml down
```

then docker is up and running enter the CLI of hbase-master and type this 

```
hbase thrift start
```

this will run the thrift server.



