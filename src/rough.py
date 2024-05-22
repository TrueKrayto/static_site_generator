path = "sample_html.txt"

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

x = extract_title(path)

print(x)