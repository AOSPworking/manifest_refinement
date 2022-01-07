
from typing import List


class NinjaModuleFilter:
    @classmethod
    def Defined(cls, content: List[str],
                path_prefix="frameworks/", path_suffix="Android.bp") -> bool:
        multi_line_defined = False
        for line in content:
            # 如果这个 define 是多行定义的，同时也以前缀开头，
            # 那么就应该 return True
            if multi_line_defined and line.startswith(f"# {path_prefix}"):
                parts = line.split(":")
                path = parts[0]
                if path.startswith(f"# {path_prefix}") and path.endswith(path_suffix):
                    return True

            # 在检查多行之后，再判断是否是以 Defined 开头的单行
            if not line.startswith("# Defined:"):
                continue

            # 如果以 "# Defined:\n" 开头 / 结尾，说明要开启一个多行
            if line.startswith("# Defined:\n"):
                multi_line_defined = True
                continue

            parts = [part.strip() for part in line.split(":")]
            defined = parts[0]
            path = parts[1]
            #print(defined, path, path.startswith(path_prefix), path.endswith(path_suffix))
            if defined == "# Defined" \
                and path.startswith(path_prefix) \
                and path.endswith(path_suffix):
                return True
        return False