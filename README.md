# number memory
To make it easier to remember long numbers, I created a script that converts them into strings of text.
For example: 231 would first turn into 0231, since all numbers need even digits, then, we would read every digit:
1. check the digit index. If it is even, (start with 0), then use a consonant. Else, use a vowel.
2. find the number in the table, with the correct combination. So, we would have 0 as the first digit, and zero is on an even place, so it's a consonant. That's a P.
3. If we do this for every digit, we would get 'pase'. Isn't that easier to remember than "Two Hundred And Thirty-One"? This gets even better with longer numbers. The first 25 digits of pi are petenaafunoeniecheechoefoewoolaloosoe. Long, but 25 digits is a lot.




### The Table
| number | consonant version | vowel version |
|--------|-------------------|---------------|
|    0   |         p         |       i       |
|    1   |         m         |       e       |
|    2   |         f         |       a       |
|    3   |         s         |       oe      |
|    4   |         t         |       oo      |
|    5   |         n         |       o       |
|    6   |         l         |       u       |
|    7   |         k         |       ee      |
|    8   |         w         |       ie      |
|    9   |        ch         |       aa      |

#### Warning: These are meant for my use, so I used Dutch sounds. If two sound too similar, you can just for my repo and edit the table and data.py.