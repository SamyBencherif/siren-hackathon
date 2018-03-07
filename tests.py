import sys
write = sys.stdout.write

from note_freqs import getFreq


def notefreqs_test():
    assert getFreq('C0') == 16.35
    assert getFreq('A4') == 440
    assert getFreq('A#2') == getFreq('Bb2') == 116.54


def run_tests():
    tests = {'get note names from freqencies': notefreqs_test}

    passed = 0
    failed = 0

    for name, callback in tests.items():

        write("Testing ability to " + name + '. [')

        try:
            callback()
            print 'Success!]'
            passed += 1
        except:
            print 'Failure!]'
            failed += 1

    print

    if failed == 0:
        print "Passed all tests!"
    else:
        print "Failed " + str(failed) + " out of " + str(passed + failed) + " tests."


run_tests()
