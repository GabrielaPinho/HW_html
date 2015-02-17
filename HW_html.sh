
for i in {1..800};
do curl 'https://www.eeb.ucla.edu/seminars.php?id='$i > $i.html;
done

# other way! curl 'https://www.eeb.ucla.edu/seminars.php?id=[0-800]' -o "file_#1.html"


