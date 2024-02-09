import argparse
from urllib.parse import urlparse
from uniseg.wordbreak import words

from wimbd.utils.utils import read_json_gz_file, read_jsonl_file, read_arrow_file

from tqdm import tqdm

def main():

    parse = argparse.ArgumentParser("")

    parse.add_argument("--in_file", type=str)

    args = parse.parse_args()

    # read compressed file
    # data = read_json_gz_file(args.in_file)
    
    # read jsonl file
    # data = read_jsonl_file(args.in_file)

    # read pyarrow (hf datasets) file
    data = read_arrow_file(args.in_file)

    for row in tqdm(data):
        tokenized_words = list(words(row['text']))
        word_count = len([x for x in tokenized_words if x != ' '])
        #print(urlparse(row['metadata']['url']).netloc, word_count)
        print(urlparse(row['url']).netloc, word_count)
	

if __name__ == "__main__":
    main()

