import sys

class Brain:

    def __init__(self,location):
        self.location=location

        self.commands=[]
        self.commands_location=0

        self.tape=[0]
        self.tape_location=0
        
        self.debug=0
        self.jump_mode=False
        self.jump_count=0

        self.execution_mode=True

    def execute(self,command):
        program_location_change=0
        if self.commands_location==len(self.commands):
            if command=="*":
                return -1
            elif command=="!":
                self.execution_mode= not self.execution_mode
                program_location_change=1
                return [self.location,program_location_change]
            else:
                self.commands.append(command)
                program_location_change=1
        execution_location=self.location
        if self.debug==4:
            print self.commands[self.commands_location],self.jump_count," ",
        if self.debug==5:
            if  not execution_location:
                print "*",
            else:
                print "!",
        if self.jump_count>0:
            if self.commands[self.commands_location]==']':
                self.jump_count -= 1
            elif self.commands[self.commands_location]=='[':
                self.jump_count += 1
        elif self.execution_mode:
            execution_location=self.execute_command()
        self.commands_location+=1
        return [execution_location,program_location_change]

    def advance_tape(self):
        self.tape_location+=1
        if self.tape_location==len(self.tape):
            self.tape.append(0)

    def rewind_tape(self):
        if self.tape_location>0:
            self.tape_location-=1

    def jump(self):
        self.jump_count = 1

    def jump_back(self):
        self.commands_location-=1
        count = 1
        while count!=0 and self.commands_location>0:
            if self.commands[self.commands_location]=='[':
                count -= 1
            elif self.commands[self.commands_location]==']':
                count += 1
            self.commands_location-=1
        self.commands_location+=1

    def execute_command(self):
        execution_location=self.location
        if self.commands[self.commands_location]=='+':
            self.tape[self.tape_location]+=1
        elif self.commands[self.commands_location]=='-':
            if self.tape[self.tape_location]>0:
                self.tape[self.tape_location]-=1
        elif self.commands[self.commands_location]=='>':
            self.advance_tape()
        elif self.commands[self.commands_location]=='<':
            self.rewind_tape()
        elif self.commands[self.commands_location]=='.':
            sys.stdout.write(chr(self.tape[self.tape_location]))
            sys.stdout.flush()
        elif self.commands[self.commands_location]==',':
            value=sys.stdin.read(1)
            self.tape[self.tape_location]+=ord(value)
        elif self.commands[self.commands_location]=='[':
            if self.tape[self.tape_location] == 0:
                self.jump()
        elif self.commands[self.commands_location]==']':
            if self.tape[self.tape_location] != 0:
                self.jump_back()
        elif self.commands[self.commands_location]=='}':
            execution_location+=self.tape[self.tape_location]
        elif self.commands[self.commands_location]=='{':
            execution_location-=self.tape[self.tape_location]
            if execution_location<0:
                execution_location=0

        elif self.debug==1 and self.commands[self.commands_location]=='#':
            print self.commands_location,self.tape_location,self.location
            print self.tape
            sys.stdout.flush()
        elif self.debug==2: 
            if self.commands[self.commands_location]!=' ':
                print self.commands[self.commands_location],
                print ":",
                print "c",self.commands_location,"b",self.location,"[",
                for i,t in enumerate(self.tape):
                    if i==self.tape_location:
                        print "*",
                    print t,
                    if i==self.tape_location:
                        print "*",
                    print ",",
                print "]"
                sys.stdout.flush()
            if  self.commands[self.commands_location]=='#':
                for i,c in enumerate(self.commands):
                    if i==self.commands_location:
                        print "*",
                    print c,
                    if i==self.commands_location:
                        print "*",
                print "jump_count:",self.jump_count
        elif self.debug==3 and self.commands[self.commands_location]=='#': 
            for i,command in enumerate(self.commands):
                if i==self.commands_location:
                    print "^",
                print command,
            print
            sys.stdout.flush()

        return execution_location

def transfer(old_execution_location,execution_location):
    old_location=brains[old_execution_location].tape_location
    new_location=brains[execution_location].tape_location

    brains[execution_location].tape[new_location]=brains[old_execution_location].tape[old_location]

    old_low_number=0
    if(old_location>0):
        old_low_number=brains[old_execution_location].tape[old_location-1]
    if(new_location>0):
        brains[execution_location].tape[new_location-1]=old_low_number

    old_high_number=0
    if(old_location<len(brains[old_execution_location].tape)-1):
        old_high_number=brains[old_execution_location].tape[old_location+1]
    if(new_location<len(brains[execution_location].tape)-1):
        brains[execution_location].tape[new_location+1]=old_high_number
    else:
        brains[execution_location].tape.append(old_high_number)

program_file=open('program.of','r')

program=program_file.read()
program+=" "
program_location=0

brains = []

a_brain = Brain(0)

brains.append(a_brain)

execution_location=0
old_execution_location=0



while program_location<len(program):
    if program[program_location]=='*':
        program_location+=1
    else:
        command=program[program_location]
        while execution_location>=len(brains):
            a_brain=Brain(len(brains))
            brains.append(a_brain)
        if old_execution_location!=execution_location:
            transfer(old_execution_location,execution_location)
        old_execution_location=execution_location
        execution_location , program_location_change=brains[execution_location].execute(command)
        program_location+=program_location_change

while execution_location!=-1 and execution_location<len(brains):
    execution_location= brains[execution_location].execute('*')

print
