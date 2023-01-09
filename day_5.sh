# #!/bin/bash
# #./script.sh 5 #greets 5 times
# #alias greet3='./script.sh 3'
# first_greeting="Nice to meet you!"
# later_greeting="How are you?"
# greeting_occasion=0
# echo 'How many times should I greet?'
# #read greeting_limit
# greeting_limit=$1
# while [ $greeting_occasion -lt $greeting_limit ]
# do
#   if [ $greeting_occasion -lt 1 ]
#   then
#     echo $first_greeting
#   else
#     echo $later_greeting
#   fi
#   greeting_occasion=$((greeting_occasion + 1))
# done
#!/bin/bash
echo "🔥🔥###START BUILD###🔥🔥"
firstline=$(head -n 1 source/changelog.md)
read -a splitfirstline <<< $firstline
version=${splitfirstline[1]}
echo "###BUILDING VERSION🔥🔥" $version
echo "###TO CONTINUE PRESS 1 OR 0 TO STOP?"
read versioncontinue
if [ versioncontinue -eq 1 ]
then
  echo "OK"
else
  echo 'Please come back when you are ready'
fi

for filename in source/*
do
  echo $filename
  if [ '$filename' -eq  'source/secretinfo.md']
  then
    echo "Not Copying" $filename
  else
    echo "Copying" $filename
    cp $filename build/.
    echo "Build version $version contains:"
    ls  
done
ls build/
cd build/

 