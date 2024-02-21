import argparse
from urllib.parse import urlparse
import tldextract
from uniseg.wordbreak import words
from wimbd.utils.utils import read_json_gz_file, read_jsonl_file, read_arrow_file, read_jsonl_smart_open_file

CULTA_X_SOURCES=["mC4", "OSCAR-2301", "OSCAR-2201"]

def main():

    parse = argparse.ArgumentParser("")

    parse.add_argument("--in_file", type=str)

    parse.add_argument("--load", type=str)

    parse.add_argument("--dataset", type=str)

    args = parse.parse_args()

    if args.load == "json":
        data = read_jsonl_smart_open_file(args.in_file)
    elif args.load == "gz":
        data = read_json_gz_file(args.in_file)
    elif args.load == "arrow":
        data = read_arrow_file(args.in_file)
        
    # stopper = 0
    for row in data:

        if args.dataset == "culturax":
            if not row["source"] in CULTA_X_SOURCES:
                continue

        if args.dataset == "redpajamav2":
            text_field = "raw_content"
            base_url = row["source_domain"]
        else:
            base_url = urlparse(row['url']).netloc
            text_field = "text"

        tokenized_words = list(words(row[text_field]))
        # unicode text segmentation
        word_count = len([x for x in tokenized_words if x != ' ']) # count the number of words for each document
        character_count = len(row[text_field]) # count the number of characters (space included) for each document
        
        # extract suffix
        suffix = tldextract.extract(row['url']).suffix
        if suffix == "":
            suffix = "None"

        # base-url, suffix, number of words, number of characters 
        print(base_url, suffix , word_count, character_count)

        # stopper += 1
        # if stopper == 2:
        #     return


if __name__ == "__main__":
    main()