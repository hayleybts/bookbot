def main():
    book_path = "/mnt/c/Users/hay/Documents/workspace/github.com/hayley/bookbot/books/f.txt"
    text = get_book_text(book_path)
    print(f"The number of {get_num_words(text)}")
    print(get_chars(text))

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
  



main()

