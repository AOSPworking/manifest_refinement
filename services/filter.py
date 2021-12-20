
from typing import List


class NinjaModuleFilter:
    @classmethod
    def Defined(cls, content: List[str], path_prefix="frameworks/") -> bool:
        multi_line_defined = False
        for line in content:
            # 如果这个 define 是多行定义的，同时也以前缀开头，
            # 那么就应该 return True
            if multi_line_defined and line.startswith(f"# {path_prefix}"):
                return True

            # 在检查多行之后，再判断是否是以 Defined 开头的单行
            if not line.startswith("# Defined:"):
                continue

            if line.startswith(f"# Defined: {path_prefix}"):
                return True
            elif line.startswith("# Defined:\n"):
                multi_line_defined = True
        return False