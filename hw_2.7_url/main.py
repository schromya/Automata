import re

def get_urls(input: str) -> list[str]:
    """
    Gets URLS from input text
    :param input    String input to parse.
    :return         List of urls.
    """

    input = input.split()
    urls = []

    for word in input:
        if check_http(word):
            urls.append(word)
            continue

        if check_ip(word):
            urls.append(word)
            continue
        
        if check_suffix(word):
            urls.append(word)
            continue

    return urls


def check_http(word: str) -> bool:
    """
    Checks if the word is a http url
    :param word     Word to check
    :return         True if the word is an http url, else False
    """

    return bool(re.search(r"^http", word))


def check_ip(word: str):
    """
    Checks if the word is a ip url
    :param word     Word to check
    :return         True if the word is an ip url, else False
    """
    return bool(re.search(r"(([1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}([1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/", word))


def check_suffix(word: str):
    """
    Checks if the word has a proper url domain suffix (com .edu .org .net .gov)
    :param word     Word to check
    :return         True if the word is a url, else False
    """
    return bool(re.search(r"^[^@]+((.com)|(.org)|(.edu)|(.gov)).*$", word))



def main():

    input = """
    Hello Myra, you can email me at automata907@alaska.org or visit the website at
    alaska.org/automata and learn about the theory of computing! Or call me at 
    907.786.1234. Another way to learn about automata is to visit 
    192.229.210.176/automata_theory/index.htm or to go to
    https://en.wikipedia.org/wiki/Automata_theory for more information. Mr.Foo posted 
    in section 999.10.34.997 about the equivalence between finite state automata and 
    regular expressions. He regularly updates www.automata.com with the latest 
    developments.
    """

    print("-------------------------------------Original Text-------------------------------------")
    print(input)
    print("\n-------------------------------------Parsed URLs-------------------------------------")
    for url in get_urls(input):
        print(" ", url)

if __name__ == "__main__":
    main()