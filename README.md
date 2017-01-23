<H3><a href="http://atlas.incubator.apache.org/">Apache Atlas</a></H3>

<br><b>To run within <a href="http://hortonworks.com/downloads/#sandbox">Hortonworks Sandbox</a>:</b>
<br>&ensp;&ensp;1.) Increase VM to 10.5 GB of RAM
<br>&ensp;&ensp;2.) Stop Flume, Oozie, Zeppelin
<br>&ensp;&ensp;3.) Within Hive, set ```atlas.hook.hive.synchronous = true```
<br>&ensp;&ensp;4.) Within Atlas, add ```atlas.feature.taxonomy.enable = true```  (Custom application-properties) 
<br>&ensp;&ensp;5.) Restart / Start - Ambari Infra, Ranger Tagsync, Hive, HBase, Atlas, Sqoop, Storm, Kafka
<br>&ensp;&ensp;6.) Turn on Maintenance Mode
<br>
<br><b>Kafka - Entities Topic</b>
<br>```/usr/hdp/current/kafka-broker/bin/kafka-console-consumer.sh --zookeeper localhost:2181 --topic ATLAS_ENTITIES --from-beginning```
<br>Other topic: ATLAS_HOOK
<br>user=atlas
<br>
<br><b>Quickstart:</b>
<br>```su atlas -c '/usr/hdp/current/atlas-server/bin/quick_start.py'```
<br>
<br><b>References:</b>
<br><a href="http://atlas.incubator.apache.org/">Apache Atlas</a>
<br><a href="http://hortonworks.com/apache/atlas/">Apache Atlas - Hortonworks Overview</a>
<br><a href="https://docs.hortonworks.com/HDPDocuments/HDP2/HDP-2.5.0/bk_data-governance/content/ch_hdp_data_governance_overview.html">Apache Atlas - Hortonworks Documentation</a>
<br><a href="https://docs.hortonworks.com/HDPDocuments/HDP2/HDP-2.5.0/bk_data-governance/content/ch_appendix_atlas_rest_api.html">Atlas REST APIs</a>
