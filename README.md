# what is Entropy:
In information theory, the entropy of a text is the average level of "information", "surprise", or "uncertainty" inherent to each sequence of letters in the text. The entropy is calculated based on the probabilities of different sequences of symbols (of length m) appearing in the text. (Even spaces and special symbols like "'" and "." and so on count in the entropy calculus )

# How to use the code:
First store the folder you downloaded in a handy place, chose a text, then save it in the random.txt file, then run the 
text_entropy.py file. the code should be able to tell the language of text file you provided. For large text files, the degree of entropy should be around 5, for small text files use a degree around 2. Rule of thumb: the larger the text sample, the more precise the code. 
by default the degree is set to 5. In future commits more languages will be added.

# function.py:
function.py file contains all the calculations of the entropy of a given text, for a specific degree 'm' that the user choses.
We start by importing the io library for reading and writing data, and math library for use of log2 function. the Entropy function takes 2 
arguments: the name of the text and the degree of entropy. we read the text file using utf-8 encoding (due to its compatibility with ascii characters), we convert to lower case and remove any new line characters (so that they do not count as symbols), and define some variables that we are going to use later:
-length: length of the text file
alphabet_list: contains all symbols from the text
-cardinal: number of symbols of the alphabet_list / could be eventually used to verify if the entropy is correct (  0 &lt; H(s) &lt; log(cardinal) ; H(s) being the entropy )
-sum_symbols: length - degree
-sum_symbols0: length - (degree-1)
-dict_proba_m: dictionary of the symbols of length "m" as keys, and their probabilities as values (proba = frequency of apparition devided by sum of symbols), we proceed by slicing the text, each time a sequence of symbols is found we add to its value: 1/sum_symbols
-dict_proba_m0: dictionary of the symbols of length "m-1" as keys, and their probabilities as values, to fill the dictionary we proceed exactly like before.
-H: Entropy of the text of the degree 'm'

# text_entropy.py:
text_entropy.py file is used to compare the entropy of chosen text with the entropy of other text files of different languages.
we start by importing the Entropy function that we defined in the function.py file, and we set the degree that we like to apply. 
We open the text file chosen by the user with utf-8 encoding (due to its compatibility with ascii characters), for french, we create a text file that contains the same number of letters as the text chosen by the user (we draw it from french.txt file that contains a large text written in french), and print the result in french1.txt, we do the same for english. Finally, it's time to call the Entropy function, so we compare the entropy of random.txt file with french1.txt and english1.txt, and we print the result.  
 

