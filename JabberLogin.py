# -*- coding: utf-8 -*-
# try something like
#import html
import lxml.etree
import requests
from requests import Session
from requests.auth import HTTPBasicAuth
import xml.etree.ElementTree as ET
from zeep import Client
from zeep.transports import Transport
from zeep.cache import SqliteCache
from gluon.tools import Service
from gluon.tools import Mail


service=Service()

def call():
    session.forget()
    return service()

def argTest():
    x = tuple(request.args)
    return dict(parms=x)

def sample():
    return dict(message="Jabber SDK Demo")

@service.xml
def emServiceProdLogout(dvn):
    csfdvn = "CSF"+dvn
    urlProd = "https://nyp-uccepub-cj.newyorklife.com/emapp/EMAppServlet?device=" + csfdvn + "&doLogout=true"
    url = urlProd
    urlquery=url 
    response = requests.get(urlquery, verify=False)	
    result=response.content
    #data = ET.fromstring(response.content)
    #itm = data[0][0][2].text
    #result="result"
    #data = ET.fromstring(result)
    #emresult = result["emccDevice
    #dataP = data[0][0].text
    #dataP = data[0]
    return dict(emccDevice=result)	
    #return dict(emccDevice=result, data=dataP)
    #return dict(data=dataP)


@service.xml
def EMServiceProdLogin(dvn):
    csfdvn = "CSF"+dvn
    urlProd = "https://nyp-uccepub-cj.newyorklife.com:8443/emservice/EMServiceServlet?xml="
    urlLab = "https://nyt-ccepub-cj.newyorklife.com:8443/emservice/EMServiceServlet?xml="
    url = "https://nyt-ccepub-cj.newyorklife.com:8443/emservice/EMServiceServlet?xml="
    url = urlProd
    queryp1 = "<request><appInfo><appID>cuae</appID><appCertificate>1qazXSW@</appCertificate></appInfo><login>"
    queryp2 = "<deviceName>"+csfdvn+"</deviceName>"
    queryp3 = "<userID>" + dvn+ "</userID>"
    queryp4 = "</login></request>"
    #queryString = "<query><appInfo><appID>cuae</appID><appCertificate>1qazXSW@</appCertificate></appInfo><deviceUserQuery><deviceName>CSFT15BU9J</deviceName>#</deviceUserQuery></query>"
    queryString = queryp1 + queryp2 + queryp3 + queryp4 
    urlquery=url + queryString
    response = requests.get(urlquery, verify=False)	
    result=response.content
    #data = ET.fromstring(response.content)
    #itm = data[0][0][2].text
    #result="result"
    data = ET.fromstring(result)
    #emresult = result["emccDevice
    try:
        dataP = data[0][0].text
    except:
        dataP = data[0].text	
    #dataP = data[0]
    #return dict(emccDevice=result, data=dataP)
    return dict(data=dataP)

def demo():
    return dict(message="Jabber demo")

@service.xml
def EMServiceLogin(dvn):
    csfdvn = "CSF"+dvn
    urlProd = "https://nyp-uccepub-cj.newyorklife.com:8443/emservice/EMServiceServlet?xml="
    urlLab = "https://nyt-ccepub-cj.newyorklife.com:8443/emservice/EMServiceServlet?xml="
    url = "https://nyt-ccepub-cj.newyorklife.com:8443/emservice/EMServiceServlet?xml="
    queryp1 = "<request><appInfo><appID>PMEAXL</appID><appCertificate>6outhLawRlew</appCertificate></appInfo><login>"
    queryp2 = "<deviceName>"+csfdvn+"</deviceName>"
    queryp3 = "<userID>" + dvn+ "</userID>"
    queryp4 = "</login></request>"
    #queryString = "<query><appInfo><appID>cuae</appID><appCertificate>1qazXSW@</appCertificate></appInfo><deviceUserQuery><deviceName>CSFT15BU9J</deviceName>#</deviceUserQuery></query>"
    queryString = queryp1 + queryp2 + queryp3 + queryp4 
    urlquery=url + queryString
    response = requests.get(urlquery, verify=False)	
    result=response.content
    #data = ET.fromstring(response.content)
    #itm = data[0][0][2].text
    #result="result"
    data = ET.fromstring(result)
    #emresult = result["emccDevice
    dataP = data[0][0].text
    #dataP = data[0].text
    #dataP = data[0]
    #return dict(emccDevice=result, data=dataP)
    return dict(data=dataP)


@service.json
def EMService(dvn):
    url = "https://172.31.25.77:8443/emservice/EMServiceServlet?xml="
    queryp1 =  "<query><appInfo><appID>cuae</appID><appCertificate>1qazXSW@</appCertificate></appInfo><deviceUserQuery><deviceName>"
    queryphone= dvn
    queryp2 = "</deviceName></deviceUserQuery></query>"
    #queryString = "<query><appInfo><appID>cuae</appID><appCertificate>1qazXSW@</appCertificate></appInfo><deviceUserQuery><deviceName>CSFT15BU9J</deviceName></deviceUserQuery></query>"
    queryString = queryp1 + queryphone + queryp2
    urlquery=url + queryString
    response = requests.get(urlquery, verify=False)	
    result=response.content
    data = ET.fromstring(response.content)
    itm = data[0][0][2].text
    return dict(emccDevice=itm)


def EMServlet():
    return dict(msg = "login")

@service.json
def AXLWebSvc():
    WSDL_URL = 'file://F:/VoicePortal/axl/schema/12.5/AXLAPI.wsdl'
    CUCM_URL = 'https://172.31.25.77:8443/axl/' 
    #CUCM_URL = 'https://172.31.27.10:8443/axl/' 
    #CUCM_URL = 'https://10.135.20.10:8443/axl/' 
    #location = 'htt'https://172.31.25.77:8443/axl/'
    #location = 'htt'https://172.31.25.77:8443/axl/'
    USERNAME = 'cuae'
    PASSWORD = '1qazXSW@'
    
    session = Session()
    session.verify = False
    session.auth = HTTPBasicAuth(USERNAME, PASSWORD)
    transport = Transport(session=session, timeout=3000)
    client = Client(WSDL_URL, transport=transport)


    service1 = client.create_service('{http://www.cisco.com/AXLAPIService/}AXLAPIBinding',CUCM_URL)
    request_data ={'name': 'SEPEC1D8BBA476C'}
    request_data ={'name': 'CSFT15BU9J'}
    #request_data ={'uuid': '040C73E0-3B09-015D-D049-DFA3D4BDEDDF'}
    uuid =  ' '
    firstName = 'Search...' 
    lastName = ' '    
    lastUpdate = ' '
    emProfile = ' '
    status = ' '
    name = ' '
    try: 
        resp = service1.getPhone(**request_data)
        name = resp['return']['phone']['name']
        #firstName = resp['return']['user']['firstName']
        #firstName = 'Sakura'
        #lastName = resp['return']['user']['lastName']    
        #lastUpdate = resp['return']['user']['pinCredentials']['pinCredTimeChanged']
        #try:
        #    emProfile = resp['return']['user']['phoneProfiles']['profileName'][0]['_value_1']
        #except:
        #    emProfile = ''
        #try:
        #    lastUpdate = resp['return']['user']['pinCredentials']['pinCredTimeChanged']
        #except:
        #    lastUpdate  = ''
    except:
        #uuid =  ' '
        #firstName = ' ' 
        ##lastName = ' '    
        #lastUpdate = ' '
        #emProfile = ''
        status = 'Record Not Found' 

    return dict (result=name, cucm=CUCM_URL, status=status)


def emLogin1():
    return dict(message="Emobility Login")

def index(): 
    return dict(message="hello from Login.py")

def emProdLogin2():
    usertuple = tuple(request.args)
    userid = usertuple[0]
    return dict(message="Emobility Login",  usr=userid.upper())


def emProdLogin():
    usertuple = tuple(request.args)
    userid = usertuple[0]
    return dict(message="Emobility Login",  usr=userid.upper())

def emLogin():
    usertuple = tuple(request.args)
    userid = usertuple[0]
    return dict(message="Emobility Login", usr=userid.upper())

def call():
    session.forget()
    return service()

#@service.json
def AXLSvc():
    WSDL_URL = 'file://F:/VoicePortal/axl/schema/12.5/AXLAPI.wsdl'
    #CUCM_URL = 'https://172.31.25.77:8443/axl/' 
    #CUCM_URL = 'https://172.31.27.10:8443/axl/' 
    CUCM_URL = 'https://10.135.20.10:8443/axl/' 
    #location = 'htt'https://172.31.25.77:8443/axl/'
    #location = 'htt'https://172.31.25.77:8443/axl/'
    USERNAME = 'cuae'
    PASSWORD = '1qazXSW@'
    
    session = Session()
    session.verify = False
    session.auth = HTTPBasicAuth(USERNAME, PASSWORD)
    transport = Transport(session=session, timeout=3000)
    client = Client(WSDL_URL, transport=transport)


    service1 = client.create_service('{http://www.cisco.com/AXLAPIService/}AXLAPIBinding',CUCM_URL)
    request_data ={'name': 'SEPEC1D8BBA476C'}
    #request_data ={'uuid': '040C73E0-3B09-015D-D049-DFA3D4BDEDDF'}
    uuid =  ' '
    firstName = 'Search...' 
    lastName = ' '    
    lastUpdate = ' '
    emProfile = ' '
    status = ' '
    name = ' '
    try: 
        resp = service1.getPhone(**request_data)
        name = resp['return']['phone']['name']
        #firstName = resp['return']['user']['firstName']
        #firstName = 'Sakura'
        #lastName = resp['return']['user']['lastName']    
        #lastUpdate = resp['return']['user']['pinCredentials']['pinCredTimeChanged']
        #try:
        #    emProfile = resp['return']['user']['phoneProfiles']['profileName'][0]['_value_1']
        #except:
        #    emProfile = ''
        #try:
        #    lastUpdate = resp['return']['user']['pinCredentials']['pinCredTimeChanged']
        #except:
        #    lastUpdate  = ''
    except:
        #uuid =  ' '
        #firstName = ' ' 
        ##lastName = ' '    
        #lastUpdate = ' '
        #emProfile = ''
        status = 'Record Not Found' 

    return dict (result=name, cucm=CUCM_URL, status=status)

@service.json
def AXLWebService():
    axl_url = "https://172.31.25.77:8443/axl"
    axl_url = "https://10.135.20.10:8443/axl"
    data="data"
    username = "cuae"
    password = "1qazXSW@"
    auth = HTTPBasicAuth("cuae", "1qazXSW@")
    errorMsg = ""
    messg = "NA"
    name= ""
    axl_request = """
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ns="http://www.cisco.com/AXL/API/12.5">
	  <soapenv:Header/>
	 <soapenv:Body>
	  <ns:getPhone>
			  <name>SEPEC1D8BBA476C</name>
			  <returnedTags>
                 <name>%</name>
                 <description>%</description>
              </returnedTags>
      </ns:getPhone>
      </soapenv:Body>
</soapenv:Envelope>
"""
    try:
        response = requests.post(axl_url, data=axl_request, auth=auth, verify=0)
        if response.status_code ==200:
            #print("AXL Response")
            messg = response.text
            #data = response.json()
            root = ET.fromstring(response.content)
            name = root.find(".//{http://www.cisco.com/AXL/API/12.5}name").text
        else:
            errorMsg = "Error:" + " - " + response.reason
    except  Exception as e:
        #errorm = f("Error = {e}")
		errorMsg = repr(e)
        #errorMsg = e.text
    return dict(ret=messg, reterror=errorMsg, responseStatus = response.status_code, data=name)



def AXLService():
    axl_url = "https://172.31.25.77:8443/axl"
    axl_url = "https://10.135.20.10:8443/axl"
    data="data"
    username = "cuae"
    password = "1qazXSW@"
    auth = HTTPBasicAuth("cuae", "1qazXSW@")
    errorMsg = ""
    messg = "NA"
    name= ""
    axl_request = """
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ns="http://www.cisco.com/AXL/API/12.5">
	  <soapenv:Header/>
	 <soapenv:Body>
	  <ns:getPhone>
			  <name>SEPEC1D8BBA476C</name>
			  <returnedTags>
                 <name>%</name>
                 <description>%</description>
              </returnedTags>
      </ns:getPhone>
      </soapenv:Body>
</soapenv:Envelope>
"""
    try:
        response = requests.post(axl_url, data=axl_request, auth=auth, verify=0)
        if response.status_code ==200:
            #print("AXL Response")
            messg = response.text
            #data = response.json()
            root = ET.fromstring(response.content)
            name = root.find(".//{http://www.cisco.com/AXL/API/12.5}name").text
        else:
            errorMsg = "Error:" + " - " + response.reason
    except  Exception as e:
        #errorm = f("Error = {e}")
		errorMsg = repr(e)
        #errorMsg = e.text
    return dict(ret=messg, reterror=errorMsg, responseStatus = response.status_code, data=name)

@service.json
def EMSDeviceUserQuery(dvn):  #deviceUserQuery # passing devicename return Device name , userid, lastlogin , emccDevice
    csfdvn = "CSF"+dvn
    urlProd = "https://nyp-uccepub-cj.newyorklife.com:8443/emservice/EMServiceServlet?xml="
    urlLab = "https://nyt-ccepub-cj.newyorklife.com:8443/emservice/EMServiceServlet?xml="
    url = "https://nyt-ccepub-cj.newyorklife.com:8443/emservice/EMServiceServlet?xml="
    url = urlProd

    queryString = "<query><appInfo><appID>cuae</appID><appCertificate>1qazXSW@</appCertificate></appInfo><deviceUserQuery><deviceName>"
    queryString = queryString + csfdvn + "</deviceName></deviceUserQuery></query>"
    urlquery=url + queryString
    response = requests.get(urlquery, verify=False)	
    result=response.content

    #data = ET.fromstring(response.content)
    #itm = data[0][0][2].text
    #result="result"
    data = ET.fromstring(result)
    #emresult = result["emccDevice
    #try:
    #     dataP = data[0][0].text
    
	#except:
    try:
        datauserid = data[0][0][0].text #UserID
        datalastlogin = data[0][0][1].text #lastlogin
        dataemcc = data[0][0][2].text #emccDevice
    except: 
        datauserid= dvn
        datalastlogin = "Do not exist"
        dataemcc = "Do not exist"
    
	#dataP = 
    dataP1 = data[0]
    #return dict(emccDevice=result, data=dataP)
    root = lxml.etree.fromstring(result)
    #results = root.find('userID')
    results = root.find('deviceUserResults/device/userID')
    #textnumbers = results.find('field/value/text').text 
	
    return dict(emccDevice=dataemcc, 
				#resp = data, #response object
				deviceName=root.find('deviceUserResults/device').attrib['name'], 
				userid=datauserid, 
				lastlogin=datalastlogin,
			    url = urlquery)
    #return dict(ret = result)


@service.json
def EMSDeviceProfileQuery(dvn):
    csfdvn = "CSF"+dvn
    urlProd = "https://nyp-uccepub-cj.newyorklife.com:8443/emservice/EMServiceServlet?xml="
    urlLab = "https://nyt-ccepub-cj.newyorklife.com:8443/emservice/EMServiceServlet?xml="
    url = "https://nyt-ccepub-cj.newyorklife.com:8443/emservice/EMServiceServlet?xml="
    url = urlProd
    queryp1 = "<Qurey><appInfo><appID>cuae</appID><appCertificate>1qazXSW@</appCertificate></appInfo><deviceUserQuery>"
    queryp2 = "<deviceName>"+csfdvn+"</deviceName>"
    queryp4 = "</deviceUserQuery></query>"
    queryString = "<query><appInfo><appID>cuae</appID><appCertificate>1qazXSW@</appCertificate></appInfo><deviceUserQuery><deviceName>CSFT15BU9J</deviceName></deviceUserQuery></query>"
    profileQueryString = "<query><appInfo><appID>cuae</appID><appCertificate>1qazXSW@</appCertificate></appInfo><deviceProfileQuery><userID>" + dvn + "</userID></deviceProfileQuery></query>"
    urlquery = url + profileQueryString
    response = requests.get(urlquery, verify=False)	
    result=response.content
    root = lxml.etree.fromstring(result)
    errorCode = 'noError'
    try:
        results = root.find('deviceProfileResults/user/deviceProfile/isDefaultDeviceProfile').text
        ProfileName =root.find('deviceProfileResults/user/deviceProfile/deviceProfileName').text
        isUDP=root.find('deviceProfileResults/user/deviceProfile/isDefaultDeviceProfile').text
    except:
        isUDP = "Do not exist"
        ProfileName = "Do not exist"
        errorCode = root.find('deviceProfileResults/user/failure/error').text

    return dict(isUDP=isUDP,
				ProfileName = ProfileName,
				error=errorCode,
			    url = urlquery)

#@service.xml  #passing UserId return device name 
@service.json
def EMSUserDeviceQuery(dvn): 
    csfdvn = "CSF"+dvn
    urlProd = "https://nyp-uccepub-cj.newyorklife.com:8443/emservice/EMServiceServlet?xml="
    urlLab = "https://nyt-ccepub-cj.newyorklife.com:8443/emservice/EMServiceServlet?xml="
    url = urlProd
    queryString = "<query><appInfo><appID>cuae</appID><appCertificate>1qazXSW@</appCertificate></appInfo><userDevicesQuery><userID>"
    queryString = queryString + dvn +"</userID></userDevicesQuery></query>"
    urlquery = url + queryString
    try:
        response = requests.get(urlquery, verify=False)	
        result=response.content
        root = lxml.etree.fromstring(result)
        
        deviceName=root[0][0][0].text
        if deviceName is None:
			deviceName = "Do not exist"
        retCode = response.status_code
    except:
        deviceName = 'NA'
        
    return dict(deviceName = deviceName, retCode = retCode, qurl = urlquery, dvn=dvn)

def JabberEMLogin():
    return dict(message="JabberEMLogin", usr="T15BU9J")

def JabberEM():
    usertuple = tuple(request.args)
    userid = usertuple[0]
    return dict(message="Emobility Login",  usr=userid.upper())

def JabberEMProd():
    usertuple = tuple(request.args)
    userid = usertuple[0]
    return dict(message="Emobility Login",  usr=userid.upper())

def JabberEMProdV2():
    usertuple = tuple(request.args)
    userid = usertuple[0]
    return dict(message="Emobility Login",  usr=userid.upper())

def EM2():
    usertuple = tuple(request.args)
    userid = usertuple[0]
    return dict(message="Emobility Login",  usr=userid.upper())

def JabberEMProdUpd():
    usertuple = tuple(request.args)
    userid = usertuple[0]
    return dict(message="Emobility Login",  usr=userid.upper())	

def JabberEMProdV3():
    usertuple = tuple(request.args)
    userid = usertuple[0]
    return dict(message="Emobility Login",  usr=userid.upper())

def JabberEMProdV4():
    usertuple = tuple(request.args)
    userid = usertuple[0]
    userid = 't15bu9j'
    return dict(message="Emobility Login",  usr=userid.upper())

def JabberEMProd3():
    usertuple = tuple(request.args)
    userid = usertuple[0]
    return dict(message="Emobility Login",  usr=userid.upper())

    return dict(message="JabberEM", usr="T15BU9J")

@service.xml
def EMSAPIProdLogout(dvn):
    csfdvn = "CSF"+dvn
    urlProd = "https://nyp-uccepub-cj.newyorklife.com/emapp/EMAppServlet?device=" + csfdvn + "&doLogout=true"
    url = urlProd
    urlquery=url 
    response = requests.get(urlquery, verify=False)	
    result=response.content
    return dict(emccDevice=result)	


@service.json
def EMSAPIProdLogin(dvn):
    csfdvn = "CSF"+dvn
    urlProd = "https://nyp-uccepub-cj.newyorklife.com:8443/emservice/EMServiceServlet?xml="
    urlLab = "https://nyt-ccepub-cj.newyorklife.com:8443/emservice/EMServiceServlet?xml="
    url = "https://nyt-ccepub-cj.newyorklife.com:8443/emservice/EMServiceServlet?xml="
    url = urlProd
    queryp1 = "<request><appInfo><appID>cuae</appID><appCertificate>1qazXSW@</appCertificate></appInfo><login>"
    queryp2 = "<deviceName>"+csfdvn+"</deviceName>"
    queryp3 = "<userID>" + dvn+ "</userID>"
    queryp4 = "</login></request>"
    queryString = queryp1 + queryp2 + queryp3 + queryp4 
    urlquery=url + queryString
    response = requests.get(urlquery, verify=False)	
    result=response.content
    data = ET.fromstring(result)
    logoutb = "Yes"
    try:
        dataP = data[0][0].text
        if dataP.find("Device does not allow hoteling") > 0 :
            dataP = "Extension Mobility not allowed on this Jabber. Please contact support"
            logoutb = "No"
		
        if dataP.find("Phone currently has user logged in") > 0 :
            dataP = "You are currently logged in"		
            logoutb = "Yes"
    except:
        dataP = data[0].text	
    #dataP = data[0]
    #return dict(emccDevice=result, data=dataP)

    return dict(loginStatus=dataP, logoutb=logoutb)

@service.json
def EMSAPIProdLogout(dvn):
    csfdvn = "CSF"+dvn
    urlProd = "https://nyp-uccepub-cj.newyorklife.com/emapp/EMAppServlet?device=" + csfdvn + "&doLogout=true"
    url = urlProd
    urlquery=url 
    queryString = "<request><appInfo><appID>cuae</appID><appCertificate>1qazXSW@</appCertificate></appInfo><logout><deviceName>" +  csfdvn + "</deviceName></logout></request>"
    urlquery=url + queryString

    response = requests.get(urlquery, verify=False)	
    result=response.content
    retCode = response.status_code
    prompt1=result.find('Prompt') + 7
    prompt2=result.find('SoftKeyItem') -12
    text1 = result.find('<Text>') + 6
    text2 = result.find('Prompt') - 10
    #decodedHtml = html.unescape(resultttt)
    decodedHtml ="999"
    return dict(prompt=result[prompt1:prompt2], text=result[text1:text2],ret=result)

@service.json
def EMLogout(dvn):
    csfdvn = "CSF" + dvn
    url = "https://172.31.25.77:8443/emservice/EMServiceServlet?xml="
    qurl = "<request><appInfo><appID>cuae</appID><appCertificate>1qazXSW@</appCertificate></appInfo><logout>"
    qurl = qurl + "<deviceName>" + csfdvn + "</deviceName></logout></request>"
    url = url + qurl
    response = requests.get(url, verify=False)	
    result = response.content
    root = lxml.etree.fromstring(result)
    try:
        results = root.find('failure/error').text
    except:
        results = root.find('success')
        results = "success"
    return dict(retStatus=response.status_code, retCode=results)

@service.xml
def EMServiceProdLogin2(dvn):
    csfdvn = "CSF"+dvn
    urlProd = "https://nyp-uccepub-cj.newyorklife.com:8443/emservice/EMServiceServlet?xml="
    urlLab = "https://nyt-ccepub-cj.newyorklife.com:8443/emservice/EMServiceServlet?xml="
    url = "https://nyt-ccepub-cj.newyorklife.com:8443/emservice/EMServiceServlet?xml="
    url = urlProd
    queryp1 = "<request><appInfo><appID>cuae</appID><appCertificate>1qazXSW@</appCertificate></appInfo><login>"
    queryp2 = "<deviceName>"+csfdvn+"</deviceName>"
    queryp3 = "<userID>" + dvn+ "</userID>"
    queryp4 = "</login></request>"
    queryString = queryp1 + queryp2 + queryp3 + queryp4 
    urlquery=url + queryString
    response = requests.get(urlquery, verify=False)	
    result=response.content
    data = ET.fromstring(result)
    try:
        dataP = data[0][0].text
    except:
        dataP = data[0].text	

    return dict(data=dataP)


def UserDeviceQuery(dvn): 
    csfdvn = "CSF"+dvn
    urlProd = "https://nyp-uccepub-cj.newyorklife.com:8443/emservice/EMServiceServlet?xml="
    urlLab = "https://nyt-ccepub-cj.newyorklife.com:8443/emservice/EMServiceServlet?xml="
    url = urlProd

    queryString = "<query><appInfo><appID>cuae</appID><appCertificate>1qazXSW@</appCertificate></appInfo><userDevicesQuery><userID>"
    queryString = queryString + dvn +"</userID></userDevicesQuery></query>"
    urlquery = url + queryString
    try:
        response = requests.get(urlquery, verify=False)	
        result=response.content
        root = lxml.etree.fromstring(result)
        
        deviceName=root[0][0][0].text
        if deviceName is None:
			deviceName = "Do not exist"
        retCode = response.status_code

    except:
        deviceName = 'NA'

    return dict(deviceName = deviceName, retCode = retCode, qurl = urlquery, dvn=dvn)



def JabberEMProdGBS():
    usertuple = tuple(request.args)
    userid = usertuple[0]
    #userid = "t15bu9j"
    return dict(message="Emobility Login",  usr=userid.upper())


@service.xml
def EMServiceProdGBSLogin(dvn):
    csfdvn = "CSF"+dvn
    urlProd = "https://CGI-vCMPub-CJ.newyorklife.com:8443/emservice/EMServiceServlet?xml="
    #urlProd = "https://nyp-uccepub-cj.newyorklife.com:8443/emservice/EMServiceServlet?xml="
    urlLab = "https://nyt-ccepub-cj.newyorklife.com:8443/emservice/EMServiceServlet?xml="
    url = "https://nyt-ccepub-cj.newyorklife.com:8443/emservice/EMServiceServlet?xml="
    url = urlProd
    queryp1 = "<request><appInfo><appID>cuae</appID><appCertificate>1qazXSW@</appCertificate></appInfo><login>"
    queryp2 = "<deviceName>"+csfdvn+"</deviceName>"
    queryp3 = "<userID>" + dvn+ "</userID>"
    queryp4 = "</login></request>"
    #queryString = "<query><appInfo><appID>cuae</appID><appCertificate>1qazXSW@</appCertificate></appInfo><deviceUserQuery><deviceName>CSFT15BU9J</deviceName>#</deviceUserQuery></query>"
    queryString = queryp1 + queryp2 + queryp3 + queryp4 
    urlquery=url + queryString
    response = requests.get(urlquery, verify=False)	
    result=response.content
    data = ET.fromstring(result)
   try:
       dataP = data[0][0].text
    except:
       dataP = data[0].text	

    return dict(data=dataP)

@service.json
def EMUserDeviceQueryGBS(dvn): 
    csfdvn = "CSF"+dvn
    urlProd = "https://CGI-vCMPub-CJ.newyorklife.com:8443/emservice/EMServiceServlet?xml="
    urlProd = "https://10.135.20.11:8443/emservice/EMServiceServlet?xml="
    urlLab = "https://nyt-ccepub-cj.newyorklife.com:8443/emservice/EMServiceServlet?xml="
    url = urlProd

    queryString = "<query><appInfo><appID>cuae</appID><appCertificate>1qazXSW@</appCertificate></appInfo><userDevicesQuery><userID>"
    queryString = queryString + dvn +"</userID></userDevicesQuery></query>"
    urlquery = url + queryString
    try:
        response = requests.get(urlquery, verify=False)	
        result=response.content
        root = lxml.etree.fromstring(result)
        
        deviceName=root[0][0][0].text
        if deviceName is None:
			deviceName = "Do not exist"
        retCode = response.status_code
    except:
        deviceName = 'NA'

    return dict(deviceName = deviceName, retCode = retCode, qurl = urlquery, dvn=dvn)

#EMSDeviceUserQuery
@service.json
def EMSDeviceUserQueryGBS(dvn):  #deviceUserQuery # passing devicename return Device name , userid, lastlogin , emccDevice
    csfdvn = "CSF"+dvn
    urlProd = "https://CGI-vCMPub-CJ.newyorklife.com:8443/emservice/EMServiceServlet?xml="
    urlLab = "https://nyt-ccepub-cj.newyorklife.com:8443/emservice/EMServiceServlet?xml="
    url = urlProd

    queryString = "<query><appInfo><appID>cuae</appID><appCertificate>1qazXSW@</appCertificate></appInfo><deviceUserQuery><deviceName>"
    queryString = queryString + csfdvn + "</deviceName></deviceUserQuery></query>"
    urlquery=url + queryString
    response = requests.get(urlquery, verify=False)	
    result=response.content

    data = ET.fromstring(result)
    
    try:
        datauserid = data[0][0][0].text #UserID
        datalastlogin = data[0][0][1].text #lastlogin
        dataemcc = data[0][0][2].text #emccDevice
    except: 
        datauserid= dvn
        datalastlogin = "Do not exist"
        dataemcc = "Do not exist"
    
    dataP1 = data[0]
    root = lxml.etree.fromstring(result)
    results = root.find('deviceUserResults/device/userID')

    return dict(emccDevice=dataemcc, 
				#resp = data, #response object
				deviceName=root.find('deviceUserResults/device').attrib['name'], 
				userid=datauserid, 
				lastlogin=datalastlogin,
			    url = urlquery)

@service.json
def EMSDeviceProfileQueryGBS(dvn):
    csfdvn = "CSF"+dvn
    urlProd = "https://CGI-vCMPub-CJ.newyorklife.com:8443/emservice/EMServiceServlet?xml="
    urlLab = "https://nyt-ccepub-cj.newyorklife.com:8443/emservice/EMServiceServlet?xml="
    url = "https://nyt-ccepub-cj.newyorklife.com:8443/emservice/EMServiceServlet?xml="
    url = urlProd
    queryp1 = "<Qurey><appInfo><appID>cuae</appID><appCertificate>1qazXSW@</appCertificate></appInfo><deviceUserQuery>"
    queryp2 = "<deviceName>"+csfdvn+"</deviceName>"
    queryp4 = "</deviceUserQuery></query>"
    queryString = "<query><appInfo><appID>cuae</appID><appCertificate>1qazXSW@</appCertificate></appInfo><deviceUserQuery><deviceName>CSFT15BU9J</deviceName></deviceUserQuery></query>"
    profileQueryString = "<query><appInfo><appID>cuae</appID><appCertificate>1qazXSW@</appCertificate></appInfo><deviceProfileQuery><userID>" + dvn + "</userID></deviceProfileQuery></query>"
    urlquery = url + profileQueryString
    response = requests.get(urlquery, verify=False)	
    result=response.content

    root = lxml.etree.fromstring(result)
    errorCode = 'noError'
    try:
        results = root.find('deviceProfileResults/user/deviceProfile/isDefaultDeviceProfile').text
        ProfileName =root.find('deviceProfileResults/user/deviceProfile/deviceProfileName').text
        isUDP=root.find('deviceProfileResults/user/deviceProfile/isDefaultDeviceProfile').text
    except:
        isUDP = "Do not exist"
        ProfileName = "Do not exist"
        errorCode = root.find('deviceProfileResults/user/failure/error').text

    return dict(isUDP=isUDP,
				ProfileName = ProfileName,
				error=errorCode,
			    url = urlquery)

@service.json
def EMSAPIProdLoginGBS(dvn):
    csfdvn = "CSF"+dvn
    urlProd = "https://nyp-uccepub-cj.newyorklife.com:8443/emservice/EMServiceServlet?xml="
    urlLab = "https://nyt-ccepub-cj.newyorklife.com:8443/emservice/EMServiceServlet?xml="
    url = "https://nyt-ccepub-cj.newyorklife.com:8443/emservice/EMServiceServlet?xml="
    url = urlProd
    queryp1 = "<request><appInfo><appID>cuae</appID><appCertificate>1qazXSW@</appCertificate></appInfo><login>"
    queryp2 = "<deviceName>"+csfdvn+"</deviceName>"
    queryp3 = "<userID>" + dvn+ "</userID>"
    queryp4 = "</login></request>"
    #queryString = "<query><appInfo><appID>cuae</appID><appCertificate>1qazXSW@</appCertificate></appInfo><deviceUserQuery><deviceName>CSFT15BU9J</deviceName>#</deviceUserQuery></query>"
    queryString = queryp1 + queryp2 + queryp3 + queryp4 
    urlquery=url + queryString
    response = requests.get(urlquery, verify=False)	
    result=response.content
    data = ET.fromstring(result)
    logoutb = "Yes"
    try:
        dataP = data[0][0].text
        if dataP.find("Device does not allow hoteling") > 0 :
            dataP = "Extension Mobility not allowed on this Jabber. Please contact support"
            logoutb = "No"
		
        if dataP.find("Phone currently has user logged in") > 0 :
            dataP = "You are currently logged in"		
            logoutb = "Yes"
    except:
        dataP = data[0].text	

    return dict(loginStatus=dataP, logoutb=logoutb)


@service.json
def EMLogoutGBS(dvn):
    csfdvn = "CSF" + dvn
    url = "https://CGI-vCMPub-CJ:8443/emservice/EMServiceServlet?xml="
    qurl = "<request><appInfo><appID>cuae</appID><appCertificate>1qazXSW@</appCertificate></appInfo><logout>"
    qurl = qurl + "<deviceName>" + csfdvn + "</deviceName></logout></request>"
    url = url + qurl
    response = requests.get(url, verify=False)	
    result = response.content
    root = lxml.etree.fromstring(result)
    try:
        results = root.find('failure/error').text
    except:
        results = root.find('success')
        results = "success"
    return dict(retStatus=response.status_code, retCode=results, url=url, query=qurl)
	
@service.json
def EMSUserDeviceQueryGBS(dvn): 
    csfdvn = "CSF"+dvn
    urlProd = "https://CGI-vCMPub-CJ.newyorklife.com:8443/emservice/EMServiceServlet?xml="
    urlLab = "https://nyt-ccepub-cj.newyorklife.com:8443/emservice/EMServiceServlet?xml="
    url = urlProd
    queryString = "<query><appInfo><appID>cuae</appID><appCertificate>1qazXSW@</appCertificate></appInfo><userDevicesQuery><userID>"
    queryString = queryString + dvn +"</userID></userDevicesQuery></query>"
    urlquery = url + queryString
    try:
        response = requests.get(urlquery, verify=False)	
        result=response.content
        root = lxml.etree.fromstring(result)
        
        deviceName=root[0][0][0].text
        if deviceName is None:
			deviceName = "Do not exist"
        retCode = response.status_code
    except:
        deviceName = 'NA'
        
    return dict(deviceName = deviceName, retCode = retCode, qurl = urlquery, dvn=dvn)

@service.json
def EMSUserDeviceQueryGBS(dvn): 
    csfdvn = "CSF"+dvn
    urlProd = "https://CGI-vCMPub-CJ.newyorklife.com:8443/emservice/EMServiceServlet?xml="
    urlLab = "https://nyt-ccepub-cj.newyorklife.com:8443/emservice/EMServiceServlet?xml="
    url = urlProd
    queryString = "<query><appInfo><appID>cuae</appID><appCertificate>1qazXSW@</appCertificate></appInfo><userDevicesQuery><userID>"
    queryString = queryString + dvn +"</userID></userDevicesQuery></query>"
    urlquery = url + queryString
    try:
        response = requests.get(urlquery, verify=False)	
        result=response.content
        root = lxml.etree.fromstring(result)
        
        deviceName=root[0][0][0].text
        if deviceName is None:
			deviceName = "None - Do not exist"
        retCode = response.status_code
    except:
        deviceName = 'NA'

    return dict(deviceName = deviceName, retCode = retCode, qurl = urlquery, dvn=dvn)
