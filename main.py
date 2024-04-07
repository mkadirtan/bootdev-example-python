def print_report(chr_app: dict):
    arr = dict_to_arr(chr_app)
    arr.sort(key=sort_on('val'), reverse=True)

    print("--- Begin report ---")
    for item in arr:
        if not item['key'].isalpha():
            continue
        print(f"The {item['key']} appears {item['val']} times")
    print("--- End report ---")


def count_character_appearance(text: str):
    dictionary = {}
    for c in text.lower():
        if c in dictionary:
            dictionary[c] += 1
        else:
            dictionary[c] = 1
    return dictionary


def sort_on(key: str):
    def sort_on_key(d: dict):
        return d[key]

    return sort_on_key


def dict_to_arr(d: dict):
    arr = []
    for key, val in d.items():
        arr.append({'key': key, "val": val})
    return arr


def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    chr_app = count_character_appearance(file_contents)
    print_report(chr_app)


main()
