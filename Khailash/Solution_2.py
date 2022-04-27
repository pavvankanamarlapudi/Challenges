import os
ROOT_DIR = r"C:\Users\pavan\Desktop\main\main"
files_remained=True

# env_dirs={}
# for env in os.listdir(ROOT_DIR):
#     ENV_PATH=os.path.join(ROOT_DIR,env)
#     env_dirs[ENV_PATH]=os.listdir(ENV_PATH)
    
env_dirs = {os.path.join(ROOT_DIR,env):os.listdir(os.path.join(ROOT_DIR,env)) for env in os.listdir(ROOT_DIR)}
    
print([len(y) for y in env_dirs.values()])
        
while files_remained:
    for env,service_files in env_dirs.items():
        if service_files:
            print(os.path.join(env,env_dirs[env].pop(0)))
            files_remained=any([len(y) for y in env_dirs.values()])