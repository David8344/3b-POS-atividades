import zeep

url = "https://www.dataaccess.com/webservicesserver/numberconversion.wso?WSDL"

client = zeep.Client(wsdl=url)

number = 88775875557

result = client.service.NumberToWords(
    ubiNum = number
)

print(result)