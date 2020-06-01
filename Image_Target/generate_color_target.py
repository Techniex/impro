import os
import cv2
import numpy as np
import pandas as pd

def generate_rectangle_color_target(screen_resolution, color_data, print_colorinfo, \
    logosrc=r"./logo/techniex_logo_square_o.png", outpath=r"./images"):
    if not os.path.isdir(outpath):
        os.mkdir(outpath)

    errorval = 0
    try:
        col_data = pd.read_csv(color_data)
    except:
        print("Error 1: Unable to read file.")
        errorval = 1
    color_data = os.path.basename(color_data)
    if not ('Red' in col_data.select_dtypes(include='int64')\
            and 'Green' in col_data.select_dtypes(include='int64')\
            and 'Blue' in col_data.select_dtypes(include='int64')\
        and 'Name' in col_data.select_dtypes(include='object')\
        and 'Column' in col_data.select_dtypes(include='int64')\
        and 'Row' in col_data.select_dtypes(include='int64')\
        and 'Pallet' in col_data.select_dtypes(include='object')):
        print("Error 2: All columns not available in supplied data file.")
        errorval = 2
    elif np.max(col_data.loc[:, ['Red', 'Green', 'Blue']].values) > 255:
        print("Error 3: Color values greater than 8 bit.")
        errorval = 3
    elif len(list(set(col_data['Pallet'].values))) != 1:
        print("Error 4: Irregular Pallet size")
        errorval = 4
    else:
        if list(set(col_data['Pallet'].values))[0] == 'square':
            square_pallet = True
        else:
            square_pallet = False
        pallet_distribution = np.array([max(col_data['Column'].values) + 1, \
            max(col_data['Row'].values) + 1])
        screen_resolution = np.array(screen_resolution)
        pgap_ratio = 1/5
        print("Info: Valid color file.")
        right_align_text = "<https://techniex.com>"

    if errorval == 0:
        area_distribution = pallet_distribution + (pallet_distribution + 3)*pgap_ratio
        limiting_side = screen_resolution/area_distribution
        pgap = int(min(limiting_side)*pgap_ratio)
        if pgap > min(screen_resolution)/30:
            pgap = int(min(screen_resolution)/30)
        if square_pallet == True:
            horizontal_pallet_size = int(min(limiting_side))
            vertical_pallet_size = int(min(limiting_side))
        else:
            horizontal_pallet_size = int((screen_resolution[0] - \
                (pgap*(pallet_distribution[0]+3)))/pallet_distribution[0])
            vertical_pallet_size = int((screen_resolution[1] - \
                (pgap*(pallet_distribution[1]+3)))/pallet_distribution[1])
        image_size_horizontal = (horizontal_pallet_size * pallet_distribution[0]) + \
            (pgap *(pallet_distribution[0]+3))
        image_size_vertical = (vertical_pallet_size * pallet_distribution[1]) + \
            (pgap *(pallet_distribution[1]+3))

        img_base = np.uint8(np.zeros((image_size_vertical, image_size_horizontal, 3)))

        font = cv2.FONT_HERSHEY_COMPLEX
        if pgap < 35:
            font_scale = 0.5
            font_scale_s = 0.25
            thickness = 1
            logosize = (pgap-5, pgap-5)
        elif pgap >= 35 and pgap < 50:
            font_scale = 0.75
            font_scale_s = 0.5
            thickness = 1
            logosize = (pgap-10, pgap-10)
        elif pgap >= 50 and pgap < 70:
            font_scale = 1
            font_scale_s = 0.65
            thickness = 2
            logosize = (pgap-15, pgap-15)
        else:
            font_scale = 2
            font_scale_s = 1
            thickness = 3
            logosize = (pgap-20, pgap-20)
        color = (255, 255, 255)

        chart_name = color_data.replace('.csv', '').replace('_', ' ').title()

        xdiff = int(cv2.getTextSize('+', font, font_scale, thickness)[0][0]/2)
        ydiff = int(cv2.getTextSize('+', font, font_scale, thickness)[0][1]/2)
        right_align = int(cv2.getTextSize(right_align_text, font, font_scale_s, thickness)[0][0])

        top_left = (pgap-xdiff, pgap+ydiff)
        top_right = (image_size_horizontal-pgap-xdiff, pgap+ydiff)
        bottom_left = (pgap-xdiff, image_size_vertical-pgap+ydiff)
        bottom_right = (image_size_horizontal-pgap-xdiff, image_size_vertical-pgap+ydiff)
        top_name = (pgap, pgap-ydiff)
        bottom_right_align = (image_size_horizontal-pgap-right_align, image_size_vertical-ydiff)

        img_base = cv2.putText(img_base, '+', \
            top_left, font, font_scale, color, thickness, cv2.LINE_AA)
        img_base = cv2.putText(img_base, '+', \
            top_right, font, font_scale, color, thickness, cv2.LINE_AA)
        img_base = cv2.putText(img_base, '+', \
            bottom_left, font, font_scale, color, thickness, cv2.LINE_AA)
        img_base = cv2.putText(img_base, '+', \
            bottom_right, font, font_scale, color, thickness, cv2.LINE_AA)
        img_base = cv2.putText(img_base, chart_name, \
            top_name, font, font_scale, color, thickness, cv2.LINE_AA)
        img_base = cv2.putText(img_base, right_align_text, \
            bottom_right_align, font, font_scale_s, color, thickness, cv2.LINE_AA)

        logo = cv2.imread(logosrc)
        logo = cv2.resize(logo, logosize)
        img_base[(image_size_vertical-pgap):(image_size_vertical-pgap +logosize[0]), \
            (ydiff + pgap):(ydiff + pgap)+logosize[0], :] = logo

        for itr in col_data.index:
            r_init = 2*pgap + (pgap + vertical_pallet_size) * col_data['Row'][itr]
            r_end = pgap + (pgap + vertical_pallet_size) * (col_data['Row'][itr] + 1)
            c_init = 2*pgap + (pgap + horizontal_pallet_size) * col_data['Column'][itr]
            c_end = pgap + (pgap + horizontal_pallet_size) * (col_data['Column'][itr] + 1)
            img_base[r_init:r_end, c_init:c_end, 2] = np.uint8(col_data['Red'][itr])
            img_base[r_init:r_end, c_init:c_end, 1] = np.uint8(col_data['Green'][itr])
            img_base[r_init:r_end, c_init:c_end, 0] = np.uint8(col_data['Blue'][itr])
            if print_colorinfo:
                color_text = "%s : #%02X%02X%02X"%(col_data['Name'][itr], \
                    col_data['Red'][itr], col_data['Green'][itr], col_data['Blue'][itr])
                diff = int(cv2.getTextSize(color_text, font, font_scale_s, thickness)[0][1]) + 5
                img_base = cv2.putText(img_base, color_text, \
                    (c_init, r_end + diff), font, font_scale_s, color, thickness, cv2.LINE_AA)

        if print_colorinfo:
            extn = "_ci"
        else:
            extn = ""
        image_name = color_data.replace(".csv", "_%dx%d%s.png"\
            %(screen_resolution[0], screen_resolution[1], extn))
        image_path = outpath + '\\' + image_name
        cv2.imwrite(image_path, img_base)

    return errorval
