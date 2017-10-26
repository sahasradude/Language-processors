#!/bin/bash
ln=`echo "$1" | bash ./countlines.sh`
i=1;
while [ $i -lt $((ln+1)) ]; do
    sed -n "$i s/^/$i\./p" "$1" >> "$2"
    ((i+=1));
done

