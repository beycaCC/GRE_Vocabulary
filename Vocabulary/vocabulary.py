import os
from re import M
import sys

# set a list to store the words in order
word_list = []
word_list.append("abandon")
word_list.append("abase")
word_list.append("abash")
word_list.append("abate")
word_list.append("abbreviate")
word_list.append("abdicate")
word_list.append("abberrant")
word_list.append("abet")
word_list.append("abeyance")
word_list.append("abhor")
# print(word_list)

# set up a meaning list
meaning_list = []
meaning_list.append("放纵; 放弃 -- carefree, freedom from constraint/ to withdraw from often in the face of danger or encroachment")
meaning_list.append("降低(地位, 职位, 威望或尊严) -- to lower in rank, office, prestige, or esteem")
meaning_list.append("使尴尬, 使羞愧 -- to destroy the self-possession or self-confidence of, disconcert embarrass")
meaning_list.append("减轻(程度或强度); 减少(数量), 降低(价值) -- to reduce in degree or intensity; to reduce in amount or value")
meaning_list.append("缩写, 缩短 -- to make brifer")
meaning_list.append("正式放弃(权利, 责任), 不干了 -- to renounce a throne, to relinquish (power or responsibility) formally")
meaning_list.append("异常的, 非常规的 -- deviating from the usual or natural type")
meaning_list.append("鼓励 -- to actively encourage (as an activity or plan)")
meaning_list.append("中止, 搁置 -- temporary inactivity")
meaning_list.append("深恶痛绝, 极度厌恶 -- to regard with extreme repugnance")

# use a loop to print each meaning, then do check of spell and word in word_list
j = 0
for i in meaning_list:
    print(i)
    # spell the word -- input the word
    spell = input("Spell the word: ")
    if spell == word_list[j]:
        print("corrent")
    else:
        print("Wrong!")
    j += 1

# TODO:
# add time limit
# add if wrong, output the correct answer (repeat later)
# add to see the answer temporary
# add a sys of counting the successes, failnesses, and see the answer to build a summary
# build them as a database
