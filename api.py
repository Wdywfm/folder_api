import json
import os
import re

from flask import Flask, Response
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


def scan_file(path):
    words = []
    reg = r"\b[a-zA-Zа-яёА-ЯЁ]+-?[a-zA-Zа-яёА-ЯЁ]+\b"
    try:
        with open(path) as file:
            for line in file:
                words.extend(re.findall(reg, line))
    except UnicodeDecodeError:
        with open(path, encoding="utf-8", errors="ignore") as file:
            for line in file:
                words.extend(re.findall(reg, line))
    return words


def scan_dir(path):
    files = []
    folders = []
    words = []
    for smth in os.listdir(path):
        new_path = os.path.join(path, smth)
        if os.path.isfile(new_path):
            if re.match(".*\\.(txt|py|md)\\Z", smth):
                files.append(new_path)
                words.extend(scan_file(new_path))
        else:
            folders.append(new_path)
            new_files, new_folders, new_words = scan_dir(new_path)
            files.extend(new_files)
            folders.extend(new_folders)
            words.extend(new_words)
    return files, folders, words


def count_words(words: list):
    frequency = {}
    len_words = 0
    for word in words:
        len_words += len(word)
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency, len_words


def find_most_common_words(frequency: dict):
    most_common_words = {}
    for word in sorted(frequency, key=frequency.get, reverse=True):
        most_common_words[word] = frequency[word]
        if len(most_common_words) == 25:
            break
    return most_common_words


def find_the_rarest_words(frequency: dict):
    the_rarest_words = {}
    for word in sorted(frequency, key=frequency.get):
        the_rarest_words[word] = frequency[word]
        if len(the_rarest_words) == 25:
            break
    return the_rarest_words


def get_letter_stats(words: list):
    letter_dict = {"English letters": {}, "Russian letters": {}}
    vowel = 0
    consonant = 0
    for word in words:
        for c in word:
            c = c.lower()
            if c != "-":
                if 96 < ord(c) < 123:
                    if c in letter_dict["English letters"]:
                        letter_dict["English letters"][c] += 1
                    else:
                        letter_dict["English letters"][c] = 1
                else:
                    if c in letter_dict["Russian letters"]:
                        letter_dict["Russian letters"][c] += 1
                    else:
                        letter_dict["Russian letters"][c] = 1
                if c in "aeiuyoаоуэыяёюеи":
                    vowel += 1
                else:
                    consonant += 1
    return letter_dict, vowel, consonant


class Stats(Resource):
    def get(self):
        response = Response(data)
        response.headers["Content-Type"] = "application/json"
        return response


class Files(Resource):
    def get(self, file_id: int):
        if file_id >= len(files):
            return f"File with {file_id} index doesn't exist"
        lines = ""
        try:
            with open(files[file_id]) as file:
                for line in file:
                    lines += line
        except UnicodeDecodeError:
            with open(files[file_id], encoding="utf-8",
                      errors="ignore") as file:
                for line in file:
                    lines += line
        response = Response(lines)
        response.headers["Content-Type"] = "text/html; charset=utf-8"
        return response


class Words(Resource):
    def get(self, word_id: int):
        if word_id >= len(words):
            return f"Word with {word_id} index doesn't exist"
        response = Response(words[word_id])
        response.headers["Content-Type"] = "text/html; charset=utf-8"
        return response


while True:
    path = input("Input path: ")
    if os.path.exists(path):
        break
    print("This path does not exist")
files, folders, words = scan_dir(path)
print(f"Possible file indexes: 0-{len(files)-1}")
print(f"Possible word indexes: 0-{len(words)-1}")
words_frequency, word_length = count_words(words)
most_common_words = find_most_common_words(words_frequency)
the_rarest_words = find_the_rarest_words(words_frequency)
try:
    average_word_size = word_length / len(words)
except ZeroDivisionError:
    average_word_size = 0
average_word_size = round(average_word_size, 2)
letters, vowels, consonants = get_letter_stats(words)
letters["English letters"] = dict(sorted(letters["English letters"].items()))
letters["Russian letters"] = dict(sorted(letters["Russian letters"].items()))
data = {
    "files": files,
    "folders": folders,
    "number_of_files": len(files),
    "top_25_of_most_common_words": most_common_words,
    "top_25_of_the_rarest_words": the_rarest_words,
    "average_word_size": average_word_size,
    "letters": letters,
    "vowels": vowels,
    "consonants": consonants,
}
data = json.dumps(data, indent=4, ensure_ascii=False)

api.add_resource(Stats, "/api/stats")
api.add_resource(Files, "/api/files/<int:file_id>")
api.add_resource(Words, "/api/words/<int:word_id>")

if __name__ == "__main__":
    app.run()
