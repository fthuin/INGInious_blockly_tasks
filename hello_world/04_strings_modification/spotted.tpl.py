def find_charlie(string):
    return string.find('Charlie')

@@spotted@@

tests = [
    "this is a test, containing Charlie",
    "A test with a charlie, but without C-harlie",
    "A test with nothing",
    "Another test with Charlie in the middle of the sentence"
]


def __my_spot_charlie__(string):
    pos_charlie = find_charlie(string)
    if pos_charlie != -1:
        return string[0:pos_charlie] + "SPOTCharlieSPOT" + string[pos_charlie+7:]
    else:
        return string


def __test_spot_charlie__(string):
    mine = __my_spot_charlie__(string)
    theirs = spot_charlie(string)
    if mine != theirs:
        return "spot_charlie('%s') returned '%s', but it should have returned '%s'" % (string, theirs, mine)
    else:
        return None


for test in tests:
    ret = __test_spot_charlie__(test)
    if ret is not None:
        print ret
        exit(0)
print 'OK'
