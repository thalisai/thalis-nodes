# Thalis AI Stack: ComfyUI Nodes

[Please see the Thalis AI stack repository for more information.](https://github.com/thalisai/thalis-stack)

## Stack

The Thalis AI stack is an all-in-one platform for interactive original characters using open-source generative AI tools.
It offers multi-modal interactions, including text, audio, and image generation, from a single web interface. It can be
self-hosted, guaranteeing privacy and security, or run in the cloud on most common GPU providers.

The Thalis AI stack is designed with privacy and security at its core, avoiding cloud services in favor of self-hosted
and open-source tools to ensure your data remains under your control at all times.

## Contents

- [Thalis AI Stack: ComfyUI Nodes](#thalis-ai-stack-comfyui-nodes)
  - [Stack](#stack)
  - [Contents](#contents)
  - [Overview](#overview)
    - [Endpoints](#endpoints)
  - [License](#license)

## Overview

This repository contains custom nodes for ComfyUI, which allows the Thalis AI manager to remotely control the ComfyUI
server.

This does not add any nodes that can be used in ComfyUI workflows yet, but it adds some endpoints to the web server
which allow the manager to:

- download new models and workflows
- fetch workflows from the server

### Endpoints

- `POST /models/{folder}/download`
  - takes a `model_name` and `source_url` in the request body (`folder` is in the path to match original ComfyUI endpoints)
  - downloads the model from the `source_url` and saves it to the `folder` directory as `model_name`
- `GET /workflows/{name}`
  - takes a `name` in the path
  - fetches the workflow with the given `name` from the server

## License

This repository is licensed under the MIT license. Please see the [LICENSE](LICENSE) file for more information.
