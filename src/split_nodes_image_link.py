from extract_markdown import extract_markdown_images, extract_markdown_links

def split_nodes_image(old_nodes):

    new_nodes = []

    for old_node in old_nodes:

        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        original_text = old_node.text

        if not original_text:
            continue

        images = extract_markdown_images(original_text)

        if not images:
            new_nodes.append(old_node)
            continue

        for image in images:
            image_alt = image[0]
            image_link = image[1]
            split_nodes = original_text.split(f"![{image_alt}]({image_link})", 1)

            if len(split_nodes) % 2 == 0:
                raise Exception("ERROR: Invalid Markdown syntax! valid syntax: ![image_alt](image_link)")

            if split_nodes[0] != "":
                new_nodes.append(TextNode(split_nodes[0], TextType.TEXT))

            new_nodes.append(TextNode(image_alt, TextType.IMAGE, image_link))

            original_text = split_nodes[1]

        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))

    return new_nodes
