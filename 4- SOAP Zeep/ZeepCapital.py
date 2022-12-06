import zeep

url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL"
client = zeep.Client(wsdl=url)
codigo_p = "BR"
result = client.service.CapitalCity(
    sCountryISOCode = codigo_p
)
print(f"A capital do {codigo_p} é {result}")