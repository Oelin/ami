# Approximate Mutual Information (AMI)

A compression-based measure mutual information between strings. 


## Theory

### Data Compression

There is a close relationship between the entropy of a string and the extent to which it can be losslessly compressed. Namely, according to Shannon's source-coding theorem, there exists no lossless code able to compress a string beyond its entropy. Compression schemes hence allow us to obtain an upper bound on the entropy of a string.

### Mutual Information

The mutual information between two random variables, denoted $I(X\ ;\ Y)$, measures how much information $X$ provides about $Y$ and visa-versa. It is a symmetric measure given by

$$I(X\ ;\ Y) = H(X) - H(X|Y) = I(Y\ ;\ X) = H(Y) - H(Y|X)$$

where $H(\cdot)$ is the entropy.

It tells us how much our uncertainty in $X$ is reduced after observing $Y$ and visa-versa. Now, since lossless compression gives an upper-bound on the entropy of string, we can also use it to approximate the mutual information between two strings. Let $L_C(x)$ denote the length of string $x$ when losslessly encoded using $C(\cdot)$; and let $L_C(x|y)$ denote the length of string $x$ when encoded *after observing* $y$. Note that while $H(X|Y) \le H(X)$, the inequality $L_C(x|y) \le L_C(x)$ may not always hold. As such, we retroactively limit the length of $L_C(x|y)$ to $L_C(x)$.

To compute $L_C(x|y)$ we use the fact that $H(X|Y) = H(Y, X) - H(Y)$, obtaining the approximation $L_C(x|y) = L_C(y||x) - L_C(y)$, where $||$ denotes string concatenation. Hence, the mutual information between $x$ and $y$ can be approximated as

$$I(x\ ;\ y) \approx  L_C(x) - L_C(x|y) \approx L_C(x) - L_C(y||x) + L_C(y)$$

Note that we may choose to use different codes for encoding $x$ and $x|y$. If a specialised conditional code for $x|y$ can be used, this is preferrable to the approximation $L_C(y||x) - L_C(y)$. Hence, the more general form of the equation is

$$I(x\ ;\ y) \approx L_x(x) - L_{x|y}(x|y)$$

in which separate codes are used.


## Implementation

Here's an example of ami implemented in Python, using zlib as the encoder.

```py
import zlib


def ami(x: str, y: str) -> float:
        """
        Returns the normalized approximate mutual information between 
        strings x and y.
        """

        lx = len(zlib.compress(x))
        ly = len(zlib.compress(y))
        lyx = len(zlib.compress(y + x))
        lx_y = min(lx, max(0, lyx - ly)) # 0 <= L(x|y) <= L(x)
        ixy = lx - lx_y
        
        return ixy / lx
```


## Uses

AMI generally measures the amount of information shared between strings. If we sample from two independent random variables, the respective samples should share approximately share no information, and their normalized AMI score will be very close to zero. In contrast, two identical strings should have a score close to 1, indicating that they're highly correlated. Scores in between 0 and 1 therefore indicate the degree of correlation between strings. 

Unlike some other measures, this correlation need not be linear, or even numerical in nature. In fact, any statistical correlation can be modelled simply by changing the compression scheme. Zlib's standard encoder is a reasonable choice due to its efficiency and ability to significantly compress a broad range of file types. However, a priori knowledge about the strings in question can be used to inform the choice of encoder.

One use of AMI is in performing document classification. For example, the distribution of French language strings is sufficiently different from the distribution of Spanish language strings that even a simple encoder such as Zlib can accurately to distinguish between them. For distributions which are closer, a more specific encoder may be required. 

To perform classification, we use AMI to measure the KL divergence between two strings. Mutual information and KL divergence are related through the following identity:

$$D_{\text{KL}}(x\ ||\ y) = H(x, y) - H(y) \approx L_{x||y}(x||y) - L_y(y)$$

