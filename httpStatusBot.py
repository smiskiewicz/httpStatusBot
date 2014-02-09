import argparse
import time
import sys
import httplib

##Built in python 2.7.3
##Author: Steve Miskiewicz

##Check the status of the request, will return true for goodStatus
##sys.exit badStatus
def getStatus(r1, goodStatus, badStatus):
    if r1.status in goodStatus:
        done = True
        status = "Website Up."
        return done, status
    elif r1.status in badStatus:
        done = 'failed'
        status = "WEBSITE DOWN!"
        return done, status
    else:
        print "Current Status:", r1.status, "ignored. Retrying..."

##Get a response from the URL, print out varables if bad
def pingSite(host, request):
    try:
        w1 = httplib.HTTPConnection(host)
        w1.request("GET", request)
        r1 = w1.getresponse()
    except Exception, err:
        print "Bad URL! Please check your entry."
        print "Host:", host
        print "Request:", request
        return err
    return r1

##Check the time and wait a second
def checkCurrentTime(length, timeout):
    if length >= timeout:
        checkTime = False
        return checkTime

    else:
        time.sleep(1)
        length += 1
        return length

##Seporate the host from the rest of the URL
def formatUrl(url):
    formatedUrl= url.split("/")
    trailingUrl = ''
    host = formatedUrl[0]
    formatedUrl.remove(host)
    for item in formatedUrl:
        x = '/' + item
        trailingUrl += x
    return host, trailingUrl

def cmdArgs(args):
    timeout = 60
    parser = argparse.ArgumentParser(description='URL to Ping')
    parser.add_argument('-u', '--url', action="store", help='Enter a full web address to check against goodStatus list', required=True)
    parser.add_argument('-t', '--time', action="store", help='Enter number of seconds to ping, default is ' + str(timeout), type=int, required=False)  
    args = parser.parse_args()
    url = args.url
    if args.time:
        timeout = args.time
    return url, timeout

def main():
    checkTime = True
    timeCheck = 0
    goodStatus = [200]
    badStatus = [400, 401, 403, 404, 500]
    ##Get cmd args
    args = cmdArgs(sys.argv)
    ##args = cmdArgs()
    url = args[0]
    timeout = args[1]
    formatedUrl= formatUrl(url)
    
    print "Status Check for website:", url
    ##Start checking the website for proper status codes,
    ##will exit after match or timeout
    while checkTime:
        timeCheck = checkCurrentTime(timeCheck, timeout)
        if timeCheck == False:
            print "Timeout exceeded!", "Status:", r1.status, "Reason:", r1.reason
            sys.exit(1)
            break
        print "URL:", url, "Attempt:", timeCheck
        r1 = pingSite(formatedUrl[0], formatedUrl[1])
        done = getStatus(r1, goodStatus, badStatus)
        if done:
            print done[1], "Status:", r1.status, "Reason:", r1.reason
            break
        if done == 'failed':
            sys.exit(1)

if __name__ == '__main__':
    main()
