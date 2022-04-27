pdflatex main
bibtex   main
pdflatex main
pdflatex main
rm main.aux  main.bbl  main.blg  main.lof  main.log  main.lot  main.out main.toc */*.aux
mv main.pdf ../CIGALE_Manual.pdf
