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


def ami2(x: str, y: str) -> float:
        """
        Returns the normalized approximate mutual information between
        strings x and y.
        """

        lx = len(zlib.compress(x))
        ly = len(zlib.compress(y))
        lxy = min(len(zlib.compress(x + y)), len(zlib.compress(y + x)))
        lxy = min(lx + ly, max(0, lxy))

        return ((lx + ly) - lxy) / (lx + ly) * 2
