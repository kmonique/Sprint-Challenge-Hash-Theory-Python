1. What is a regular expression and how does it work?

   A regular expression is a method of matching or finding all sequence of characters or bytes in a given piece of text/html.  Regex uses the re library and methods like findall(), search(), and match() to take in the regular expresion (what the user wishes to find proceeded by the letter "r") and the content the expression is searching through.

   for example: findall(regex, content)

   Regular expression flags can find number, characters, hidden escape characters like \n, and spaces amongst other things.  Furthermore, multipliars can be used to signify 0 or 1, 0 or more, or 1 or more times, or denote a specific amount of times a character is repeated.

   for example: [G]{1}[O]+[A]{,5}[L]{1, 6}[S]*[!]?

   In the above example:
      G is found once 
      followed by one or more O's
      followed by up to 5 A's
      followed by between 1-6 L's
      followed by 0 or more S's
      followed by 0 or one ?'s

2. What is an array and how does it work?

   An array or a list is a container that holds a fixed number of elements.  Likewise a developer can access the value of these elements by using its index.

   for example: array = []

   The above example creates an empty array with no elements. In python the size of the array adjusts automatically when elements are added. However, in other languages like C the size of the array has to be adjusted manually. For example array.append(2) adds 2 into index 0 or our current array.  We can access the value through array[0]. 

   for example: array = [None] * 4

   In the above example an array is created with indexes 0-3 and a capacity of 4.  However if we add indexes 4-7 the array written to memory is deleted and recreated 4 times.  Likewise as the continue to add more indexes we continue to rewrite the array in memeory. On way to minimize this is to double the size of the array if we are adding indexes past its current capacity.

3. What is a hash table and how does it work?

   A hash table is simular to a dictionary because they both store key value pairs. However hash tables use indexs as keys to store unique information into seperate buckets thus compacting the data.

   However, when making the data smaller that often causes collision to occur.  To avoid this we use linked list as opposed to arrays to store our hash table values. That way when a collision occurs (two values end up having the same hashtable key) a new node is formed on the linked list to save that additional value as opposed to over writing the array.