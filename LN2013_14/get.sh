nothing=$(cat temp)
wget "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="$nothing
(awk '{print $6}' < linkedlist.php\?nothing\=$nothing)>temp
echo $nothing >> list
./get.sh
