#!/bin/bash

WORKING_PATH=`pwd`
if [ ! -f ${WORKING_PATH}/install_mycmd.sh ]; 
then
    echo "must execute in the script's path" 
    exit 0

fi

ESNOTE_ROOT=`realpath ..`
MYCMD_PATH=`realpath .`
#NOTE_PATH=`realpath "../2018"`

echo "input the year to setup, ex: 2018"
read year

NOTE_PATH=`realpath "../${year}/note"`

[ -d "${NOTE_PATH}" ] || echo "folder not exist" 
[ -d "${NOTE_PATH}" ] || exit

echo $MYCMD_PATH
echo $NOTE_PATH

echo " This installation will do the following thins:"
echo "1. Add e, note aliases"
echo "2. export $MYCMD_PATH/bin to PATH env"
echo "3. add complete for notes"


echo -n "This will overwrite the bash_alias, are you sure? (y/n)? "
read yn

[ $yn != "y" ] && exit 0


echo "" > ~/.bash_aliases

cat alias_base.txt >> ~/.bash_aliases 

echo "alias note=\"$MYCMD_PATH/mynote.py\"" >> ~/.bash_aliases

echo "alias e=gvim" >> ~/.bash_aliases

echo "WORDS=\`ls $NOTE_PATH\`" >> ~/.bash_aliases
echo "complete  -W \"\$WORDS\" note" >> ~/.bash_aliases

echo "export PATH=\$PATH:$MYCMD_PATH/bin" >> ~/.bash_aliases
echo "export MYNOTE_PATH=$NOTE_PATH" >> ~/.bash_aliases
echo "export ESNOTE_ROOT=${ESNOTE_ROOT}" >> ~/.bash_aliases

echo "alias np=\"cd ${ESNOTE_ROOT}\"" >> ~/.bash_aliases

echo OK


