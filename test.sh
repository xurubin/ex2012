#!/bin/bash

JCODE=ex2012
PCODE=naive.py
GEN=gen.py
DATA=data.txt
COUNT=5

/cygdrive/c/Program\ Files/Java/jdk1.7.0/bin/javac.exe $JCODE.java || exit 1

for i in {10,50,100,150,200} ; do
    for j in {10,50,100,150,200} ; do
	    for k in {1..5} ; do
		    echo Testing "$i * $j" "$k/5"
			python $GEN $i $j > $DATA
			python $PCODE < $DATA > expected.txt
			java $JCODE < $DATA > actual.txt
			diff --strip-trailing-cr expected.txt actual.txt > /dev/null
			if [ $? -eq 0 ] ; then
				echo "CORRECT"
			else
				echo "WRONG"
				diff --strip-trailing-cr expected.txt actual.txt
				exit 1
			fi
		done
	done
done

