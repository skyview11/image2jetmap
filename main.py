import numpy as np
import cv2
def depth2jet_bar(depth_image:np.ndarry, depth_min=0, depth_max=50):
    """read depth map and convert to jetbar image

    Args:
        depth_image (np.ndarray): depth image (W, H)
        depth_min (int, optional): min depth(red). Defaults to 0.
        depth_max (int, optional): max_depth(blue). Defaults to 50.

    Returns:
        jet colormap (np.ndarray): W * H * 3
    """
    # Apply the 'jet' colormap and invert the colors
    # Normalize depth values to 0-1 range
    depth_norm = (depth_image - depth_min) / (depth_max-depth_min)
    
    # Create jet colormap function (R,G,B values based on normalized input)
    jet_b = np.clip(1.5 - np.abs(4 * depth_norm - 3), 0, 1)
    jet_g = np.clip(1.5 - np.abs(4 * depth_norm - 2), 0, 1) 
    jet_r = np.clip(1.5 - np.abs(4 * depth_norm - 1), 0, 1)
    
    # Stack RGB channels and convert to uint8
    jet_colormap = np.stack([jet_b, jet_g, jet_r], axis=-1)
    jet_colormap = (jet_colormap * 255).astype(np.uint8)
    
    return jet_colormap

if __name__ == "__main__":
    demo_depth = np.array([np.arange(640)//640*255 for _ in range(360)]).T
    cv2.imwrite("demo.jpg", depth2jet_bar(demo_depth, depth_min=0, depth_max=255))
    