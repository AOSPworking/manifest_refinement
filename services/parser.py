from copy import deepcopy
from io import TextIOWrapper
from typing import List, Tuple
from services.const import MODULE_HEADER

class NinjaFileParser:
    """
    其实根本不是 Parser。思路就是在外层根据标识确定好是哪个部件，然后开始读。
    读完之后把新读的一行返回掉，又作为外层的 line。
    """

    @classmethod
    def HeaderComment(cls, first_line: str, f: TextIOWrapper) -> Tuple[List[str], str]:
        """ 返回的是所有的 header comment 和它的下一行（用于替换外层的 line） """
        res: List[str] = []
        line: str = deepcopy(first_line)
        while True:
            res.append(line)
            line = f.readline()
            if not line.startswith("#") or len(line) == 0:
                # 如果最开始不以 # 开头了，那说明头部注释已经解析完了
                res.append("\n")
                return res, line

    @classmethod
    def Module(cls, first_line, f: TextIOWrapper) -> Tuple[List[str], str]:
        res: List[str] = []
        line: str = deepcopy(first_line)
        while True:
            res.append(line)
            line = f.readline()
            if line.startswith(MODULE_HEADER) or len(line) == 0:
                # len(line) == 0 是为了顾及 build module 后没有其他的 module
                # 如果看到了下个 MODULE_HEADER，那说明这个 module 结束了
                return res, line

    @classmethod
    def Rule(cls, first_line, f: TextIOWrapper) -> Tuple[List[str], str]:
        res: List[str] = []
        line: str = deepcopy(first_line)
        while True:
            res.append(line)
            line = f.readline()
            if line.startswith("\n") or len(line) == 0:
                # Rule 如果遇到了 \n，那说明 Rule 结束了
                res.append("\n")
                return res, line