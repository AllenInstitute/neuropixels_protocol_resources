# define roll, pitch, and yaw transforms

import numpy as np
from scipy.optimize import leastsq

def roll(inputMat, g): 
    
    """
    Rotate an input matrix around the X axis (bank angle)
    
    Parameters
    ----------
    inputMat - np.ndarray (3 x 3)
        original rotation matrix
    g - float
        rotation angle (in radians)
    
    
    Returns
    -------
    outputMat - np.ndarray (3 x 3)
        rotated matrix
    
    """
    
    rollMat = np.array([[1, 0,         0],
               [0, np.cos(g), -np.sin(g)],
               [0, np.sin(g), np.cos(g)]])
    return np.dot(inputMat,rollMat)


def pitch(inputMat, b):
    
    """
    Rotate an input matrix around the Y axis (elevation angle)
    
    Parameters
    ----------
    inputMat - np.ndarray (3 x 3)
        original rotation matrix
    b - float
        rotation angle (in radians)
    
    
    Returns
    -------
    outputMat - np.ndarray (3 x 3)
        rotated matrix
    
    """
    
    pitchMat = np.array([[np.cos(b), 0, np.sin(b)],
               [0, 1, 0],
               [-np.sin(b), 0, np.cos(b)]])
    return np.dot(inputMat,pitchMat)


def yaw(inputMat, a):
    
    """
    Rotate an input matrix around the Z axis (heading angle)
    
    Parameters
    ----------
    inputMat - np.ndarray (3 x 3)
        original rotation matrix
    a - float
        rotation angle (in radians)
    
    
    Returns
    -------
    outputMat - np.ndarray (3 x 3)
        rotated matrix
    
    """
    
    yawMat = np.array([[np.cos(a), -np.sin(a), 0],
               [np.sin(a), np.cos(a), 0],
               [0, 0, 1]])
    return np.dot(inputMat,yawMat)


def extractAngles(mat):
    
    """
    Converts a rotation matrix to a set of 3 angles
    
    Parameters
    ----------
    mat - np.ndarray (3 x 3)
        a rotation matrix
    
    Returns
    -------
    x - float
        bank angle
    y - float
        elevation angle
    z - float
        heading angle
    
    """
    
    x = np.arctan2(mat[2,1],mat[2,2])
    y = np.arctan2(-mat[2,0], np.sqrt(pow(mat[2,1],2)+ pow(mat[2,2],2)))
    z = np.arctan2(mat[1,0],mat[0,0])
    
    return x, y, z


def combineAngles(x,y,z):
    
    """
    Combines a set of 3 angles into a rotation matrix
    
    Parameters
    ----------
    x - float
        bank angle
    y - float
        elevation angle
    z - float
        heading angle
    
    Returns
    -------
    mat - np.ndarray (3 x 3)
        a rotation matrix
    
    """
    
    eye = np.identity(3)
    R = roll(pitch(yaw(eye,z),y),x)
    
    return R


def func(x, global_pts, measured_pts):
    
    """
    Error function for least squares optimization
    
    Parameters
    ----------
    x - np.ndarray (6 x 0)
        3 rotations and 3 offsets in a 1-D matrix
    global_pts - np.ndarray (M x 3)
        points in global coordinate space
        M = number of calibration points
    measured_pts - np.ndarray (M x 3)
        points in local coordinate space
        M = number of calibration points
    
    Returns
    -------
    error_values - np.ndarray (15 x 0)
    
    """
    
    R = combineAngles(x[2], x[1], x[0])
    origin = np.array([x[3], x[4], x[5]]).T
    
    M = global_pts.shape[0]

    error_values = np.zeros((M * 3,))

    for i in range(M):
        global_pt = global_pts[i,:].T
        measured_pt = measured_pts[i,:].T - np.array([3,3,3])
        local_pt = np.dot(global_pt + origin, R)

        error_values[0+i*3:3+i*3] = local_pt - measured_pt
        
    return error_values


def fit_params(global_coords, local_coords):
    
    """
    Finds the optimal rotation and offset for a set of 
    calibration points for one probe
    
    Parameters
    ----------
    global_coords : np.ndarray (M x 3)
      Global (reticle) XYZ coordinates for each calibration point
      M = number of calibration points
     
    local_coords : np.ndarray (M x 3)
      Local (motor) XYZ coordinates for each calibration point
      M = number of calibration points
    
    Returns
    -------
    origin - np.ndarray (3 x 0)
      3D offset of the origin of the probe's local coordinate space
    
    R - np.ndarray (3 x 3)
      3D rotation matrix that defines the orientation of the probe's
      local coordinate space
    
    """

    x0 = np.array([0,0,0,0,0,0])
    res = leastsq(func, x0, args=(global_coords, local_coords))
    rez = res[0]
    R = combineAngles(rez[2],rez[1],rez[0])
    origin = rez[3:]

    return origin, R


