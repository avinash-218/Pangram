def main():
 inp=input("Enter a string\n")
 print(pangram(inp))

def pangram(inp):
 inp=inp.lower()
 l=set('abcdefghijklmnopqrstuvwxyz')
# for i in l:
#  if i not in inp:
#   return False
# return True'''
 inpset=set(inp)
 return l<=inpset
 

main()
