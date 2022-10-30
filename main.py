import math
import re
import pandas as pd

words_file = 'input/WordsToFind.csv'
search_file = 'input/TextToSearch.txt'


def get_word_counts():
    # Read the words file into a pandas dataframe
    df = pd.read_csv(words_file)
    # Get the text from the search file
    file_obj = open(search_file, "r")
    text = file_obj.read()
    for i in df.index:
        df.at[i, 'Count'] = math.trunc(len(re.findall(df.at[i, 'Word'], text, flags=re.IGNORECASE)))
    df.to_csv('output/WordCounts.csv', header=True, index=False)


def main() -> None:
    # Get the count of matching words using regex & output to word counts file
    get_word_counts()


if __name__ == "__main__":
    main()
