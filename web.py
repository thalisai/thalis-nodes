import os

from folder_paths import folder_names_and_paths, models_dir
from server import PromptServer

folder_names_and_paths["workflows"] = ([os.path.join(models_dir, "workflows")], [".json", ".yaml"])

PromptServer.instance.routes.post("/models/{folder}/download")
async def download_model(request, folder):
    print("Downloading model", request, folder)
