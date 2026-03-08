import os
import shutil
from markdown_to_html_node import markdown_to_html_node
from extract_markdown import extract_title


def main():
    copy_static_to_public()
    from_path = "content/index.md"
    template_path = "template.html"
    dest_path = "public/index.html"
    generate_page(from_path, template_path, dest_path)


def copy_static_to_public(src="./static", dst = "./public"):
    first_run = True
    if os.path.exists(dst) and first_run:
        shutil.rmtree(dst)
        first_run = False
    os.mkdir(dst)
    static_files = os.listdir(src)
    for file in static_files:
        src_path = os.path.join(src, file)
        dst_path = os.path.join(dst, file)
        if os.path.isfile(src_path):
            shutil.copy(src_path, dst_path)
        else:
            copy_static_to_public(src_path, dst_path)


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as f:
        from_data = f.read()
    with open(template_path) as f:
        template_data = f.read()
    md_to_html = markdown_to_html_node(from_data).to_html()
    page_title = extract_title(from_data)
    html_page = template_data.replace("{{ Title }}", page_title).replace("{{ Content }}", md_to_html)
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, "w") as f:
        f.write(html_page)



if __name__ == "__main__":
    main()