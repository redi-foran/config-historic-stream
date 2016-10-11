#!/bin/sh
echo -n 'Current directory is: '
pwd
ls *
echo "java -Xms1g -Xmx2g -server -XX:+UseCompressedOops -XX:+UseG1GC -XX:MaxGCPauseMillis=100 -verbose:gc -Dplatform.configPath=config -Dplatform.dataPath=data -Dplatform.logPath=logs -Dplatform.stripe=HTA1 -Dtextadmin.listenPort=1500 -DdiscoveryUrl=discovery://239.111.133.34:18014?ifName=eth1 -Dstatus.target=pulse://239.111.133.33:18013?ifName=eth1 -Dmain.log.udp=false -agentlib:jdwp=transport=dt_socket,server=y,suspend=n,address=2500 -DPackageScanner.ignoreManifest=true -DprocessName=sequencer -cp "libs/*" com.redi.platform.launcher.application.LauncherMain sequencer.commands"
java -Xms1g -Xmx2g -server -XX:+UseCompressedOops -XX:+UseG1GC -XX:MaxGCPauseMillis=100 -verbose:gc -Dplatform.configPath=config -Dplatform.dataPath=data -Dplatform.logPath=logs -Dplatform.stripe=HTA1 -Dtextadmin.listenPort=1500 -DdiscoveryUrl=discovery://239.111.133.34:18014?ifName=eth1 -Dstatus.target=pulse://239.111.133.33:18013?ifName=eth1 -Dmain.log.udp=false -agentlib:jdwp=transport=dt_socket,server=y,suspend=n,address=2500 -DPackageScanner.ignoreManifest=true -DprocessName=sequencer -cp "libs/*" com.redi.platform.launcher.application.LauncherMain sequencer.commands