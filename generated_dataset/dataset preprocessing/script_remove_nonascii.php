<?php
$file = file_get_contents('train.txt');
$result = preg_replace('/[\x00-\x1F\x80-\xFF]/', '', $file);
$fp = fopen('train1.txt', 'w');
fwrite($fp,$result);
fclose($fp)
?>
