import argparse
import os
from time import sleep
from numpy.random import rand

from utils.points import lat_long_to_x_y, define_lines_from_corners, content_to_x_y_z, change_origin, save_points_txt
from utils.plot import plot_3d_from_txt
from utils.web_scrapping import request_elevation_line_from_2_points, get_long_lat_z

def main(args):
    
    x_list, y_list, z_list = [], [], []

    # Saving file path
    if not(os.path.exists('./data')):
        os.mkdir('./data')

    if args.file_name == '':
        x_1, y_1 = args.top_left_corner
        x_2, y_2 = args.bottom_right_corner
        file_path = f'./data/lon_{x_1}-{x_2}_lat_{y_1}-{y_2}_data.txt'
    else : 
        file_path = os.path.join('data', args.file_name + '.txt')
    # Remove if exists
    if os.path.exists(file_path):
        os.remove(file_path)

    x_0, _ = lat_long_to_x_y(args.top_left_corner[0], args.top_left_corner[1])
    _, y_0 = lat_long_to_x_y(args.bottom_right_corner[0], args.bottom_right_corner[1])
    
    pairs_points_list = define_lines_from_corners(args.top_left_corner, args.bottom_right_corner, args.number_points_x)

    # Get points coordinates for each elevation lines (corresponding to each pair of points)
    for pair_points in pairs_points_list:
        http_request = request_elevation_line_from_2_points(pair_points[0], pair_points[1], args.number_points_y)
        data_content = get_long_lat_z(http_request)
        x_tmp_list, y_tmp_list, z_tmp_list = content_to_x_y_z(data_content)

        x_tmp_list, y_tmp_list = change_origin(x_tmp_list, y_tmp_list, x_0, y_0)
        save_points_txt(x_tmp_list, y_tmp_list, z_tmp_list, file_path)

        sleep_time = rand()/3+0.1
        sleep(sleep_time)

    print(f'File saved at {file_path} !')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('-a', '--top_left_corner', help="Coordinate (latitude, longitude) of the top left corner of the rectangular elevation map", nargs='+', type=float)
    parser.add_argument('-b', '--bottom_right_corner', help="Coordinate (latitude, longitude) of the bottom right corner of the rectangular elevation map", nargs='+', type=float)

    parser.add_argument('-n_x', '--number_points_x', help="Number of horizontal points of the rectangular map", type=int, default = 50)
    parser.add_argument('-n_y', '--number_points_y', help="Number of vertical points of the rectangular map", type=int, default = 50)

    parser.add_argument('-fn', '--file_name', help="Name of the data .txt file", type=str, default='')
    args = parser.parse_args()

    main(args)
