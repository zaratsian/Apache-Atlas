<H3><a href="http://atlas.incubator.apache.org/">Apache Atlas</a></H3> 
Apache Atlas provides scalable governance for Enterprise Hadoop that is driven by metadata. Apache Atlas empowers enterprises to effectively and efficiently address their compliance requirements through a scalable set of core governance services. These services including <b>Data Lineage</b>, <b>REST APIs</b>, <b>Metadata Exchange</b>, <b>Business Taxonomies</b>.     
<br>
<br><b>To run within <a href="http://hortonworks.com/downloads/#sandbox">Hortonworks Sandbox</a>:</b>
<br>&ensp;&ensp;1.) Increase VM to 10.5 GB of RAM
<br>&ensp;&ensp;2.) Stop Flume, Oozie, Zeppelin
<br>&ensp;&ensp;3.) Within Hive, set ```atlas.hook.hive.synchronous = true```
<br>&ensp;&ensp;4.) Within Atlas, add ```atlas.feature.taxonomy.enable = true```  (Custom application-properties) 
<br>&ensp;&ensp;5.) Restart / Start - Ambari Infra, Ranger Tagsync, Hive, HBase, Atlas, Sqoop, Storm, Kafka
<br>&ensp;&ensp;6.) Turn on Maintenance Mode
<br>
<br><b>Quickstart:</b>
<br>```su atlas -c '/usr/hdp/current/atlas-server/bin/quick_start.py'```
<br>
<br><b>Kafka - Entities Topic</b>
<br>```/usr/hdp/current/kafka-broker/bin/kafka-console-consumer.sh --zookeeper localhost:2181 --topic ATLAS_ENTITIES --from-beginning```
<br>Other topic: ATLAS_HOOK
<br>user=atlas
<br>
<br>
<br><b>References:</b>
<br><a href="http://atlas.incubator.apache.org/">Apache Atlas</a>
<br><a href="http://hortonworks.com/apache/atlas/">Apache Atlas - Hortonworks Overview</a>
<br><a href="https://docs.hortonworks.com/HDPDocuments/HDP2/HDP-2.5.0/bk_data-governance/content/ch_hdp_data_governance_overview.html">Apache Atlas - Hortonworks Documentation</a>
<br><a href="https://docs.hortonworks.com/HDPDocuments/HDP2/HDP-2.5.0/bk_data-governance/content/ch_appendix_atlas_rest_api.html">Atlas REST APIs</a>
<br><a href="http://atlas.incubator.apache.org/AtlasTechnicalUserGuide.pdf">Atlas Technical User Guide</a>
<br><a href="https://community.hortonworks.com/articles/124/atlas-api-tips-create-trait-type-example.html">HCC - Create Trait Type API</a>
<br><a href="https://cwiki.apache.org/confluence/display/RANGER/Geo-location+based+policies">Ranger/Atlas Location Geo-based Policies</a>
