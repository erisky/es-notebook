#!/bin/bash

MYCMD_PATH=`realpath .`
NOTE_PATH=`realpath "../2017"`

echo $MYCMD_PATH
echo $NOTE_PATH
#alias note="~/.mycmds/mynote.py"

#alias qsdk="subl ~/work/note/es-notebook/2017/qsdk.txt"

echo -n "This will overwrite the bash_alias, are you sure? (y/n)? "
read yn

[ $yn != "y" ] && exit 0

echo OK

#WORDS=`ls ~/work/note/es-notebook/2017/`
#complete  -W "$WORDS" note
echo "" > ~/.bash_aliases
echo "alias note=\"$MYCMD_PATH/mynote.py\"" >> ~/.bash_aliases

echo "alias e=gvim" >> ~/.bash_aliases
#echo "alias qsdk=\"subl ~/work/note/es-notebook/2017/qsdk.txt" >> ~/.bash_aliases

echo "WORDS=\`ls $NOTE_PATH\`" >> ~/.bash_aliases
echo "complete  -W \"\$WORDS\" note" >> ~/.bash_aliases

