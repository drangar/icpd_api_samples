import sys

for line in sys.stdin:
    line = line.strip()
    unpacked = line.split("|")
    PID, DATE, SALES_AMT = line.split("|")
    results = [PID,SALES_AMT]
    print("\t".join(results))

