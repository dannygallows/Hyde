import os
import shutil
import sys
from markdown_to_html_node import markdown_to_html_node
from extract_markdown import extract_title


def main():
    if os.path.exists("./docs"):
        shutil.rmtree("./docs")
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = "/"
    copy_static_to_docs("./static", "./docs")
    generate_pages_recursive("content", "template.html", "./docs", basepath)


def copy_static_to_docs(src, dst):
    os.mkdir(dst)
    static_files = os.listdir(src)
    for file in static_files:
        src_path = os.path.join(src, file)
        dst_path = os.path.join(dst, file)
        if os.path.isfile(src_path):
            shutil.copy(src_path, dst_path)
        else:
            copy_static_to_docs(src_path, dst_path)


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



def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    os.makedirs(dest_dir_path, exist_ok=True)
    content_files = os.listdir(dir_path_content)
    for file in content_files:
        from_path = os.path.join(dir_path_content, file)
        dest_path = os.path.join(dest_dir_path, file)
        if os.path.isfile(from_path):
            if from_path.endswith(".md"):
                dest_path = dest_path.replace(".md", ".html")
                with open(from_path) as f:
                    markdown = f.read()
                with open(template_path) as f:
                    template = f.read()
                md_to_html = markdown_to_html_node(markdown).to_html()
                page_title = extract_title(markdown)
                html_page = template.replace("{{ Title }}", page_title).replace("{{ Content }}", md_to_html)
                html_page = html_page.replace('href="/', f'href="{basepath}').replace('src="/', f'src="{basepath}')
                with open(dest_path, "w") as f:
                    f.write(html_page)
        else:
            generate_pages_recursive(from_path, template_path, dest_path, basepath)


if __name__ == "__main__":
    main()
