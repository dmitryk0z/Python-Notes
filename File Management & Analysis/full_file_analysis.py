"""
Full File Analysis

Program to perform full file analysis on the selected txt file provided by the user, 
to find the number of characters, words and lines used in the file. Program can also
list top occurring words in the selected txt file.
"""

KEEP = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
        ' ', '-', "'"}


def Normalise(s):
    result = ''

    for x in s.lower():
        if x in KEEP:
            result = result + x

    return result


def FreqDict(s):
    new_string = Normalise(s)
    words = new_string.split()
    new_dict = {}

    for word_index in words:
        if word_index in new_dict:
            new_dict[word_index] = new_dict[word_index] + 1
        else:
            new_dict[word_index] = 1

    return new_dict


def FileAnalysis(file_name, top_occur):
    script = open(file_name, 'r').read()
    num_chars = len(script)
    num_lines = script.count("\n")
    num_words = len(script.split())

    full_dict = FreqDict(script)
    dict_array = []

    for k in full_dict:
        pair = (full_dict[k], k)
        dict_array.append(pair)

    dict_array.sort()
    dict_array.reverse()

    print("The file '%s' has:" % file_name)
    print("    %s characters" % num_chars)
    print("    %s lines" % num_lines)
    print("    %s words" % num_words)
    print(" ")
    print("The top %d most occurring words are:" % top_occur)

    i = 1

    for count, word in dict_array[:top_occur]:
        print('%3s. %5s %s' % (i, count, word))
        i = i + 1


def main():
    try:
        print('\nLocation of the filename you wish to analyse:')
        file_name = input()
        print('How many more frequently occurring words:')
        top_occur = int(input())
        FileAnalysis(file_name, top_occur)
    except IOError as e1:
        print('File does not exist or incorrect file name provided --->', e1)
        main()
    except ValueError as e2:
        print('\nPlease provide integers only to avoid the following error --->', e2)
        main()


if __name__ == '__main__':
    main()
