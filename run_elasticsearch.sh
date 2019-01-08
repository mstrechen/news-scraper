#!/bin/bash
docker run --name elastic \
--mount source=elasticdata,target="/usr/share/elasticsearch/data" \
--rm -it -i -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:6.5.4