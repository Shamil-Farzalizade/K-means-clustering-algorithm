# K-means-clustering-algorithm
Improved version of K-means clustering algorithm. AI Research project. From Theory to practice
https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=5b4d09f41f8fa28c8f4ac3e7b8a474ae9f84b197
Enhanced version from the paper
Require: D = {d1, d2, d3,..., di,..., dn } // Set of  n data  
                         points. 
               di = { x1, x2, x3,..., xi,..., xm } // Set of attributes  
                        of one data point. 
               k // Number of desired clusters. 
Ensure: A set of k clusters. 
Steps: 
1:  In the given data set D, if the data points contains the both   
     positive  and   negative   attribute   values then go to step 2,  
     otherwise go to step 4. 
2:  Find the minimum attribute value in the given data set D. 
3:  For each data point attribute,  subtract  with  the minimum  
     attribute value. 
4:  For each data point calculate the distance from origin. 
5:  Sort  the  distances  obtained in step 4.  Sort the data points  
     accordance with the distances. 
6:  Partition the sorted data points into k equal sets. 
7:  In each set, take the middle point as the initial centroid. 
8:  Compute  the  distance  between  each data point di  (1 <= i  
    <= n) to all the initial centroids cj (1 <= j <= k). 
9:  Repeat 
10:  For each data point di, find the closest centroid cj and ass- 
       ign di to cluster j. 
11: Set ClusterId[i]=j.  // j:Id of the closest cluster. 
12: Set NearestDist[i]= d(di, cj). 
13: For each cluster j (1 <= j <= k), recalculate the centroids. 
14: For each data point di, 
      14.1 Compute its distance from the centroid of the present  
              nearest cluster. 
      14.2 If this distance is less than or equal to the present ne- 
           arest distance, the data point stays in the same 
 cluster. 
               Else 
               14.2.1 For every centroid c
