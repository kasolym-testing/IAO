from pathlib import Path


def newline(fileobj, repeat=1):
    return fileobj.write("\n" * repeat)


# cleverref must come AFTER hyperref
pkgs = ["physics", "siunitx", "graphicx", "amsmath", "hyperref", "cleveref"]
alltex = list(Path("doc").glob("*.tex"))

titlepg = r'''\begingroup
\thispagestyle{empty}
%\AddToShipoutPicture*{\put(0,0){\includegraphics[scale=1.25]{esahubble}}} % Image background
\centering
\vspace*{5cm}
\par\normalfont\fontsize{35}{35}\sffamily\selectfont
\textbf{국제천문올림피아드 }\\
{\LARGE IAO 역대 문제 및 해설}\par % Book title
\vspace*{1cm}
{\Huge Yoonsoo P. Bach}\par % Author name
\endgroup

\tableofcontents

'''

with open("main_IAO.tex", "w+") as mf:
    mf.write(r"\documentclass[10pt,a4paper]{book}" + '\n')
    mf.write(r"\usepackage[top=3cm,bottom=3cm,left=3.2cm,right=3.2cm,headsep=10pt,letterpaper]{geometry}")
    newline(mf, 1)
    mf.write(r"\usepackage{kotex}" + '\n')
    for p in pkgs:
        mf.write(r"\usepackage{{{}}}".format(p) + '\n')
    newline(mf, 2)

    mf.write(r"\begin{document}" + '\n\n')
    mf.write(titlepg)
    for t in alltex:
        mf.write(r"\input{{{}}}".format(t) + '\n')
    newline(mf, 2)
    mf.write(r"\end{document}")