#
# Example of how to calibrate probes to a reticle
#
# All values are placeholders, and should be changed for your specific use case
#
# 

import numpy as np

def getCalibrationInfo():
    
  """
  The global and local coordinates at which multiple probes 
  touch a calibration reticle.
  
  Returns
  -------
  
  calibrationInfo : dict with fields:
  
      <'probe_name'> : dict with fields:
      
          'global_coords' : np.ndarray (M x 3)
              Global (reticle) XYZ coordinates for each calibration point (in mm)
              M = number of calibration points

          'local_coords' : np.ndarray (M x 3)
              Local (motor) XYZ coordinates for each calibration point (in mm)
              M = number of calibration points
      
  """

  cal = { }
    
  cal['probeA'] = { }
    
  # probe A
  cal['probeA']['global_coords'] = \
    np.array([[0,0,0],
              [-1,0,0],
              [-2,0,0],
              [0,-1,0],
              [0,-2,0]])*0.8
   
  cal['probeA']['local_coords'] = \
      np.array([[1795.0, 4574.0, 3167.5],
                [1146.0, 3923.0, 3057.0],
                [879.0, 3160.0, 2991.0],
                [2461.0, 4182.5, 2900.0],
                [2844.0, 3811.5, 2679.0]])/1000.
    
  cal['probeB'] = { }
    
  cal['probeB']['global_coords'] = \
    np.array([[0,0,0],
              [-1,0,0],
              [-2,0,0],
              [0,-1,0],
              [0,-2,0]])*0.8

  cal['probeB']['local_coords'] = \
    np.array([[1922.5, 2305.5, 3345.0],
               [2339.5, 1518.5, 3107.0],
               [2674.0, 867.0, 2862.0],
               [2606.5, 2643.0, 3338.5],
               [3307.0, 3002.0, 3286.5]])/1000.

  cal['probeC'] = { }

  cal['probeC']['global_coords'] = \
    np.array([[0,0,0],
              [-1,0,0],
              [-2,0,0],
              [0,1,0],
              [0,2,0]])*0.8
   
  cal['probeC']['local_coords'] = \
    np.array([[2534.0, 3010.5, 3286.0],
              [3355.0, 3010.5, 3012.0],
              [4168.0, 3010.5, 2948.0],
              [2546.0, 2214.5, 3035.5],
              [2522.5, 1429.0, 2780.5]])/1000.

  cal['probeD'] = { }

  cal['probeD']['global_coords'] = \
      np.array([[0,0,0],
               [1,0,0],
               [2,0,0],
               [0,1,0],
               [0,2,0]])*0.8
   
  cal['probeD']['local_coords'] = \
    np.array([[2759.0, 4455.5, 3303.0],
              [2342.0, 3763.5, 3238.5],
              [1920.5, 3143.0, 3180.0],
              [3394.5, 4103.0, 3080.5],
              [4024.5, 3771.0, 2802.0]])/1000.

  cal['probeE'] = { }

  cal['probeE']['global_coords'] = \
    np.array([[0,0,0],
              [1,0,0],
              [2,0,0],
              [0,1,0],
              [0,2,0]])*0.8
   
  cal['probeE']['local_coords'] = \
    np.array([[1511.0, 4536.5, 3101.5],
              [1851.0, 3883.0, 2795.5],
              [2254.0, 3210.0, 2522.0],
              [2126.0, 5041.0, 2989.5],
              [2848.5, 5400.5, 2969.5]])/1000.

  cal['probeF'] = { }

  cal['probeF']['global_coords'] = \
     np.array([[0,0,0],
               [1,0,0],
               [2,0,0],
               [0,-1,0],
               [0,-2,0]])*0.8
   
  cal['probeF']['local_coords'] = \
    np.array([[1549.5, 4934.0, 3286.0],
              [2326.5, 4939.5, 3028.0],
              [3143.5, 4922.5, 2842.0],
              [1498.5, 4141.5, 3050.0],
              [1485.0, 3416.0, 2769.0]])/1000.

  return cal


