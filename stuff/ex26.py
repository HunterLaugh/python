#coding:utf-8 
# 修正代码  test

import ex25

# sentence  string 切分成word []
def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

# 排序 []
def sort_words(words):
    """Sorts the words."""
    return sorted(words)

# 打印 第一个 words[0]
def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print(word) 

# 打印最后一个 words[-1]
def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print (word)

# 拆分sentence 为words ，并对words排序
def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

# 打印第一个与最后一个
def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)


print ("Let's practice everything.")
print ('You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.')

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explantion
\n\t\twhere there is none.
"""


print ("--------------")
print (poem)
print ("--------------")

five = 10 - 2 + 3 - 5
print ("This should be five: %s" % five)

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point)

print ("With a starting point of: %d" % start_point)
print ("We'd have %d jeans, %d jars, and %d crates." % (beans, jars, crates))

start_point = start_point / 10

print ("We can also do that this way:")
print ("We'd have %d beans, %d jars, and %d crabapples." % secret_formula(start_point))


sentence = "All good\tthings come to those who weight."

words = break_words(sentence)
sorted_words = sort_words(words)

print_first_word(words)
print_last_word(words)
print_first_word(sorted_words)
print_last_word(sorted_words)
sorted_words = ex25.sort_sentence(sentence)
print (sorted_words)

print_first_and_last(sentence)

print_first_and_last_sorted(sentence)
