"""reverse this tuple: t=( 1,2,3,4,5)"""

t=(1,2,3,4,5)
print("Tuple elements are: ",t)
y=reversed(t)
print("Reversed tuple are: ",(tuple(y)))

rt=list(t)
print("now its list here",rt)
rt.reverse()
rt=tuple(rt)
print("Reversed tuple using list are: ",rt)
