#!/bin/sh

TODAY=`date +20%y%m%d`
git archive --prefix=testserver/ -o ../testserver_${TODAY}.tar.gz HEAD

