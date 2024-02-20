import json
import sys
from collections import defaultdict
import logging
import numpy as np
from pathlib import Path
import argparse
from tqdm import tqdm

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

def main():

    parse = argparse.ArgumentParser("")

    parse.add_argument("--outputdir", type=str)

    args = parse.parse_args()

    outputdir_path = Path(args.outputdir)

    outputdir_path.mkdir(parents=True, exist_ok=True)

    # base url counter
    base_url_counter = defaultdict(int)
    # num words counter, by base url
    base_url_num_words = defaultdict(int)
    # num character counter, by base url
    base_url_num_characters = defaultdict(int)
    # suffic counter
    suffix_counter = defaultdict(int)

    # general statistics
    word_count_document = defaultdict(int)
    character_count_document = 0
    min_cc_d = None
    max_cc_d = None
    number_docs = 0

    # reduce sequentially all the parallel computations docwise
    for line in tqdm(sys.stdin):
        try:
            base_url, suffix, word_count, character_count = line.strip().split()
            
            base_url_counter[base_url]              += 1
            base_url_num_words[base_url]            += int(word_count)
            base_url_num_characters[base_url]       += int(character_count)
            suffix_counter[suffix]                  += 1
            
            word_count_document[int(word_count)]    += 1
            number_docs                             += 1
            character_count_document                += int(character_count)

            if min_cc_d is None:
                min_cc_d = int(character_count)
                max_cc_d = int(character_count)

            min_cc_d                            = min_cc_d if int(character_count) > min_cc_d else int(character_count)
            max_cc_d                            = max_cc_d if int(character_count) < max_cc_d else int(character_count)

        except Exception as e:
            logging.info(line)
            logging.info("Error occurred")
            logging.info(e)
            pass

    with open(outputdir_path / "base_url_counter.jsonl", "w") as f:
        for k, v in base_url_counter.items():
            f.write(json.dumps({'url': k, 'count': v}) + "\n")

    with open(outputdir_path / "base_url_num_words.jsonl", "w") as f:
        for k, v in base_url_num_words.items():
            f.write(json.dumps({'url': k, 'words': v}) + "\n")

    with open(outputdir_path / "base_url_num_characters.jsonl", "w") as f:
        for k, v in base_url_num_characters.items():
            f.write(json.dumps({'url': k, 'characters': v}) + "\n")

    with open(outputdir_path / "suffix_counter.jsonl", "w") as f:
        for k, v in suffix_counter.items():
            f.write(json.dumps({'suffix': k, 'count': v}) + "\n")

    with open(outputdir_path / "word_counter.jsonl", "w") as f:
        for k, v in word_count_document.items():
            f.write(json.dumps({'number_words': k, 'count': v}) + "\n")

    with open(outputdir_path / "general_statistics.jsonl", "w") as f:
        f.write(json.dumps({'average number of characters': character_count_document / number_docs}) + "\n")
        f.write(json.dumps({'min number of characters': min_cc_d}) + "\n")
        f.write(json.dumps({'max number of characters': max_cc_d}) + "\n")
        f.write(json.dumps({'number_docs': number_docs}) + "\n")


if __name__ == "__main__":
    main()