class Neuron:

    def __init__(self, w, f = lambda x: x):
        self.w=w
        self.f=f
        self.x=None

    def forward(self, x):
        self.x=x
        value= [self.w[i]*x[i] for i in range(len(x))]
        return self.f(sum(value))

    def backlog(self):
        return self.x

# n=Neuron([1,2,3], lambda x:x**2)
# print(n.forward([3,4,5]))
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        return f"ListNode({self.val}) -> {self.next}"
