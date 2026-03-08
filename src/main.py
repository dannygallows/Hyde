import os
import shutil

def main():
    copy_static_to_public()
 
def copy_static_to_public(src="./static", dst = "./public"):
    # lets do rm -rf public and cp -r static public with extra steps! (to stay platform independent!)
    if os.path.exists(dst):
        shutil.rmtree(dst)
    os.mkdir(dst)

    static_files = os.listdir(src)

    for file in static_files:
        src_path = os.path.join(src, file)
        dst_path = os.path.join(dst, file)

        if os.path.isfile(src_path):
            shutil.copy(src_path, dst_path)
        else:
            copy_static_to_public(src_path, dst_path)


if __name__ == "__main__":
    main()