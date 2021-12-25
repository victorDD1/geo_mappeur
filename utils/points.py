from numpy import linspace
from utm import from_latlon

def lat_long_to_x_y(latitude, longitude):
    if type(latitude) != list:
        x, y, _, _ = from_latlon(latitude, longitude)
        return x, y
    else :
        x_list = []
        y_list = []
        for lat, lon in zip(latitude, longitude):
            x, y, _, _ = from_latlon(lat, lon)
            x_list.append(x)
            y_list.append(y)
        return x_list, y_list

def change_origin(x_list, y_list, x_o, y_o):
    '''
    (x_o, y_o) new origin
    '''
    x_list = [x - x_o for x in x_list]
    y_list = [y - y_o for y in y_list]

    return x_list, y_list

def content_to_x_y_z(content):
    '''
    Read coordinates from the web page's content (latitude, longitude, altitude)
    Convert in (x,y,z)
    '''
    longitude = []
    latitude = []
    z_list = []
    for line in content.split('\n'):
        if 'lon' in line:
            longitude.append(float(line.replace('<lon>','').replace('</lon>', '').replace('\n', '')))
        if 'lat' in line:
            latitude.append(float(line.replace('<lat>','').replace('</lat>', '').replace('\n', '')))
        if 'z' in line:
            z_list.append(float(line.replace('<z>','').replace('</z>', '').replace('\n', '')))

    x_list, y_list = lat_long_to_x_y(latitude, longitude)
    return x_list, y_list, z_list

def save_points_txt(x_list, y_list, z_list, file_path):
    with open(file_path, 'a') as f:
        for x,y,z in zip(x_list, y_list, z_list):
            str_1, str_2 = '{', '}'
            f.writelines(f'{str_1}{x},{y},{z}{str_2}\n')
    f.close

def define_lines_from_corners(top_left_corner, bottom_rigth_corner, x_res = 50):
    '''
    Defines the pairs of points to create the elevation map from the elevation lines. One pair of points define an elevation line.
    Points coordinates are given in latitude, longitude
    Return :
        - list(tupple(list)) : [([lat_11, lon_1], [lat_12, lon_1]), ..., ([lat_N1, lon_N], [lat_N2, lon_N])]
    '''
    assert (top_left_corner[0]>bottom_rigth_corner[0] and top_left_corner[1]<bottom_rigth_corner[1]), print('Choose the right points!\n first coordinate <-> top left corner | second coordinate <-> bottom right corner')
    long_points_list = linspace(top_left_corner[1], bottom_rigth_corner[1], num = x_res)

    lat_top, lat_bottom = top_left_corner[0], bottom_rigth_corner[0]
    pairs_points_list = []

    for lon in long_points_list:
        pairs_points_list.append(([lat_top, lon], [lat_bottom, lon]))
    
    return pairs_points_list