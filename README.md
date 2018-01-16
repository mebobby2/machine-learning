# MachineLearningBook

## How to run code (example)
1. Navigate to directory, eg cd path/recommendations
2. python
3. from mockdelicious import *
4. get_popular('devops')
5. exit() or CTR-D
6. To run a python script: python script.py
7. To install a packege: python -m pip install feedparser

## Run a class
1. Repeat steps 1 and 2 from above
2. import searchengine
3. crawler=searchengine.crawler('db_name')
4. crawler.crawl(pagelist)

## Installing Packages

### Use pip to install packages you need.

```which python``` on my machine gives ```/usr/local/bin/python```.
/usr/bin/python is the executable for the python that comes with OS X. /usr/local/lib is a location for user-installed programs only, possibly from Python.org or Homebrew.

When you use ```pip install package_name``` you are installing it for the /usr/bin/python version (since the default system pip is probably the one specified in your $PATH), so when you run your python script and it loads a package, you will get a load error. Since your default python is now set to ```/usr/local/bin/python```.

In order to make sure you use the pip associated with a particular python, you can run ```python -m pip install package_name```, or go look at what the pip on your path is, or is symlinked to. This will install the package into ```usr/local/lib/python2.7/site-packages``` which is then picked up by ```/usr/local/bin/python```.

### pip on new machines
stick with the default python installation at ```/usr/bin/python```. Do not install another version of python. Install pip by downloading ```wget https://bootstrap.pypa.io/get-pip.py``` and running it with ```sudo python get-pip.py```. When you install a package using pip, use the command ```sudo pip install bs4```. As long as you don't install another verison of python and use the default one that comes with the OS, you don't need any of that funky stuff in the above section.

### pysqlite

As of python version 2.5 and up, a working version of pysqlite 2, bundled as sqlite3, is available from within the language. So you don't need to install it as an external package.

## Notes

### Euclidean vs Pearson

If you are dealing with data where the actual difference in values of attributes is important, go with Euclidean Distance. If you are looking for trend or shape similarity, then go with correlation

In the blogs exercise, some blogs contain more entries or much longer entries than others, and will thus contain more words overall. The Pearson correlation will correct for this, since it really tries to determine how well two sets of data fit onto a straight line.

### Tanimoto coefficient
The Pearson correlation works well for the blog dataset where the values are actual word counts. However, this dataset just has 1s and 0s for presence or absence, and it would be more useful to define some measure of overlap between the people who want two items. For this, there is a measure called the Tanimoto coefficient, which is the ratio of the intersection set (only the items that are in both sets) to the union set (all the items in either set).

```
def tanamoto(v1,v2):
  c1,c2,shr=0,0,0
  for i in range(len(v1)):
    if v1[i]!=0: c1+=1 # in v1
    if v2[i]!=0: c2+=1 # in v2
    if v1[i]!=0 and v2[i]!=0: shr+=1 # in both
  return 1.0-(float(shr)/(c1+c2-shr))
```

This will return a value between 1.0 and 0.0. A value of 1.0 indicates that nobody who wants the first item wants the second one, and 0.0 means that exactly the same set of people want the two items.

### User based or item based filtering

Item-based filtering is significantly faster than user-based when getting a list of recommendations for a large dataset, but it does have the additional overhead of main- taining the item similarity table. Also, there is a difference in accuracy that depends on how “sparse” the dataset is. In the movie example, since every critic has rated nearly every movie, the dataset is dense (not sparse). On the other hand, it would be unlikely to find two people with the same set of del.icio.us bookmarks—most book- marks are saved by a small group of people, leading to a sparse dataset. Item-based filtering usually outperforms user-based filtering in sparse datasets, and the two per- form about equally in dense datasets.

### Supervised vs Unsupervised Learning

Techniques that use example inputs and outputs to learn how to make predictions are known as supervised learning methods. Examples of supervised learning methods include neural networks, decision trees, support-vector machines, and Bayesian filtering.

Clustering is an example of unsupervised learning. Unlike a neural network or a decision tree, unsupervised learning algorithms are not trained with examples of correct answers. Their purpose is to find structure within a set of data where no one piece of data is the answer. In the fashion example where fashion islands are generated from user purchasing data for a retail shop, the clusters don’t tell the retailers what an individual is likely to buy, nor do they make predictions about which fashion island a new person fits into. The goal of clustering algorithms is to take the data and find the distinct groups that exist within it.

### Hierarchical clustering

Hierarchical clustering builds up a hierarchy of groups by continuously merging the two most similar groups. Each of these groups starts as a single item. In each iteration this method calculates the distances between every pair of groups, and the closest ones are merged together to form a new group. This is repeated until there is only one group.

A dendrogram is a visualization of hierarchical clustering.

Some insights derivied from heirarchical clustering: It closely clustered these blogs together: Official google blog, search engine roundtable, google operating system, google blogoscoped.

### Column clustering
It’s often necessary to cluster on both the rows and the columns. In a marketing study, it can be interesting to group people to find demographics and products, or perhaps to determine shelf locations of items that are commonly bought together. In the blog dataset, the columns represent words, and it’s potentially interesting to see which words are commonly used together.

One important thing to realize about clustering is that if you have many more items than variables, the likelihood of nonsensical clusters increases. There are many more words than there are blogs, so you’ll notice more reasonable patterns in the blog clustering than in the word clustering.

Some insights derivied from column clustering: these words formed a cluster, meaning, they were mentioned the same number of times across all blogs.
1. iraq, war
2. president, bush
3. national, government, against
4. 1, 2, and 3 all formed a larger cluster

### K-Means Clustering

Hierarchical clustering gives a nice tree as a result, but it has a couple of disadvan- tages. The tree view doesn’t really break the data into distinct groups without additional work, and the algorithm is extremely computationally intensive. Because the relationship between every pair of items must be calculated and then recalculated when items are merged, the algorithm will run slowly on very large datasets.

An alternative method of clustering is K-means clustering. This type of algorithm is quite different from hierarchical clustering because it is told in advance how many distinct clusters to generate. The algorithm will determine the size of the clusters based on the structure of the data.

Some insights derived from k-means:
The blogs were all found to be in one cluster:
'Publishing 2.0', 'GigaOM', "John Battelle's Searchblog", 'Google Operating System', 'Valleywag', 'Search Engine Watch Blog', 'Techdirt', 'Official Google Blog', 'Search Engine Roundtable', 'PaulStamatiou.com', 'A Consuming Experience (full feed)', 'Matt Cutts: Gadgets, Google, and SEO', 'Google Blogoscoped', 'Read/WriteWeb'

### Multidimensional Scaling
Used to find a two-dimensional representation of the dataset. Since most real-life examples of items you would want to cluster have more than two numbers, you can’t just take the data as-is and plot it in two dimensions. However, to understand the relationship between the various items, it would be very useful to see them charted on a page with closer distances indicating similarity.

The concept of imagining items in space depending on their parameters will be a recurring theme in this book. Using multidimensional scaling is an effective way to take a dataset and actually view it in a way that’s easy to interpret. It’s important to realize that some information is lost in the process of scaling, but the result should help you understand the algorithms better.

### Content-Based Ranking for search results
A score for a search item result is calculated based on 3 metrics:
Word frequency - The number of times the words in the query appear in the document can help determine how relevant the document is.
Document location - The main subject of a document will probably appear near the beginning of the document.
Word distance - If there are multiple words in the query, they should appear close together in the document.

### Inbound Links to rank search results
Content-Based Ranking metrics have all been based on the content of the page. Although many search engines still work this way, the results can often be improved by considering information that others have provided about the page, specifically, who has linked to the page and what they have said about it. This is particularly useful when indexing pages of dubious value or pages that might have been created by spammers, as these are less likely to be linked than pages with real content.

### Stochastic Optimization
Optimization techniques are typically used in problems that have many possible solutions across many variables, and that have outcomes that can change greatly depending on the combinations of these variables.

Optimization finds the best solution to a problem by trying many different solutions and scoring them to determine their quality. Optimization is typically used in cases where there are too many possible solutions to try them all.

The cost function is the key to solving any problem using optimization, and it’s usu- ally the most difficult thing to determine.

Whether a particular optimization method will work depends very much on the problem. Simulated annealing, genetic optimization, and most other optimization methods rely on the fact that, in most problems, the best solution is close to other good solutions.

A useful rule when creating a cost function is, if possible, to make the perfect solu- tion (which in this example is everyone being assigned to their top choice) have a cost of zero. In this case, you’ve already determined that the perfect solution is impossible, but knowing that its cost is zero gives you an idea of how close you are to it. The other advantage of this rule is that you can tell an optimization algorithm to stop searching for better solutions if it ever finds a perfect solution.

### Features
A feature is anything that you can determine as being either present or absent in the item. When considering documents for classification, the items are the docu- ments and the features are the words in the document. When using words as fea- tures, the assumption is that some words are more likely to appear in spam than in nonspam, which is the basic premise underlying most spam filters. Features don’t have to be individual words, however; they can be word pairs or phrases or anything else that can be classified as absent or present in a particular document.

The other thing to consider when deciding on features is how well they will divide the set of documents into the target categories. For example, the code for getwords above reduces the total number of features by converting them to lowercase. This means it will recognize that a capitalized word at the start of a sentence is the same as when that word is all lowercase in the middle of a sentence—a good thing, since words with different capitalization usually have the same meaning. However, this function will completely miss the SHOUTING style used in many spam messages, which may be vital for dividing the set into spam and nonspam. Another alternative might be to have a feature that is deemed present if more than half the words are uppercase.

### Assumed Probability
Used when you have very little information about the feature in question. An assumed probability of 0.5 is a safe number simply because it is halfway between 0 and 1. However, it’s possible that you might have better background information than that, even on a completely untrained classifier. For example, one person who begins training a spam filter can use probabilities from other people’s already-trained spam filters as the assumed probabilities. The user still gets a spam filter personalized for him, but the filter is better able to handle words that it has come across very infrequently.

### naïve Bayesian classifier
Is called naïve because it assumes that the probabilities being combined are independent of each other. That is, the probability of one word in the document being in a specific category is unrelated to the probability of the other words being in that category. This is actually a false assumption, since you’ll probably find that documents containing the word “casino” are much more likely to contain the word “money” than documents about Python programming are.

### Neural Networks over Bayesian classifiers
Neural networks and support-vector machines have one big advantage over the Bqyesian classifiers: they can capture more complex relationships between the input features. In a Bayesian classifier, every feature has a probability for each category, and you combine the probabilities to get an overall likelihood. In a neural network, the probability of a feature can change depending on the presence or absence of other features. It may be that you’re trying to block online-casino spam but you’re also interested in horse betting, in which case the word “casino” is bad unless the word “horse” is somewhere else in the email message. Naïve Bayesian classifiers cannot capture this interdependence, and neural networks can.

### Gini Impurity
First, a definition: Gini impurity is a measure of how often a randomly chosen element from the set would be incorrectly labeled if it were randomly labeled according to the distribution of labels in the subset. The higher this probability, the worse the split. A probability of zero is great because it tells you that everything is already in the right set.

#### Question:
Say you have 3 classes of balls: red, green blue. The odds of any colored ball appearing are red = 4/10, blue = 3/10, green = 3/10. Misclassifying red is calculated as 4/10*(3/10 + 3/10) or the odds of picking "True Class" * "Wrong Class".

Why do you multiply, instead of say add, to find the odds of picking the wrong red ball?

#### Answer:
The probability that a ball is red is 0.4. You can only make a mistake about a red ball if the ball is, in fact, red.

Assuming that the guess is based precisely on the probability distribution of the balls, then a guess of blue has probability 0.3 and equally a guess of green has probability 0.3. If the ball really is red, these are the incorrect guesses, since the only other possible guess is correct.

If two events are independent, the probability that both of them occur (P and Q) is the product of their probabilities. If two events are mutually exclusive, then the probability that one of them occurs (P or Q) is the sum of their probabilities.

So the probability that a ball is red and is misclassified (as blue or green) is 0.4 * (0.3 + 0.3).

To that, we'd have to add the probability of a blue ball being misclassified as red or green (0.3 * (0.4 + 0.3)) and the probability of a green ball being misclassified as blue or red (0.3 * (0.3 + 0.4)) for a total of 0.66. That's extremely close to the maximum value of 2/3 (when all the probabilities are equal).



### Maths
#### Number of combinations
Let's say I have six values, A, B, C, D, E, F. And TWO of these values make a valid tuple. How many times/loops do I need to make to find the valid tuple. The formula is I^P, where P = number of possibilities and I = the number of inputs. Hence, 6^2 = 36 loops/combinations we need to look through.


## Source code for book
https://github.com/arthur-e/Programming-Collective-Intelligence

## Upto

Upto page 171

Entropy
