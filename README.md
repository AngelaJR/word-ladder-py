# Python Word Ladder

## Project Specifications

In a Word Ladder puzzle, the challenge is to convert one word into another of the same length. At each step, you change one letter into another such that you still have an English word. The goal is to reach the target word in the minimum number of steps.

For example, to convert WARM to COLD, you could change WARM to WARD then WORD then CORD then COLD for a total of four steps. 
(Note that this must be a minimal ladder, since all four letters in WARM differ from those in COLD.)

For this to work, you will need a dictionary of four-letter words. I don’t particularly care which ones you use; you should make up a set of at least 25 words with several possible word ladders present. It is up to you to decide how to represent a word and how to represent the dictionary as a whole.

Solving word ladders is basically a graph search problem. Words are nodes in the graph, two words are adjacent if they differ by one letter, and a word ladder is a path in the graph. To find the most effecitve path breath-first search algorithm is used. 
