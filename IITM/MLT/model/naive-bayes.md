## Naive Bayes
#### Intro
- Naive Bayes is a classification algorithm for binary and multi-class classification problems.
- Naive Bayes is a supervised machine learning algorithm to predict the probability of different classes based on numerous attributes.
- We will be using Bayes theorem to find probability of a class if data is given
  -  $P(class|data)= {\frac{P(data|class) * P(class)}{P(data)}}$
 #### The Naive Bayes classifier is based on two essential assumptions:-
 - (i) Conditional Independence - All features are independent of each other. This implies that one feature does not affect the performance of the other. This is the sole reason behind the ‘Naive’ in ‘Naive Bayes.’ 
 - (ii) Feature Importance - All features are equally important. It is essential to know all the features to make good predictions and get the most accurate results. 
#### Theory of Naive Bayes classifier
- we know Bayes theorem
  $P(class|data)= {\frac{P(data|class) * P(class)}{P(data)}}$
- $P(class A | X ) ={\frac {P(X | class A ) * P(class A)}{P(X)}}$ <br>
or $P(y=class A | X= x_1,x_2,...,x_m ) ={\frac {P( X= x_1,x_2,...,x_m  | y=class A ) * P(y=class A)}{P(X= x_1,x_2,...,x_m )}}$ <br>
Now using naive assumption <br>
 $P(class A | X= x_1,x_2,...,x_m ) ={\frac { P( x_1 | class A )*  P( x_2 | class A )....* P( x_m | class A ) * P(class A)}{P(x_1)*P(x_2)...*P(x_m)}}$
 - simillarly calculate **probability of a class condition that given data** corresponding to all classes
 - pick class corresponding to maximum probability
#### Types of Naive Bayes
Based on what distribution the features of data follow, Naive Bayes is classified into three main types: 
- Multinomial Naive Bayes
- Bernoulli Naive Bayes : when features value follow Bernoulli distribution
- Gaussian Bayes : when features value follow Gaussian distribution

## Bernoulli Naive Bayes
Let us consider the example below to understand Bernoulli  Naive Bayes
##### Question - Classify an instance ‘X’ where Adult=’Yes’, Gender= ‘Male’, and Fever=’Yes’ based on below information
| Adult | Gender | Fever | Disease |
|-------|--------|-------|---------|
| Yes   | Female | No    | False   |
| Yes   | Female | Yes   | True    |
| No    | Male   | Yes   | False   |
| No    | Male   | No    | True    |
| Yes   | Male   | Yes   | True    |

Here
- Here, ‘Disease’ is the target, and the rest are the features.
- we are trying to predict whether a person has a disease or not based on their age, gender, and fever.
- All values are binary.
. 
##### Solution
x=(adult=yes,gender=male,fever=yes)
## $P(y=y_c| x )= {\frac{P(x|y=y_c) * P(y=y_c)}{P(x)}}$ <br> <br>
## $P(y=y_c| x )= {\frac{P(Adult=yes,Gender=male,Fever=yes|y=y_c) * P(y=y_c)}{P(Adult=yes,Gender=male,Fever=yes)}}$ <br><br>
## $P(y=y_c| x )= {\frac{P(Adult=yes|y=y_c) * P(Gender=male|Y=y_c) * P(Fever=yes|y=y_c) * P(y=y_c)}{P(Adult=yes) * P(Gender=male) * P(Fever=yes)}}$
  

- Firstly, we calculate the class probability (aka prior), probability of disease or not. 
  - P(Disease = True) = ⅗
  - P(Disease = False) = ⅖ 
  
- Secondly, we calculate the individual probabilities for each feature. 
  - P(Adult= Yes | Disease = True) = ⅔
  - P(Gender= Male | Disease = True) = ⅔
  - P(Fever= Yes | Disease = True) = ⅔
  - P(Adult= Yes | Disease = False) = ½
  - P(Gender= Male | Disease = False) = ½
  - P(Fever = Yes | Disease = False) = ½
  
- Now, we calculate estimator probability (aka Evidence)
   - P(X) = P(Adult= Yes,Gender = Male ,Fever = Yes)= P(Adult= Yes) * P(Gender = Male ) * P(Fever = Yes) = ⅗ * ⅗ * ⅗ = 27/125 = 0.21

- Now, we need to find out two probabilities
  - (i) P(Disease= True | X) = (P(X | Disease= True) * P(Disease=True))/ P(X) 
    -  P(Disease = True | X) = (( ⅔ *⅔ * ⅔ ) * (⅗))/0.21 = (8/27 * ⅗) / 0.21  = 0.17/0.21=0.80 
  - (ii) P( Disease = False | X) = (P(X | Disease = False) * P(Disease= False) )/P(X)
    - P(Disease = False | X) = [(½ * ½ * ½ ) * (⅖)] / 0.21  = [⅛ * ⅖] / 0.21  = 0.05/ 0.21 = 0.23



Now, we notice that (1) > (2), the result of instance ‘X’ is ‘True’, i.e., the person has the disease.
