from urllib.request import Request, urlopen

def get_long_lat_z(http_request):
    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'fr-FR,en;q=0.8',
        'Connection': 'keep-alive'}

    req = Request(http_request, headers=hdr)
    try :
        page = urlopen(req)
    except :
        print("Can't open the web page")

    content = str(page.read().decode('UTF-8'))
    return content

def request_elevation_line_from_2_points(point_1, point_2, sampling = 50):
    '''
    Return http request to get elevation line data between 2 points
    '''
    lat_1, lon_1 = point_1
    lat_2, lon_2 = point_2
    request_elevation_line = lambda lon_1, lon_2, lat_1, lat_2, s : f'https://wxs.ign.fr/an7nvfzojv5wa96dsga5nk8w/alti/rest/elevationLine.xml?gp-access-lib=3.0.3&lon={lon_1:.6f}|{lon_2:.6f}&lat={lat_1:.6f}|{lat_2:.6f}&indent=true&crs=%27CRS:84%27&sampling={s}'

    http_request = request_elevation_line(lon_1, lon_2, lat_1, lat_2, sampling)

    return http_request
