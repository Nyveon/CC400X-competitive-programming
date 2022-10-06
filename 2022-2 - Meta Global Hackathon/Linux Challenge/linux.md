# Linux Challenge

## Problem

The following challenge requires you to use Linux. To find out how to install Linux as a Windows Subsystem please click the link below.
Instructions to find the 3 keys.

## Key 1

Find and unzip "Key1.zip" (Password will be required to unzip the folder, instructions below to find out the password). Open Key1.txt to get the key
The password is the sum of the following two values:
total number of files in the "Linux Challenge" directory (inc. sub directories)
number of .txt files in "Linux Challenge" directory (inc. sub directories) that contain the word "Meta" in the file name (not in the file itself)

Solution

```bash
number of files with "Meta": find . -iname '*Meta*.txt' | wc -l 63
Total number of files: find -type f | wc -l 141
Password = 204
```

## Key 2

Find and unzip "Key2.zip" (Password will be required to unzip the folder, instructions below to find out the password). Open Key2.txt to get the key
To get the password:
Find Profile 1.txt and Profile 2.txt and open them to find some social media data for each profile.
Compare the total number of instagram followers added in these 28 days. How many more followers has Profile 1 added compared to Profile 2, the answer is the password. (HINT - interestingly their daily social media stats seem to be exactly the same every day apart from the number of instagram followers they receive each day, even then, some days they seem to add the exact same number of followers.....)

Solution

```bash
diff Meta4/Profile\ 1.txt Meta8/Profile\ 2.txt
Sum profile 1 (not counting the same entries as profile 2 due to using diff)     101231
Sum profile 2 (not counting the same entries as profile 1 due to using diff)     6579
Password = 94652
```

## Key 3

Find and unzip "Key3.zip" (Password will be required to unzip the folder, instructions below to find out the password). Open Key3.txt to get the key
To get the password find Password.txt and extract the 2nd and 9th character of each line in Password.txt

Solution

```bash
cut -c 2,9 Meta2/Password.txt
displays: ThePasswordIsZuckerberg!?56412
Password = Zuckerberg!?56412
```
