import sys

# --last-name Cleese --first-name John

print(sys.argv)

for i in range(1, len(sys.argv), 2):
    print(sys.argv[i], sys.argv[i+1])