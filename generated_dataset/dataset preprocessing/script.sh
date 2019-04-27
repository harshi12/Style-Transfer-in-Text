# php -a
# $result = preg_replace('/[\x00-\x1F\x80-\xFF]/', '', $file);
# $fp = fopen('train_sen1', 'w');
# fwrite($fp,$result);
# fclose($fp)
# exit
#!/usr/bin/php
# php script_remove_nonascii.php


cat sentiment.txt | sed '1,$ s/[[:digit:]]*\,\s*//g'> temp_sentiment.txt
cat temp_sentiment.txt | sed -e '1,$ s/sadness/0/g' -e '1,$ s/surprise/1/g' -e '1,$ s/worry/0/g' -e '1,$ s/anger/0/g' -e '1,$ s/boredom/0/g' -e '1,$ s/empty/0/g' -e '1,$ s/enthusiasm/1/g' -e '1,$ s/fun/1/g' -e '1,$ s/happiness/1/g' -e '1,$ s/hate/0/g' -e '1,$ s/love/1/g' -e '1,$ s/neutral/1/g' -e '1,$ s/relief/1/g'>s_twitter.txt
python3 python_script.py
cat train1.txt | sed '1,$ s/[[:digit:]]*\,\s*//g'> output.txt
cat output.txt | sed -e 's/http.*//g' > output1.txt
cat output1.txt | tr '[:upper:][:lower:]' '[:lower:][:lower:]' > q_twitter.txt
rm output.txt
rm output1.txt
rm temp_sentiment.txt
rm sentiment.txt
# rm train2.txt