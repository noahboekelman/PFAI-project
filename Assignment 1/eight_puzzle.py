from copy import deepcopy

class EightPuzzle:

    def __init__(self, initial_state, goal):
        self.state = initial_state
        self.goal = goal
        self.action = ["u","d","l","r"]
        self.ePos = self.state.index(0)

    def state_val(self):
        return (f"{self.state[0]}{self.state[1]}{self.state[2]}{self.state[3]}{self.state[4]}{self.state[5]}{self.state[6]}{self.state[7]}{self.state[8]}")

    def check_goal(self):
        if self.state==self.goal:
            return True
        else:
            return False
    
    def move(self, move):
        if move=="u":
            dc=deepcopy(self)
            if dc.u():
                return dc
        elif move=="d":
            dc=deepcopy(self)
            if dc.d():
                return dc
        elif move=="l":
            dc=deepcopy(self)
            if dc.l():
                return dc
        elif move=="r":
            dc=deepcopy(self)
            if dc.r():
                return dc
    
    def u(self):
        if self.ePos>2:
            self.state[self.ePos], self.state[self.ePos-3] = self.state[self.ePos-3], self.state[self.ePos]
            self.ePos-=3
            return True
        return False

    def d(self):
        if self.ePos<6:
            self.state[self.ePos], self.state[self.ePos+3] = self.state[self.ePos+3], self.state[self.ePos]
            self.ePos+=3
            return True
        return False
    
    def l(self):
        if (self.ePos%3)!=0:
            self.state[self.ePos], self.state[self.ePos-1] = self.state[self.ePos-1], self.state[self.ePos]
            self.ePos-=1
            return True
        return False

    def r(self):
        if ((self.ePos+1)%3)!=0:
            self.state[self.ePos], self.state[self.ePos+1] = self.state[self.ePos+1], self.state[self.ePos]
            self.ePos+=1
            return True
        return False

    def pretty_print(self):
        print('/-----------------\\')
        print(f'|  {self.state[0]}  |  {self.state[1]}  |  {self.state[2]}  |')
        print('+-----+-----+-----+')
        print(f'|  {self.state[3]}  |  {self.state[4]}  |  {self.state[5]}  |')
        print('+-----+-----+-----+')
        print(f'|  {self.state[6]}  |  {self.state[7]}  |  {self.state[8]}  |')
        print('\\-----------------/')
    
    def deb(self):
        print(self.state_val())

    def h_1(self):
        val=0
        for i in range(0,9):
            val+=(self.state[i]!=self.goal[i])
        return val
    
    def h_2(self):
        val=0
        for i in range(0,9):
            val += (abs(i%3 - self.state[i]%3) + abs(i/3 - self.state[i]/3))
        return val
    
    def score(self, h):
        if h==1 or h=="h_1": return self.h_1()
        elif h==2 or h=="h_2": return self.h_2()
        elif h==0 or h==None: return 0