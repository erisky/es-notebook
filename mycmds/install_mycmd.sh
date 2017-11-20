#!/bin/bash

MYCMD_PATH=`realpath .`
NOTE_PATH=`realpath "../2017"`

echo $MYCMD_PATH
echo $NOTE_PATH

echo " This installation will do the following thins:"
echo "1. Add e, note aliases"
echo "2. export $$MYCMD_PATH/bin to PATH env"
echo "3. add complete for notes"


echo -n "This will overwrite the bash_alias, are you sure? (y/n)? "
read yn

[ $yn != "y" ] && exit 0


echo "" > ~/.bash_aliases
echo "alias note=\"$MYCMD_PATH/mynote.py\"" >> ~/.bash_aliases

echo "alias e=gvim" >> ~/.bash_aliases

echo "WORDS=\`ls $NOTE_PATH\`" >> ~/.bash_aliases
echo "complete  -W \"\$WORDS\" note" >> ~/.bash_aliases

echo "export PATH=\$PATH:$MYCMD_PATH/bin" >> ~/.bash_aliases
echo "export MYNOTE_PATH=$NOTE_PATH" >> ~/.bash_aliases



echo OK


