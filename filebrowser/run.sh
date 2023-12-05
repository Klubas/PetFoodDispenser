#!bin/sh

DB=/config/filebrowser.db
AUTH=proxy
CHOWN_DEST='chown 1000:1000 $DESTINATION'
CHMOD_DEST='chmod 755 $DESTINATION'

CHOWN_FILE='chown 1000:1000 $FILE'
CHMOD_FILE='chmod 755 $FILE'


if [ ! -f "$DB" ]; then
    echo "$DB not exists. Creating..."
    /filebrowser config init --database=$DB
    /filebrowser users add lucas.kluber@gmail.com $(echo $RANDOM | md5sum | head -c 20) --database=$DB
else
    echo "Clean commands that run on events"
    /filebrowser cmds rm after_copy     0 1 --database=$DB > /dev/null
    /filebrowser cmds rm after_rename   0 1 --database=$DB > /dev/null
    /filebrowser cmds rm after_save     0 1 --database=$DB > /dev/null
    /filebrowser cmds rm after_upload   0 1 --database=$DB > /dev/null
fi

#echo "Set commands to run on events"
#/filebrowser cmds add after_copy $CHOWN_DEST --database=$DB > /dev/null
#/filebrowser cmds add after_copy $CHMOD_DEST --database=$DB > /dev/null

#/filebrowser cmds add after_rename $CHOWN_DEST --database=$DB > /dev/null
#/filebrowser cmds add after_rename $CHMOD_DEST --database=$DB > /dev/null

#/filebrowser cmds add after_save $CHOWN_FILE --database=$DB > /dev/null
#/filebrowser cmds add after_save $CHMOD_FILE --database=$DB > /dev/null

#/filebrowser cmds add after_upload $CHOWN_FILE --database=$DB > /dev/null
#/filebrowser cmds add after_upload $CHMOD_FILE --database=$DB > /dev/null

#echo "Set auth method via proxy"
#/filebrowser config set --database=$DB --auth.method=$AUTH --auth.header=Remote-Email 
/filebrowser config set --database=$DB --auth.method=noauth

echo "Starting Server"
/filebrowser --root=/data --address=0.0.0.0 --database=$DB

