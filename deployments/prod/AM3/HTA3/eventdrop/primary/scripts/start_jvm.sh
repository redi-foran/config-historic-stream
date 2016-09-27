#!/bin/sh
java \
	-Xms1g \
	-Xmx2g \
	-server \
	-XX:+UseCompressedOops \
	-XX:+UseG1GC \
	-XX:MaxGCPauseMillis=100 \
	-verbose:gc \
	-Dplatform.configPath=config \
	-Dplatform.dataPath=data \
	-Dplatform.logPath=logs \
	-Dplatform.stripe=HTA3 \
	-Dtextadmin.listenPort=1501 \
	-DdiscoveryUrl=discovery://239.111.130.34:18014?ifName=eth1 \
	-Dstatus.target=pulse://239.111.130.33:18013?ifName=eth1 \
	-Dmain.log.udp=false \
	-agentlib:jdwp=transport=dt_socket,server=y,suspend=n,address=2501 \
	-DPackageScanner.ignoreManifest=true \
	-DprocessName=eventdrop \
	-cp "libs/*" \
	com.redi.platform.launcher.application.LauncherMain \
	eventdrop.commands