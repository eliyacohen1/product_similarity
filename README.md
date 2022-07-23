# Products Matching
### Explanations of the code that found in the notebook
As I mentioned in the notebook, there are 3 issues that need to be considered:
1. Choosing the 50 most important chars
2. Calculate the similarity score
3. Choosing the threshold score

Note: I found that part of the text was written in a language other than English (for example German) and I decided to
 convert all languages other than English to English by the package googletrans.
 
Solutions to the issues mentioned above:
1. Use tf-idf for finding the most important chars
    * TF-IDF is a good algorithm that find the most important word if each product title / description
    * In my work I preferred to only refer to the title and not the other fields.
        * If the title length is less that K (50) I concat the title with the description
        
2. Create vector embedding by SentenceBert and calculate the cosine similarity between products
    * One of my thoughts is using bert cls token for the embedding but i found that bert cls is good for downstream task
      But sometimes it doesnt work well in creating a vector embedding for sentence, and so I chose to use SentenceBert
      
3. The explanation for this point inside the notebook
    * In addition this solution we choose is depend on what our customer want
        * precision preferred on recall -> Higher threshold
        * recall preferred on precision -> Lower threshold
    * I think its more important do not just return results that are not good for us (precision preferred)
           

### Future Things
1. combine more field, for example:
    * Use categories - The categories are like words with high certainty that should be in the results that will be returned
        * The problem with the categories is that they can be words that appear in many
         products and this can confuse our query search
        * Therefore we will only want to use categories on repeated results

2. Make a moving window to solve the problem of limiting search

3. To label some of the data in order to better understand the threshold

4. Get more details from the alibaba website

5. Add more metrics for finding the best matching products results 


#### Resourses
* https://arxiv.org/pdf/1908.10084.pdf
* https://towardsdatascience.com/two-most-common-similarity-metrics-39c37f3fe14d#9aca
