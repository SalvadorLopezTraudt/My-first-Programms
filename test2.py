while True:
    line=input(">")
    if line=="done":
        break
    print(line)
print("Done!")
# break gets an extra indendation because it follows an if statement so it has to be extra indented
# print(line) is deindented to ensure its still part of the codeblock while True and not part of the break
#its still a loop that awaits the command "done" so the prinbt(done) only appears after we broke the loop via the command "done"
# the break command ends the loop and jumps immediately to the next following line (print(done))
