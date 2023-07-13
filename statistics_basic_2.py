QUESTION:-1. What are the three measures of central tendency?
(i) Mean
(ii) Median
(iii) Mode 

(i) Mean:- The sum of all values divided by the total number of values. 
(ii) Median:- The middle number in an ordered dataset.
(iii) Mode:- The most frequent value.



QUESTION:-2. What is the difference between the mean, median, and mode? How are they used to measure the central tendency of a dataset?
The mean is the average where the sum of all the numbers is divided by the total number of numbers, whereas the median is the middle value in the list of given nubers numerically ordered from smallest to bigger and mode is the value of the number which occurs most often in the list.
The central tendency can be found using the formulas of mean, median or mode in most of the cases.



QUESTION:-3. Measure the three measures of central tendency for the given height data: 
[178, 177, 176, 177, 178.2, 178, 175, 179, 180, 175, 178.9, 176.2, 177, 172.5, 178, 176.5]

Mean :- 
height = [178, 177, 176, 177, 178.2, 178, 175, 179, 180, 175, 178.9, 176.2, 177, 172.5, 178, 176.5]
import numpy as np 
np.mean(height)

Median :- 
height = [178, 177, 176, 177, 178.2, 178, 175, 179, 180, 175, 178.9, 176.2, 177, 172.5, 178, 176.5]
import numpy as np 
np.median(height)

Mode :- 
height = [178, 177, 176, 177, 178.2, 178, 175, 179, 180, 175, 178.9, 176.2, 177, 172.5, 178, 176.5]
from scipy import stats 
stats.mode(height)



QUESTION:-4. Find the standard deviation for the given data:
[178, 177, 176, 177, 178.2, 178, 175, 179, 180, 175, 178.9, 176.2, 177, 172.5, 178, 176.5] 

Standard deviation :- 
height = [178, 177, 176, 177, 178.2, 178, 175, 179, 180, 175, 178.9, 176.2, 177, 172.5, 178, 176.5]
import numpy as np 
np.std(height)



QUESTION:-5. How are measures of dispersion such as range, variance, and standard deviation used to describe the spread of a dataset? Provide an example.

Range :- It is defined as the difference between the largest and the smallest value in the distribution.
Example :- 
import numpy 
values = [13,21,21,40,48,55,72]
x = numpy.ptp(values)
print(x)

Variance :- The term variance refers to a statistical measurement of the spread between numbers in a data set.
Example :-
ages_1st = [23,43,23,56,74,32,68,98,45,32]
import numpy as np 
np.var(ages_1st)

Standard Deviation :- This is the square root of the arithmetic average of the square of the deviations measured from the mean.
Example :- 
ages_1st = [23,43,23,56,74,32,68,98,45,32]
import numpy as np 
np.std(ages_1st)



QUESTION:-6. What is a venn diagram?
A Venn diagram is an illustration that uses circles to show the relationships among things or finite groups of things. Circles that overlap have a commonality while circles that do not overlap do not share those traits.
Venn diagrams help to visually represent the similarities and differences between two concepts.



QUESTION:-7. For the two given sets A = (2,3,4,5,6,7) & B = (0,2,6,8,10). find: 
(i) A ∩ B
(ii) A ∪ B
(i) A ∩ B :- (2,6)
(ii) A ∪ B :- (0,2,3,4,5,6,7,8,10)



QUESTION:-8. What do you understand about skewness in data?
Skewness is a measurement of the distortion of symmetrical distribution or asymmetry in a data set.



QUESTION:-9. If a data is right skewed then what will be the position of median with respect to mean?
If the distribution of data is skewed to the right, the mode is often less than the median, which is less than the mean.



QUESTION:-10. Explain the difference between covariance and correlation. How are these measures used in statistical analysis? 
Covariance :- Covariance signifies the direction of the linear relationship between the two variables. By direction we mean if the variables are directly proportional or inversely proportional to each other.

Correlation :- Correlation analysis is a method of statistical evaluation used to study the strength of a relationship between two, numerically measured, continuous variables.
Statistics measures are a descriptive analysis technique used to summarise the characteristics of a data set.



QUESTION:-11. What is the formula for calculating the simple mean? Provide an example calculation for a dataset.

The sample mean formula is:
x̄ = ( Σ xi ) / n
Where,
∑xi = sum of terms
n = number of terms

Example :- 
ages_1st = [12,21,23,24,32,21,33,26,32,31,29,28,44,30,22]
import numpy as np 
np.mean(ages_1st)



QUESTION:-12. For a normal distribution data what is the relationship between its measure of central tendency?
For normally distributed data, all three measures of central tendency will give you the same answer so they can all be used.



QUESTION:-13. How is covariance different from correlation? 
Covariance indicates the direction of the linear relationship between variables. Correlation measures both the strength and direction of the linear relationship between two variables.



QUESTION:-14. How do outliers affect measures of central tendency and dispersion? Provide an example.
Outliers affect the mean value of the data but have little effect on the median or mode of a given set of data.
Example :- 
age = [12,21,23,45,65,43,56,45,32,67,54,34,200]
import numpy as np 
np.mean(age)
np.median(age)
 