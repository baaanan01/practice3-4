def palindrome(s):
	while " " in s:
		s = s.replace(" ", "")
	s = s.lower()
	return s == s[::-1]