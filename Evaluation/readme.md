
## Evaluation
- Use python2 for running evaluation

Evaluation tool is in _eval_

#### Preprocess
- put glove embedding in eval/word_emb.
- Please follow ```run1.sh``` to put test data.
- The results of converting test data to style 0 is put in style0.txt and style 1 respectively.
- test1 test2 test3 for different mode (autoencoder, style embedding. multi decoder).


#### Transfer Strength (Classifier)
```Usage
$ python classifier data        # process data of classifier
$ python classifier train       # train classifier
$ python classifier test test1  # test classifier
                                # test1 is the test result dir
                                # results in test1/embedding/style0_classification.txt ...

```

#### Content reservation


```CP
$cd eval
$python emb_test.py test1   # test1 is the test result dir
                           # results in test1/embedding/style0_semantics.txt ...
```


Finally, run ```python eval.py  > eval_result.txt``` to show results collection.

Example:-
```
dir_name model_type 	 transfer_strength 	 content_reservation 	 mixture
==============================================================================================
test1 	embedding8 		    0.4585 		      0.9438803062989316 	  0.3085961193937439
test1 	embedding6 	    	0.542 		      0.8960117473061905 	  0.33771515980289835
test1 	embedding1 		    0.5145 		      0.9156584887943305 	  0.3294084510045042
test1 	embedding7 		    0.4865 		      0.9145880600519364 	  0.3175725380164709
test1 	embedding 	    	0.548 		      0.8965986599545084 	  0.340119425052314
test1 	embedding2 		    0.4465 		      0.9434864821132846 	  0.3030725260170179
test1 	embedding5  		0.45 		      0.9440204290794388 	  0.3047367055920954
test1 	embedding4 		    0.5015 		      0.9153460001569551 	  0.32399147051116417
test1 	embedding3 		    0.5455 		      0.8956981594839047 	  0.3390257909942375
=============================================================================================
```