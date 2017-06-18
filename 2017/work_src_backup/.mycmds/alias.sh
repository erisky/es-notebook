

#alias note="subl ~/work/note/es-notebook/2017/note_2017.txt ~/work/note/es-notebook/Notes/openWRT/source_tree.txt"

alias note="~/.mycmds/mynote.py"

alias qsdk="subl ~/work/note/es-notebook/2017/qsdk.txt"

WORDS=`ls ~/work/note/es-notebook/2017/`
complete  -W "$WORDS" note

