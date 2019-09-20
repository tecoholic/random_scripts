#!/usr/bin/env python
import argparse


def make_cards(filename, subject, chapter):
    template = """\documentclass[avery5371,grid,frame]{flashcards}
\geometry{margin=0.75cm}
\setlength{\cardwidth}{10cm}
\setlength{\cardheight}{6.5cm}
\setlength{\cardmargin}{0.3cm}
\\renewcommand{\cardrows}{4}
\\renewcommand{\cardcolumns}{2}
\usepackage{amsmath}

\cardfrontstyle[\LARGE\slshape]{headings}

\\begin{document}
"""
    if subject:
        template += "\n\cardfrontfoot{{{}}}".format(subject)

    f = open(filename, 'r')
    intext = f.read()
    cards = intext.split("\n\n")
    for card in cards:
        question, answer = card.strip().split("\n", 1)
        if "__" in question:
            question = question.replace("__", "\\underline{\hspace{1cm}}")
        if chapter:
            template += "\n\\begin{flashcard}["+chapter+"]{"+question+"}"
        else:
            template += "\n\\begin{flashcard}{"+question+"}"
        template += "\n    "+answer.replace("\n", "\\\\\n")
        template += "\n\end{flashcard}\n"

    template += "\n\end{document}"
    if not chapter:
        chapter = filename.split('.')[0]
    with open(chapter.replace(" ", "_")+".tex", 'w') as output:
        output.write(template)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="input filename")
    parser.add_argument(
        "subject", help="subject appears in the front of every card")
    parser.add_argument(
        "--chapter", help="chapter name appears in the front of every card")
    args = parser.parse_args()

    make_cards(args.filename, args.subject, args.chapter)
