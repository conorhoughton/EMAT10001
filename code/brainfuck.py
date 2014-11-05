import sys

def advance_tape():
    global tape_location
    tape_location+=1
    if tape_location==len(tape):
        tape.append(0)

def rewind_tape():
    global tape_location
    if tape_location>0:
        tape_location-=1

def jump():
    global commands_location
    commands_location+=1
    count = 1
    while count!=0 and commands_location<len(commands):
        if commands[commands_location]==']':
            count -= 1
        elif commands[commands_location]=='[':
            count += 1
        commands_location+=1
    commands_location-=1

def jump_back():
    global commands_location
    commands_location-=1
    count = 1
    while count!=0 and commands_location>0:
        if commands[commands_location]=='[':
            count -= 1
        elif commands[commands_location]==']':
            count += 1
        commands_location-=1

   

def read_command():
    if commands[commands_location]=='+':
        tape[tape_location]+=1
    elif commands[commands_location]=='-':
        if tape[tape_location]>0:
            tape[tape_location]-=1
    elif commands[commands_location]=='>':
        advance_tape()
    elif commands[commands_location]=='<':
        rewind_tape()
    elif commands[commands_location]=='.':
         sys.stdout.write(chr(tape[tape_location]))
         sys.stdout.flush()
    elif commands[commands_location]==',':
        value=sys.stdin.read(1)
        tape[tape_location]+=ord(value)
    elif commands[commands_location]=='[':
        if tape[tape_location] == 0:
            jump()
    elif commands[commands_location]==']':
        if tape[tape_location] != 0:
            jump_back()
    elif debug==1 and commands[commands_location]=='#':
        print commands_location,tape_location
        print tape
        sys.stdout.flush()
    elif debug==2: 
        if commands[commands_location]!=' ':
            print commands[commands_location],commands_location,tape_location
            print tape
            sys.stdout.flush()

debug=1

commands_file=open('program.bf','r')

commands=commands_file.read()
commands_location=0

tape=[0]
tape_location=0


while(commands_location<len(commands)):
    read_command()
    commands_location+=1

print
