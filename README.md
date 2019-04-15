# ABAQUS-Remove-bad-elements
The script remove failed elements in Abaqus inp-file by means of comment sign

---Scope---
If mesh has a number of failed elements in uncritical parts and the model can't be remeshed the solution is to remove fail elements from the model

---Steps---
1. Creating a text file with failed elements
 - Open odb-file of a model with failed elements in ABAQUS VIEW
 - Use command REPLACE in CREATE DISPLAY GROUP to make visible a set of failed elements
 - Use command ACTIVE ELEMENTS in TOOLS->QUERY->ELEMENTS (see Picture.png)
 - Copy numbers of the failed elements into a text file (see Picture.png).
2. Command:
python CommentElem.py [a text file of failed elements] [inp-file]

*Note: The script searches '*Element' at the beginning to find the section to comment elements
