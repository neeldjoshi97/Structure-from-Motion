
# import necessary packages
import gym
import numpy as np
import metadrive
import cv2 as cv

def show_plot(img_to_show):

    cv.namedWindow("Show Image", cv.WINDOW_NORMAL)
    cv.imshow("Show Image", img_to_show)
    k = cv.waitKey()
    cv.destroyAllWindows()

# Setup road scenario
config_dict =  dict(use_render = False)  #initialise config dictionary
config_dict["map_config"] = {"type": "block_sequence", "config": "OCOC", "lane_num": 3}

# Setup Vision-Based Observation
config_dict["offscreen_render"] = True
config_dict["vehicle_config"] = {"image_source": "rgb_camera"}
# config_dict["vehicle_config"]["image_source"] = "rgb_camera"
config_dict["vehicle_config"]["rgb_camera"] = (100, 100)


# initialise the env
env = gym.make("MetaDrive-validation-v0", config = config_dict)

env.reset()

for i in range(1000):
    obs, reward, done, info = env.step(env.action_space.sample())
    img = obs['image']
    show_plot(img)
    print(np.max(img))
    print(np.sum(img) / 1e4)
    env.render()
    if done:
        env.reset()
