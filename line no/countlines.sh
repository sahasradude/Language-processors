i=0;
read file
while read -r LINE; do
   ((i+=1));
    done < "$file";
echo $i
