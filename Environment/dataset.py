import pybullet as p
import pybullet_data
import cv2
import numpy as np

# Initialize PyBullet
physicsClient = p.connect(p.DIRECT)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

# Load environment and husky model
planeId = p.loadURDF("plane.urdf")
huskyId = p.loadURDF("husky.urdf", basePosition=[0,0,0])

# Set up camera parameters
width, height, fov = 640, 480, 60
aspect = width / height
near, far = 0.02, 10
view_matrix = p.computeViewMatrixFromYawPitchRoll(cameraTargetPosition=[0,0,0],
                                                  distance=1.0,
                                                  yaw=0,
                                                  pitch=0,
                                                  roll=0,
                                                  upAxisIndex=2)
projection_matrix = p.computeProjectionMatrixFOV(fov, aspect, near, far)

# Generate images
for _ in range(2000):
    # Randomly position the husky
    x, y, z = np.random.uniform(-1, 1, size=3)
    p.resetBasePositionAndOrientation(huskyId, [x, y, z], [0, 0, 0, 1])

    # Capture image
    img_arr = p.getCameraImage(width,
                               height,
                               view_matrix,
                               projection_matrix,
                               shadow=True,
                               lightDirection=[1, 1, 1],
                               renderer=p.ER_BULLET_HARDWARE_OPENGL)
    rgb = img_arr[2]  # RGB data
    depth = img_arr[3]  # depth data

    # Save image
    cv2.imwrite(f'images/husky_{_:04d}.png', rgb)
    cv2.imwrite(f'depth/husky_{_:04d}.png', depth)

p.disconnect()