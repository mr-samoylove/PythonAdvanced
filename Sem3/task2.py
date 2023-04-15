# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов.
# За основу возьмите любую статью из википедии или из документации к языку.

import re
from collections import Counter

text = """Johann Carl Friedrich Gauss (/ɡaʊs/; German: Gauß [kaʁl ˈfʁiːdʁɪç ˈɡaʊs] (listen);[2][3] Latin: \
Carolus Fridericus Gauss; 30 April 1777 – 23 February 1855) was a German mathematician and physicist who made \
significant contributions to many fields in mathematics and science.[4] Sometimes referred to as the Princeps \
mathematicorum (Latin for 'the foremost of mathematicians')[5] and "the greatest mathematician since antiquity", \
Gauss had an exceptional influence in many fields of mathematics and science; he is ranked among history's most influential mathematicians.[6]

He was a child prodigy in mathematics and completed his magnum opus, Disquisitiones Arithmeticae, at age 21. \
Gauss attended Collegium Carolinum and the University of Göttingen, where he made several mathematical discoveries. \
In 1807, he became the director of the astronomical observatory at the University of Göttingen, where he was active in mathematical research. Gauss died of a heart attack on February 23, 1855, in Göttingen.

He had two wives and six children. He had conflicts with his sons over their career choices, as he did not want them \
to enter mathematics or science, fearing they would not surpass his achievements. Despite being a hard worker, he was \
not a prolific writer and refused to publish incomplete work. Gauss was known to dislike teaching, but some of his \
students became influential mathematicians. He supported monarchy and opposed Napoleon. Gauss believed that the act of \
learning, not possession of knowledge, granted the greatest enjoyment.[7]

Gauss proved the fundamental theorem of algebra which states that every non-constant single-variable polynomial with \
complex coefficients has at least one complex root.[8] He made important contributions to number theory and developed \
the theories of binary and ternary quadratic forms. Gauss is also credited with inventing the fast Fourier transform \
algorithm and was instrumental in the discovery of the dwarf planet Ceres. His work on the motion of planetoids \
disturbed by large planets led to the introduction of the Gaussian gravitational constant and the method of least squares, \
which is still used in all sciences to minimize measurement error."""

counter = Counter()
for word in re.findall(r'\w+', text):
    counter[word] += 1

print(counter.most_common(10))
