#!/bin/bash

#let "fl = 0"
#cat switch.cfg | grep -E "host_name|address|parents" | while read line
#do
#	a=`echo ${line} | tr -s ' ' | cut -f 1 -d ' '`
#	case $a in
#	"host_name" ) host="`echo ${line} | tr -s ' ' | cut -f 2 -d ' '`+`echo ${line} | tr -s ' ' | cut -f 3 -d ' '`+`echo ${line} | tr -s ' ' | cut -f 4 -d ' '`"
#	    #echo "host"
#	    let "fl = 1";;
#	"address" ) ip=`echo ${line} | tr -s ' ' | cut -f 2 -d ' '`
#	    #echo "ip"
#	    let "fl = 2";;
#	esac
#	if [ "$fl" -gt 1 ];
#	then echo "$host $ip" >> sw_tmp.txt
#	let "fl = 0"
#	fi
#done

let "fl = 0"
cat switch.cfg | grep -E "host_name|address|parents" | while read line
do
	a=`echo ${line} | tr -s ' ' | cut -f 1 -d ' '`
	case $a in
	"host_name" ) host="`echo ${line} | tr -s ' ' | cut -f 2 -d ' '`-`echo ${line} | tr -s ' ' | cut -f 3 -d ' '`-`echo ${line} | tr -s ' ' | cut -f 4 -d ' '`"
	    #echo "host"
	    let "fl = 1";;
	"address" ) ip=`echo ${line} | tr -s ' ' | cut -f 2 -d ' '`
	    #echo "ip"
	    let "fl = 2";;
	"parents" ) father="`echo ${line} | tr -s ' ' | cut -f 2 -d ' '`+`echo ${line} | tr -s ' ' | cut -f 3 -d ' '`+`echo ${line} | tr -s ' ' | cut -f 4 -d ' '`"
	    fatherip=`grep $father sw_tmp.txt | tr -s ' ' | cut -f2 -d ' '`
	    let "fl = 3";;
	esac
	if [ "$fl" -gt 2 ];
	then nordwest=`curl http://geocode-maps.yandex.ru/1.x/?geocode=rybinsk+${host//-/+} | grep pos | sed -e :a -e 's/<[^>]*>//g;/</N;//ba'`
	nord=`echo $nordwest | tr -s ' ' | cut -f2 -d ' '`
	west=`echo $nordwest | tr -s ' ' | cut -f1 -d ' '`
	addr=`curl http://geocode-maps.yandex.ru/1.x/?geocode=rybinsk+${host//-/+} | grep AddressLine | sed -e :a -e 's/<[^>]*>//g;/</N;//ba'`
	fulladdr=`echo ${addr// /+} | tr -s ' ' | cut -f1 -d ' '`
	echo "${host};${fulladdr//+/ };$ip;$nord;$west;${father//-/+};$fatherip;" | tr -s ' ' >> sw.txt
	let "fl = 0"
	fi
done
