while True:
    line=input(">")
    if line[0]=="#":
        continue
    if line=="done":
        break
    print(line)
print("done")
#as long as my inputs start with an # it doesnt get repeated by the loop and it jumps back up to line=input(>), so the print(line) command doesnt run, continue brings u back to the start of the first if
