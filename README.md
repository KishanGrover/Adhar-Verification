# Adhar-Verification
Document Verification Via image processing, first
started with the adhaar card number checker, extracting image to text
using tesseract and applying the Verhoeff algorithm(checksum(which i
checked using permutation and combination) for validating the adhaar card
number and extracting all details from the adhaar card to text and using it
for verification purposes.

PrePrequisites: 1.Docker 2.Python 3.Postman

Clone The Repositry in your specific destination Go inside the terminal/cmd and run command 
1.docker build -t abc .
2.docker run -d -p 5022:5022 --name abcd abc

now you can test in postman using Post method by entering localhost:5025 in url and passing images of adhar card
