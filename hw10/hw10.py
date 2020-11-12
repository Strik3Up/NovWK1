# Author: Carter Monroe cam7002@psu.edu
# GitHub ID: Strik3Up
def is_anagram(s1, s2):
  x = 0
  while x < len(s1 + s2):
	for c in b:
		lob = b.lower()
		lobs = lob.strip()
		lobst = lobs.strip('"')
		lobstr = lobst.strip("-")
		lobstri = lobstr.strip(".")
		lobstrin = lobstri.strip(" ")
		loa = a.lower()
		loas = loa.strip()
		loast = loas.strip('"')
		loastr = loast.strip("-")
		loastri = loastr.strip(".")
		loastrin = loastri.strip(" ")
	x = x + 1
  bl = sorted(list("".join(lobstrin.split())))
  al = sorted(list("".join(loastrin.split())))
  if bl == al:
	  return "anagram"
  else:
	  return "not anagram" 
