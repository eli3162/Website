from trimesh import *
import os
def convert_mesh(input_path, output_path, file_name):
    root = os.path.dirname(__file__)
    in_path = os.path.join(root, input_path)
    model = trimesh.load(in_path)
    path_to_glb = os.path.join(output_path, file_name)
    output = os.path.join(root, path_to_glb)
    model.export(output)
    return path_to_glb

root = os.path.dirname(__file__)
