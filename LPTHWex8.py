# exercise 8 demonstrates to the student further use of the formatter 
formatter = "%r %r %r %r" # formatter "r" accepts all data types and is useful for debugging

print formatter % (1, 2, 3, 4 )
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
	"I had this thing.", 
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
)