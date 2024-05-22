from textnode import TextNode
import os, shutil
from markdown_blocks import markdown_to_html_node

def copy_static(path, dest):
    files = os.listdir(path)
    for file in files:
        new_path = path + "/" + file
        if os.path.isfile(new_path):
            shutil.copy(new_path, dest)
        else:
            new_dest = dest + "/" + file
            new_path = path + "/" + file
            os.mkdir(new_dest)
            copy_static(new_path, new_dest)

def main():
    absolute_path = os.path.abspath(__file__)
    directory = os.path.dirname(absolute_path)
    parent_dir = os.path.dirname(directory)
    path = parent_dir + "/public"
    shutil.rmtree(path, ignore_errors=True)
    if not os.path.exists(path):
        os.mkdir(path)
    data_path = directory + "/static"
    copy_static(data_path, path)
    source = parent_dir + "/content"
    template = parent_dir + "/template.html"
    dest_path = path
    generate_pages_recursive(source, template, dest_path)
    
    
def extract_title(markdown):
    title = ""
    with open(markdown, "r") as file:
        lines = file.readlines()        
        for line in lines:
            if line.startswith("# "):
                # this strips the trailing newline character (may need to remove the .strip())
                title = line.strip("\n")
                break
    if title == "":
        raise Exception("MISSING HEADING: No <h1> found!")
    return title

def generate_page(from_path, template_path, dest_path):
    title = extract_title(from_path)
    print(f"Generating page: from {from_path} to {dest_path}: using {template_path}.")
    with open(from_path, "r") as data:
        src_mrkdwn = data.read()
        data.close()
    with open(template_path, "r") as data:
        template = data.read()
        data.close()
    html_node = markdown_to_html_node(src_mrkdwn)
    html = html_node.to_html()
    template = template.replace("{{ Content }}", html)
    template = template.replace("{{ Title }}", title)
    with open(dest_path, "w") as data:
        data.write(template)
        data.close()
    
def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    files = os.listdir(dir_path_content)
    for file in files:
        new_path = f"{dir_path_content}/{file}"
        if os.path.isfile(new_path):
            new_des_dir = f"{dest_dir_path}/index.html"
            generate_page(new_path, template_path, new_des_dir)
        else:
            new_content_dir = f"{dir_path_content}/{file}"
            new_des_dir = f"{dest_dir_path}/{file}"
            os.mkdir(new_des_dir)
            generate_pages_recursive(new_content_dir, template_path, new_des_dir)
main()
