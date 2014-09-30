#cats script for sprunge.us

date
#echo `history |tail -n2 |head -n1` | sed 's/[0-9]* //' | sed 's/^/krsumeet@ArchLinux ~ \$ /'
echo -e "cat $1" | sed 's/^/krsumeet@ArchLinux ~ \$ /'
cat $1
echo -e "" | sed 's/^/krsumeet@ArchLinux ~ \$ /'
