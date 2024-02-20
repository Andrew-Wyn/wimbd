# WIMBD on CulturaX, HPLT,and RedPv2

To run python based scripts, you need to create and install a python environment using the ```
requirements.txt```
 file.

## CX analysis

python scripts
```
./cineca_run_cx.sh max_jobs
```

## HPLT analysis

python scripts
```
./cineca_run_hplt.sh max_jobs
```

## RedPajamaV2 analysis

python scripts
```
./cineca_run_rdpv2.sh max_jobs
```

## Python output

The python scripts will create a folder where will be saved several files, that contain the computed statistics

- ```ds_lang_wimbd_re/base_url_counter.jsonl``` base url and the number of documents

- ```ds_lang_wimbd_re/base_url_num_characters.jsonl``` base url and the number of characters

- ```ds_lang_wimbd_re/base_url_words.jsonl``` base url and the number of words

- ```ds_lang_wimbd_re/suffix_counter.jsonl``` suffix and the number of documents

- ```ds_lang_wimbd_re/word_counter.jsonl``` number of words per document and their occurrencies for all the dataset

- ```ds_lang_wimbd_re/general_statistics.jsonl``` number of characters and number of documents for all the dataset