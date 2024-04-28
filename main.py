def main():
    book_path = "/mnt/c/Users/Thrishala s kariyar/Documents/workspace/github.com/hayley/bookbot/books/f.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)

    print(f"The number of {get_num_words(text)}")
    words= get_chars(text)
    print(get_chars(text))
    for i,v in words.items():
        if not i.isalpha():
            continue
        print(f"The '{i}' character was found {words[i]} times")
    print(chars_dict_to_sorted_list(words))
    chars_sorted_list = chars_dict_to_sorted_list(words)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_num_words(text):
    words=text.split()
    return len(words)

def get_chars(text):
    chars={}
    for c in text:
        lowered=c.lower()
        if lowered in chars:
            chars[lowered]+=1
        else:
            chars[lowered]=1
    return chars
  

def sort_on(d):
    return d["num"] 

def chars_dict_to_sorted_list(words):
    sorted_list = []
    for ch in words:
        sorted_list.append({"char": ch, "num": words[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

   



main()

