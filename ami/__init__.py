import zlib


encode = lambda x: zlib.compress(x.encode('ascii', 'ignore'))


def ami(x: str, y: str) -> float:
        """
        Returns the normalized approximate mutual information between
        strings x and y.
        """

        lx = len(encode(x))
        ly = len(encode(y))
        lyx = len(encode(y + x))
        lx_y = min(lx, max(0, lyx - ly)) # 0 <= L(x|y) <= L(x)
        ixy = lx - lx_y

        return ixy / lx


def ami2(x: str, y: str) -> float:
        """
        Returns the normalized approximate mutual information between
        strings x and y.
        """

        lx = len(encode(x))
        ly = len(encode(y))
        lxy = min(len(encode(x + y)), len(encode(y + x)))
        lxy = min(lx + ly, max(0, lxy))

        return ((lx + ly) - lxy) / (lx + ly) * 2


def match(x: str, y: str, context: str) -> bool:
        """
        Returns which string, x or y, best matches the given context
        string. Can be used as a simple basic classifier.
        """
        
        ami_x = ami2(x, context)
        ami_y = ami2(y, context)
        
        return ami_x < ami_y
