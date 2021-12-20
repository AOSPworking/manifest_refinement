"""
这个脚本用来测试当前目录下的 build.ninja 和 new-build.ninja 到底是不是相同的。
"""

"""
with open("build.ninja", encoding="utf-8") as fin_origin, \
     open("origin.module.list", "w") as fout_origin:
    while True:
        line = fin_origin.readline()
        if len(line) == 0:
            break
        if line.startswith("# Defined: frameworks"):
            fout_origin.write(line)
        elif line.startswith("# frameworks"):
            fout_origin.write(f"# Defined:{line[1:]}")
"""

with open("new-build.ninja") as fin_origin, \
     open("new.module.list", "w") as fout_origin:
    while True:
        line = fin_origin.readline()
        if len(line) == 0:
            break
        if line.startswith("# Defined: frameworks"):
            fout_origin.write(line)
        elif line.startswith("# frameworks"):
            fout_origin.write(f"# Defined:{line[1:]}")