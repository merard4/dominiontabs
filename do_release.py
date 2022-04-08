import os
import zipfile

import domdiv
import domdiv.main
from setuptools_scm import get_version

if not os.path.exists("generated"):
    os.makedirs("generated")

version = ".".join(
    get_version(root=".", relative_to=__file__, version_scheme="post-release").split(
        "."
    )[:3]
)

prefix = "generated/sumpfork_dominion_dividers_"
postfix = "v" + version + ".pdf"


def doit(args, main):
    args = args + " --outfile " + prefix + main + postfix
    args = args.split()
    fname = args[-1]
    print(args)
    print(":::Generating " + fname)
    options = domdiv.main.parse_opts(args)
    options = domdiv.main.clean_opts(options)
    domdiv.main.generate(options)
    return fname


argsets = [
    ("", ""),
    ("--orientation=vertical", "vertical_"),
    ("--papersize=A4", "A4_"),
    ("--papersize=A4 --orientation=vertical", "vertical_A4_"),
    ("--size=sleeved", "sleeved_"),
    ("--size=sleeved --orientation=vertical", "vertical_sleeved_"),
]
additional = ["--expansion-dividers"]

fnames = [doit(args[0] + " " + " ".join(additional), args[1]) for args in argsets]
print(fnames)

zip = zipfile.ZipFile(
    f"generated/sumpfork_dominion_dividers_v{version}.zip",
    "w",
    zipfile.ZIP_DEFLATED,
)
for f in fnames:
    zip.write(f, arcname=f"sumpfork_dominion_dividers/{os.path.basename(f)}")
zip.close()
