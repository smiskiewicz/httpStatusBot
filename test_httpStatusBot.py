import unittest
import httpStatusBot
import sys



class formatUrlTests(unittest.TestCase):

    def testFullRequest(self):
        urlParts = httpStatusBot.formatUrl('www.google.com/testsuite/testcase')
        self.assertEqual(urlParts[0], 'www.google.com')
        self.assertEqual(urlParts[1], '/testsuite/testcase')

    def testHostRequest(self):
        urlParts = httpStatusBot.formatUrl('www.google.com')
        self.assertEqual(urlParts[0], 'www.google.com')
        self.assertEqual(urlParts[1], '')

    def testNoWWWRequest(self):
        url = httpStatusBot.formatUrl('stackoverflow.com/questions/3278418/testing-urllib2-application-http-responses-loaded-from-files')
        self.assertEqual(url[0], 'stackoverflow.com')
        self.assertEqual(url[1], '/questions/3278418/testing-urllib2-application-http-responses-loaded-from-files')

    def testHTTPRequest(self):
        url = httpStatusBot.formatUrl('http://localhost:80/')
        self.assertEqual(url[0], 'localhost:80')
        self.assertEqual(url[1], '/')

class getStatusTests(unittest.TestCase):
    class dummyRequest:
        def __init__(self, status, reason):
            self.status = status
            self.reason = reason
    goodStatus = [200, 1]
    badStatus = [404, 500]
    getStatusFailed = ('failed', 'WEBSITE DOWN!')
    getStatusPassed = (True, 'Website Up.')

    def testGoodStatus(self):
        goodRequest = getStatusTests.dummyRequest(200, 'OK')
        self.assertEqual(httpStatusBot.getStatus(goodRequest, getStatusTests.goodStatus, getStatusTests.badStatus), self.getStatusPassed)

    def testGoodStatus2(self):
        goodRequest = getStatusTests.dummyRequest(1, 'OK')
        self.assertEqual(httpStatusBot.getStatus(goodRequest, getStatusTests.goodStatus, getStatusTests.badStatus), self.getStatusPassed)

    def testBadStatus(self):
        goodRequest = getStatusTests.dummyRequest(404, 'BAD')
        self.assertEqual(httpStatusBot.getStatus(goodRequest, getStatusTests.goodStatus, getStatusTests.badStatus), self.getStatusFailed)

    def testBadStatus2(self):
        goodRequest = getStatusTests.dummyRequest(500, 'BAD')
        self.assertEqual(httpStatusBot.getStatus(goodRequest, getStatusTests.goodStatus, getStatusTests.badStatus), self.getStatusFailed)

    def testNotListedStatus(self):
        goodRequest = getStatusTests.dummyRequest(1234, 'UNKNOWN')
        self.assertEqual(httpStatusBot.getStatus(goodRequest, getStatusTests.goodStatus, getStatusTests.badStatus), None)

class checkCurrentTimeTests(unittest.TestCase):

    def testEqualTimeout(self):
        self.assertEqual(httpStatusBot.checkCurrentTime(6, 6), False)

    def testGreaterThanTimeout(self):
        self.assertEqual(httpStatusBot.checkCurrentTime(7, 6), False)

    def testLessThanTimeout(self):
        self.assertEqual(httpStatusBot.checkCurrentTime(1, 5), 2)

class pingSiteTests(unittest.TestCase):

    def testException(self):
        self.assertRaises(Exception, httpStatusBot.pingSite('www.1', ''))

def main():
    print sys.path
    unittest.main()

if __name__ == '__main__':
    main()
