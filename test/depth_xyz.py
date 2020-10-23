def d2xyz(pix_x,pix_y):
    cam_pts_x = np.multiply(pix_x-camera_intrinsics[0][2],depth/camera_intrinsics[0][0])
    cam_pts_y = np.multiply(pix_y-camera_intrinsics[1][2],depth/camera_intrinsics[1][1])
    cam_pts_z = depth