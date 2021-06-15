# Exam Assignment
# Programmer Name: Jin Li
# Date: 1/9/2021
# Course Name and Term: CS X458.05 - Data Structures and Algorithms (EXT Fall 2020)
# Program Title: Simple Demo of google search autocomplete.
# Description: Given an input (prefix), return all words begin with the prefix and the 5 most commonly used ones.

class TreeNode():
    def __init__(self, c):
        self.char = c
        self.weight = 0 # 0 not a word
        self.child = {} #dictionary of TrieNode

class Tree():
    def __init__(self):
        self.root = TreeNode("")

    def insert(self, word, weight):
        node = self.root
        for char in word:
            if char in node.child:
                node = node.child[char]
            else:
                newNode = TreeNode(char)
                node.child[char] = newNode
                node = newNode
        node.weight = weight

    #given a prefix, return all words start with the prefix
    def getWord(self,prefix):
        node = self.root
        for char in prefix:
            if char not in node.child:
                return "No match result found"
            node = node.child[char]
        res_dic = {}
        if node.weight > 0:
            res_dic[node.weight] = prefix
        self.helper(node.child, prefix, res_dic)
        return res_dic

    # helper serves getWord, helper traverse the tree and maintain a dictionary for return
    def helper(self, dic, maxString, res_dic):
        if dic == None:
            return
        for key in dic:
            if dic[key].weight > 0:
                res_dic[dic[key].weight] = maxString + key
            self.helper(dic[key].child, maxString + key, res_dic)

    #given a prefix, return the top 10 most commonly used words
    def weightedListTop10(self,dic):
        numList = []
        for key in dic:
            numList.append(key)
        self.bubbleSort(numList)
        weightedWordList = []
        for i in numList[:5]:
            weightedWordList.append(dic[i])
        return weightedWordList

    #given a num list, sort it using bubble sort and then return it back
    def bubbleSort(self, aList):
        for i in range(len(aList)):
            for j in range(1, len(aList) - i):
                if aList[j-1] < aList[j]:
                    temp = aList[j-1]
                    aList[j-1] = aList[j]
                    aList[j] = temp
        return aList

#Build the word search tree
wordSearchTree = Tree()
inputFile = open("Data_google-10000-english.txt", "r")
weight = 10000
for line in inputFile:
    wordSearchTree.insert(line.strip(), weight)
    weight -= 1

prefix = input("please enter the prefix you'd like to search")
print("The words begin with the prefix are:")
words_dic = wordSearchTree.getWord(prefix)
for key in words_dic:
    print(words_dic[key])
print("")
print("The 5 most commonly used words are:")
weighted_word_list = wordSearchTree.weightedListTop10(words_dic)
for i in weighted_word_list:
    print(i)

