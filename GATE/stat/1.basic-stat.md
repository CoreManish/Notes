## Expectation $\mu ~ or ~ E[X]$ 

$$ E[X] = \sum x * P(X=x)$$
$$ E[X] = \int x * f(x)$$

*Note* 
1. In simple variable case, probability of each discrete value is equal, means P(X=x) = $\frac{1}{n}$. So expression becomes  

$$ \sum x * P(X=x) = \sum x * \frac{1}{n} = \frac{1}{n} * \sum x $$

2. Called mean or average $\bar{X}$

### Properties of expected value
* $E[X+k] = E[X] + k$

* $E[k_1X_1 + k_2X_2] = k_1 E[X_1] + k_2 E[X_2]$

---

## Variance $Var(X) ~ or ~ \sigma ^2 $
 $$ Var(X) = \sum (x-\mu)^2 * P(X=x) $$
 $$ Var(X) = \int (x-\mu)^2 * f(x) $$

*Note* 
1. In simple variable case, probability of each discrete value is equal, means P(X=x) = $\frac{1}{n}$. So expression becomes  

$$ \sum (x-\bar{X})^2 * P(X=x) =  \sum (x-\bar{X})^2 * \frac{1}{n} =  \frac{1}{n} * \sum (x-\bar{X})^2 $$

2. Variance formula in terms of expectation,

$$ \sum (x-\mu)^2 * P(X=x) = E[(X-\mu)^2] $$

3. Expanding expression $E[(X-\mu)^2]$

$$  E[(X-\mu)^2] = E[X^2 - 2 * X * \mu  + \mu^2] = E[X^2] - 2*\mu*E[X] + \mu^2  = E[X^2] - \mu^2 $$

### Properties of Variance

* $Var(X+k) = Var(X)$

* $Var(k_1X_1 + k_2 X_2) = {k_1}^2 Var(X_1) + {k_2}^2 Var(X_2)$

---

## Covariance cov(X,Y)
$$ Cov(X,Y) =  \sum (x-\mu_x)(y-\mu_x)*P(xy~pair)$$

*Note*
1. In simple variable case, probability of each xy pair value is equal. So expression becomes   

$$ \frac{1}{n}\sum (x-\mu_x)(y-\mu_x)$$

2. Covariance formula in terms of expectation, 

$$ \sum (x-\mu_x)(y-\mu_x)*P(xy~pair) = E[(X-\mu_x)(Y-\mu_y)] $$


3. Expanding expression $E[(X-\mu_x)(Y-\mu_y)]$

$$ = E[XY - X*\mu_y - \mu_x*Y + \mu_x \mu_y] = E[XY] - \mu_x \mu_y $$

### Properties of covariance
* If two random variable X and Y are independent,
$$Cov(X,Y) = E[XY] -  \mu_x \mu_y = E[X] E[Y] -  \mu_x \mu_y =  \mu_x \mu_y -  \mu_x \mu_y = 0 $$
