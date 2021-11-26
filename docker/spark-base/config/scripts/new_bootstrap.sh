#!/bin/bash

# Este trecho rodará independente de termos um container master ou
# worker. Necesário para funcionamento do HDFS e para comunicação
# dos containers/nodes.
/etc/init.d/ssh start

# Abaixo temos o trecho que rodará apenas no master.
if [[ $HOSTNAME = spark-master ]]; then

    # Formatamos o namenode caso ainda não exista um HDFS
    if [ "`ls -A $HADOOP_HOME/data`" == "" ]; then
      echo "Formatting namenode name directory: $HADOOP_HOME/data"
      hdfs namenode -format

    fi

    # Iniciamos os serviços
    $HADOOP_HOME/sbin/start-dfs.sh
    $HADOOP_HOME/sbin/start-yarn.sh

else
    # Configs de HDFS nos dataNodes (workers)
    $HADOOP_HOME/sbin/hadoop-daemon.sh start datanode &
    $HADOOP_HOME/bin/yarn nodemanager

fi

while :; do sleep 2073600; done
