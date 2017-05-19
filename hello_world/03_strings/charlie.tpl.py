@@charlie@@

tests = [
    "this is a test, containing Charlie",
    "A test with a charlie, but without C-harlie",
    "A test with nothing",
    "Another test with Charlie in the middle of the sentence"
]


def __my_find_charlie__(string):
    return string.find('Charlie')


def __test_find_charlie__(string):
    mine = __my_find_charlie__(string)
    theirs = find_charlie(string)
    if mine != theirs:
        return "find_charlie('%s') returned %i, but it should have returned %i" % (string, theirs, mine)
    else:
        return None


for test in tests:
    ret = __test_find_charlie__(test)
    if ret is not None:
        print ret
        exit(0)
print 'OK'
