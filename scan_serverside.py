import webbrowser, os, sys, shutil, asyncio, time
async def main():
    try:
        os.remove(r"C:\Users\Public\images\captured_img1.jpg")
        os.remove(r"C:\Users\Public\images\captured_img2.jpg")
        os.remove(r"C:\Users\Public\images\captured_img6.jpg")
        os.remove(r"C:\Users\Public\images\captured_img7.jpg")
        os.remove(r"C:\Users\Public\images\captured_img10.jpg")
        os.remove(r"C:\Users\Public\images\captured_img11.jpg")
    except FileNotFoundError:
        pass
    time.sleep(1)
    webbrowser.open("http://192.168.29.152:5000/images/captured_img1.jpg")
    webbrowser.open("http://192.168.29.152:5000/images/captured_img2.jpg")
    webbrowser.open("http://192.168.29.152:5000/images/captured_img3.jpg")
    webbrowser.open("http://192.168.29.152:5000/images/captured_img4.jpg")
    webbrowser.open("http://192.168.29.152:5000/images/captured_img5.jpg")
    webbrowser.open("http://192.168.29.152:5000/images/captured_img6.jpg")
    webbrowser.open("http://192.168.29.152:5000/images/captured_img7.jpg")
    webbrowser.open("http://192.168.29.152:5000/images/captured_img8.jpg")
    webbrowser.open("http://192.168.29.152:5000/images/captured_img9.jpg")
    webbrowser.open("http://192.168.29.152:5000/images/captured_img10.jpg")
    webbrowser.open("http://192.168.29.152:5000/images/captured_img11.jpg")
    time.sleep(10)
    shutil.move(r'C:\Users\Ethan Li\Downloads\captured_img1.jpg', r"C:\Users\Public\images\captured_img1.jpg")
    shutil.move(r'C:\Users\Ethan Li\Downloads\captured_img2.jpg', r"C:\Users\Public\images\captured_img2.jpg")
    shutil.move(r'C:\Users\Ethan Li\Downloads\captured_img3.jpg', r"C:\Users\Public\images\captured_img3.jpg")
    shutil.move(r'C:\Users\Ethan Li\Downloads\captured_img4.jpg', r"C:\Users\Public\images\captured_img4.jpg")
    shutil.move(r'C:\Users\Ethan Li\Downloads\captured_img5.jpg', r"C:\Users\Public\images\captured_img5.jpg")
    shutil.move(r'C:\Users\Ethan Li\Downloads\captured_img6.jpg', r"C:\Users\Public\images\captured_img6.jpg")
    shutil.move(r'C:\Users\Ethan Li\Downloads\captured_img7.jpg', r"C:\Users\Public\images\captured_img7.jpg")
    shutil.move(r'C:\Users\Ethan Li\Downloads\captured_img8.jpg', r"C:\Users\Public\images\captured_img8.jpg")
    shutil.move(r'C:\Users\Ethan Li\Downloads\captured_img9.jpg', r"C:\Users\Public\images\captured_img9.jpg")
    shutil.move(r'C:\Users\Ethan Li\Downloads\captured_img10.jpg', r"C:\Users\Public\images\captured_img10.jpg")
    shutil.move(r'C:\Users\Ethan Li\Downloads\captured_img11.jpg', r"C:\Users\Public\images\captured_img11.jpg")
    time.sleep(10)
    try:
        os.remove(r"C:\Users\Ethan Li\Downloads\captured_img1.jpg")
        os.remove(r"C:\Users\Ethan Li\Downloads\captured_img2.jpg")
        os.remove(r"C:\Users\Ethan Li\Downloads\captured_img3.jpg")
        os.remove(r"C:\Users\Ethan Li\Downloads\captured_img4.jpg")
        os.remove(r"C:\Users\Ethan Li\Downloads\captured_img5.jpg")
        os.remove(r"C:\Users\Ethan Li\Downloads\captured_img6.jpg")
        os.remove(r"C:\Users\Ethan Li\Downloads\captured_img7.jpg")
        os.remove(r"C:\Users\Ethan Li\Downloads\captured_img8.jpg")
        os.remove(r"C:\Users\Ethan Li\Downloads\captured_img9.jpg")
        os.remove(r"C:\Users\Ethan Li\Downloads\captured_img10.jpg")
        os.remove(r"C:\Users\Ethan Li\Downloads\captured_img11.jpg")
    except FileNotFoundError:
        pass

asyncio.run(main())

os.system(r'"C:\Users\Public\Meshroom2025\Meshroom2025\meshroom_compute.exe" "C:\Users\Public\scanner.mg"')

while not os.path.exists(r"C:\Users\Public\scanner\texturedMesh.obj"):
    pass

import trimesh
from trimesh.visual import resolvers

def convert_obj_to_glb(obj_path, mtl_path, texture_path, output_glb_path):
    """
    Load an OBJ with specified MTL and PNG texture paths, and export to GLB with embedded texture.
    """

    # Build a resolver from the folder where the MTL and texture live
    # Put mtl and texture folder location(s) here:
    base_resolver = resolvers.FilePathResolver('.')
    base_resolver = base_resolver.namespaced(mtl_path.rsplit('/', 1)[0])
    base_resolver = base_resolver.namespaced(texture_path.rsplit('/', 1)[0])

    # Load the scene using trimesh.load with the custom resolver
    scene = trimesh.load(obj_path, resolver=base_resolver, force='scene')

    # Export to GLB bytes (binary glTF with embedded textures)
    glb_bytes = scene.export(file_type='glb')

    # Write the GLB file
    with open(output_glb_path, 'wb') as f:
        f.write(glb_bytes)

    print(f"Converted '{obj_path}' + '{mtl_path}' + '{texture_path}' → '{output_glb_path}'")


if __name__ == "__main__":
    # Replace these with your actual paths
    input_obj     = r"C:\Users\Public\scanner\texturedMesh.obj"
    input_mtl     = r"C:\Users\Public\scanner\texturedMesh.mtl"
    input_texture = r"C:\Users\Public\Scans\texture1001.png"
    output_glb    = r"C:\Users\Ethan Li\OneDrive\Documents\website\fll\artifacts\scan.glb"

    convert_obj_to_glb(input_obj, input_mtl, input_texture, output_glb)
