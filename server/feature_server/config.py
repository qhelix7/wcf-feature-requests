import os
import dotenv


_env = dotenv.dotenv_values()
locals().update(_env)

APP_DIR = os.path.dirname(__file__)
ROOT_DIR = os.path.dirname(os.path.dirname(APP_DIR))
# DIST_DIR = os.path.join(ROOT_DIR, 'app', 'public')

if not os.path.exists(DIST_DIR):
    raise RuntimeError(f'DIST_DIR not found: {DIST_DIR}')
