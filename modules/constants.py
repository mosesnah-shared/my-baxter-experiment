import numpy as np

class Constants:
    PROJECT_NAME            = '[M3X] Baxter'
    VERSION                 = '2.0.0'
    UPDATE_DATE             = '2022.08.18'
    AUTHOR_GITHUB           = 'mosesnah-shared'
    AUTHOR_FULL_NAME        = 'Moses C. Nah'
    DESCRIPTION             = "mujoco-py scripts for running a Baxter simulation"
    URL                     = 'https://github.com/mosesnah-shared/baxter-mujoco-playground',
    AUTHOR_EMAIL            = 'mosesnah@mit.edu', 'mosesnah@naver.com'

    # =============================================================== #
    # Constant variables for running the simulation
    # =============================================================== #
    
    # The module directory which contains all python modules.
    MODULE_DIR     = "./modules/"

    # The model directory which contains all the xml model files.
    MODEL_DIR     = "./models/"

    # The directory which saves all the simulation results
    SAVE_DIR      = "./results/"

    # The directory which saves all the temporary data
    TMP_DIR       = "./tmp/"