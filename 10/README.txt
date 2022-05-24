First test:
    1000 matrices with shape (2, 3) and 1000 with shape (3, 2)
PyMatrix:
    steps: 100, mid time: 0.02642521619796753
CMatrix:
    steps: 100, mid time: 0.006873857975006103

>>> 0.02642521619796753 / 0.006873857975006103
3.844306398830428


Second test:
    10 matrices with shape (200, 300) and 10 with (300, 200):
PyMatrix:
    steps: 20, mid time: 26.675102007389068
CMatrix:
    steps: 20, mid time: 0.5459846973419189

>>> 26.675102007389068 / 0.5459846973419189
48.856867485947106
