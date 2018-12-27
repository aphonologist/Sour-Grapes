# Sour-Grapes

This repo contains the script testSourGrapes.py, which tests the weakly deterministic analysis of Sour Grapes in Lamont (2019). The script will return the output of the machines on a specific string if one is provided, and otherwise tests all strings of some length.

To call with a specific string, just type it after the script:

```
python testSourGrapes.py maaamasa
Input: maaamasa
Output of S1: mamamasa
Output of S2: mmmmmasa
Output of SG: mmmmmasa
Success: True
```

To test strings of some length n, just call the script:

```
python testSourGrapes.py
Total strings to test: 81
Total strings remaining: 0
SUCCESSFUL? True
```

By default, the script only reports the remaining number every 10 million strings, as the number of test cases grows exponentially. To change the length of strings to test, just change the value of n on line 138 of the script.

Lamont, Andrew. 2019. Sour Grapes is phonotactically complex. Poster at _LSA 2019 Annual Meeting_. New York, NY. January 3. Abstract-reviewed.
