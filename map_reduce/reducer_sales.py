import sys

last_pid = 999999
sales_amt_sum = 0

for line in sys.stdin:

    line = line.strip()
    pid, sales_amt = line.split("\t")
    sales_amt = int(sales_amt)
    # if this is the first iteration
    if not last_pid:
        last_pid = pid

    # if they're the same, log it
    if pid == last_pid:
        sales_amt_sum += sales_amt
    else:
        result = [last_pid, sales_amt_sum]
	if last_pid!=999999:
        	print("\t".join(str(v) for v in result))
        last_pid = pid
        sales_amt_sum = 0

# this is to catch the final counts after all records have been received.
print("\t".join(str(v) for v in [last_pid, sales_amt_sum]))

