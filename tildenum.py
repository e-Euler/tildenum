#!/usr/bin/python3
import requests
import argparse


def parseargs():
        parser=argparse.ArgumentParser(add_help=True)
        parser.add_argument('-u', '--url',help='Full URL to test (ex. http://<hostname>/)')
        parser.add_argument('-s','--sensitive',action='store_true', help='Set to case sensitive default=false',default=False)
        parser.add_argument('-v', '--verbose',action='store_true',help='Enable verbose logging',default=False)
        #parser.add_argument('-w','--wordlist',action='store_false',help='Wordlist to use to bruteforce directories')
        parser.add_argument('-m','--method',default='OPTIONS',help='Method to use for enumeration (ex. GET,OPTIONS,POST,TRACE,HEAD)')
        args=parser.parse_args()
        return args

def tildeenum(args,url,method,verbose):
        dirs=['']
        if args.sensitive==False:
                chars='abcdefghijklmnopqrstuvwx._-yz1234567890'
        if args.sensitive==True:
                chars='abcdefghijklmnopqrstuvwxyz_-.ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        if len(url) - len(url) >= 6:
                print("Found!!!")
        if len(url) - len(url) < 6:
                #print(len(url) - len(args.url))
                for x in chars:
                        testurl="%s%s"%(url,x)
                        if verbose == True:
                                print(testurl,end="             \r")
                        #OPTIONS,POST,DEBUG,TRACE,GET,HEAD
                        match method:
                                case "OPTIONS":
                                        response=requests.options("%s*~1*" %(testurl))
                                case "POST":
                                        response=requests.post("%s*~1*" %(testurl))
                                #case "DEBUG":
                                #       reponse=requests.debug("%s*~1*" %(testurl))
                                case "TRACE":
                                        reponse=requests.trace("%s*~1*" %(testurl))
                                case "GET":
                                        response=requests.get("%s*~1*" %(testurl))
                                case "HEAD":
                                        response=requests.head("%s*~1*" %(testurl))
                        if response.status_code == 404:
                                print(("%s%s"%(testurl,"            ")))
                                tildeenum(args,testurl,method,verbose)
                        if args.verbose == True:
                                print(testurl+" "+str(response.status_code),end="           \r")

def main():
        args = parseargs()
        url = args.url
        method = args.method
        verbose = args.verbose
        tildeenum(args,url,method,verbose)
main()