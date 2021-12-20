from services.const import COMMENT_HEADER, MODULE_HEADER, RULE_HEADER, POOL_HEADER
from services.filter import NinjaModuleFilter
from services.parser import NinjaFileParser

with open("build.ninja", encoding="utf-8") as fin, \
     open("new-build.ninja", "w") as fout:

    done = False
    line = fin.readline()
    while True:
        if len(line) == 0:
            break
        elif len(line) == 1:
            pass
        elif line.startswith(COMMENT_HEADER):
            content, line = NinjaFileParser.HeaderComment(line, fin)
            fout.writelines(content)
            continue

        elif line.startswith(MODULE_HEADER):
            content, line = NinjaFileParser.Module(line, fin)
            if NinjaModuleFilter.Defined(content, "frameworks/"):
                fout.writelines(content)
            continue

        elif line.startswith(RULE_HEADER):
            content, line = NinjaFileParser.Rule(line, fin)
            fout.writelines(content)
            continue

        else:
            fout.write(line)

        line = fin.readline()