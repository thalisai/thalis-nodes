import os
from aiohttp import web

from folder_paths import folder_names_and_paths, models_dir
from server import PromptServer

from .utils import download_url

folder_names_and_paths["workflows"] = ([os.path.join(models_dir, "workflows")], [".json", ".yaml"])

routes = web.RouteTableDef()

@routes.post("/models/{folder}/download")
async def download_model(request):
    folder = request.match_info.get("folder", None)
    if folder not in folder_names_and_paths:
        return web.Response(status=404, text="Folder not found")

    json_data = await request.json()
    source_url = json_data.get("source_url", None)
    if source_url is None:
        return web.Response(status=400, text="source_url not found in request")

    model_name = json_data.get("model_name", None)
    if model_name is None:
        return web.Response(status=400, text="model_name not found in request")

    dest_folder = folder_names_and_paths[folder][0][0]
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder, exist_ok=True)

    print("Downloading model", request, folder, source_url, model_name, dest_folder)
    download_url(source_url, os.path.join(dest_folder, model_name))
    return web.Response(status=200, text="Model downloaded")

@routes.get("/workflows/{workflow_name}")
async def get_workflow(request):
    workflow_name = request.match_info.get("workflow_name", None)
    if workflow_name is None:
        return web.Response(status=400, text="Workflow name not found in request")

    print("Getting workflow", request, workflow_name)
    workflow_file = os.path.join(folder_names_and_paths["workflows"][0][0], workflow_name)
    if not os.path.exists(workflow_file):
        return web.Response(status=404, text="Workflow not found")

    with open(workflow_file, "r") as f:
        workflow = f.read()
    return web.Response(status=200, text=workflow)

print("Adding Thalis AI routes")
PromptServer.instance.app.add_routes(routes)
