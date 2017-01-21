<H3><a href="http://atlas.incubator.apache.org/">Apache Atlas</a></H3>

<br><b>To run within <a href="http://hortonworks.com/downloads/#sandbox">Hortonworks Sandbox</a></b>
<br>&ensp;&ensp;1.) Increase VM to 10.5 GB of RAM
<br>&ensp;&ensp;2.) Stop Flume, Oozie, Zeppelin
<br>&ensp;&ensp;3.) Within Hive, set ```atlas.hook.hive.synchronous = true```
<br>&ensp;&ensp;4.) Within Atlas, add ```atlas.feature.taxonomy.enable = true```  (Custom application-properties) 
<br>&ensp;&ensp;5.) Restart / Start - Ambari Infra, Ranger Tagsync, Hive, HBase, Atlas, Sqoop, Storm, Kafka
<br>&ensp;&ensp;6.) Turn on Maintenance Mode
<br>
<br>
<br><b>References:</b>
<br><a href="http://atlas.incubator.apache.org/">Apache Atlas</a>
<br><a href="http://hortonworks.com/apache/atlas/">Apache Atlas - Hortonworks</a>
