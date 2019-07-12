# folder_api
An app that scans folders with all subfolders and txt, py, md files.
## Example usage
```
$ python api.py
Inputh path: E:\some_folder
Possible file indexes: 0-7
Possible word indexes: 0-569
* Running on http://127.0.0.1:5000/
```
## GET stats
```
$ curl http://127.0.0.1:5000/api/stats
{
    "files": [
        "E:\\some_folder\\another_folder\\folder\\a.txt",
        "E:\\some_folder\\another_folder\\folder\\b.txt",
        "E:\\some_folder\\another_folder\\folder\\hw1.py",
        "E:\\some_folder\\another_folder\\folder\\hw1.txt",
        "E:\\some_folder\\another_folder\\folder\\hw2.py",
        "E:\\some_folder\\another_folder\\folder\\hw2.txt",
        "E:\\some_folder\\another_folder\\folder2\\hw3.py",
        "E:\\some_folder\\another_folder\\folder2\\hw3.txt",
        "E:\\some_folder\\another_folder\\folder2\\hw4.py",
        "E:\\some_folder\\another_folder\\folder2\\hw4.txt"
    ],
    "folders": [
        "E:\\some_folder\\another_folder",
        "E:\\some_folder\\another_folder\\folder",
        "E:\\some_folder\\another_folder\\folder2"
    ],
    "number_of_files": 10,
    "top_25_of_most_common_words": {
        "func": 17,
        "start": 13,
        "print": 13,
        "stop": 12,
        "def": 11,
        "return": 10,
        "функции": 10,
        "аргументов": 10,
        "doc": 10,
        "alphabet": 9,
        "значение": 9,
        "принимает": 7,
        "функцию": 7,
        "step": 6,
        "index": 6,
        "которая": 6,
        "качестве": 6,
        "smth": 5,
        "по": 5,
        "умолчанию": 5,
        "atom": 5,
        "setv": 5,
        "переменной": 5,
        "None": 4,
        "for": 4
    },
    "top_25_of_the_rarest_words": {
        "some": 1,
        "text": 1,
        "некоторый": 1,
        "текст": 1,
        "abcdefghijklmnopqrstuvwxyz": 1,
        "Некоторые": 1,
        "встроенные": 1,
        "Python": 1,
        "имеют": 1,
        "нестандартное": 1,
        "когда-то": 1,
        "дело": 1,
        "касается": 1,
        "Например": 1,
        "от": 1,
        "которые": 1,
        "обычно": 1,
        "называются": 1,
        "использовании": 1,
        "всех": 1,
        "трех": 1,
        "именно": 1,
        "таком": 1,
        "этом": 1,
        "ноль": 1
    },
    "average_word_size": 6.23,
    "letters": {
        "English letters": {
            "a": 70,
            "b": 13,
            "c": 48,
            "d": 40,
            "e": 115,
            "f": 42,
            "g": 24,
            "h": 19,
            "i": 43,
            "j": 1,
            "k": 6,
            "l": 29,
            "m": 26,
            "n": 92,
            "o": 61,
            "p": 62,
            "q": 1,
            "r": 83,
            "s": 74,
            "t": 125,
            "u": 39,
            "v": 13,
            "w": 6,
            "x": 9,
            "y": 6,
            "z": 1
        },
        "Russian letters": {
            "а": 191,
            "б": 34,
            "в": 99,
            "г": 33,
            "д": 46,
            "е": 254,
            "ж": 9,
            "з": 71,
            "и": 231,
            "й": 29,
            "к": 83,
            "л": 75,
            "м": 106,
            "н": 229,
            "о": 239,
            "п": 85,
            "р": 105,
            "с": 70,
            "т": 140,
            "у": 83,
            "ф": 25,
            "х": 18,
            "ц": 33,
            "ч": 52,
            "ш": 8,
            "щ": 8,
            "ы": 44,
            "ь": 35,
            "э": 5,
            "ю": 24,
            "я": 59,
            "ё": 1
        }
    },
    "vowels": 1465,
    "consonants": 2107
}
```
## GET file by index
```
$ curl http://127.0.0.1:5000/api/files/1
some text
некоторый текст
```
## GET word by index
```
$ curl http://127.0.0.1:5000/api/words/0
some
```
