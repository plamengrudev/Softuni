import os

extensions = {}

path = input()

for file in os.listdir(path):
    current_path = os.path.join(path, file)

    if os.path.isfile(current_path) and file != "report.txt":
        extension = os.path.splitext(file)[1]
        extensions.setdefault(extension, []).append(file)
    elif os.path.isdir(current_path):
        for nested_file in os.listdir(current_path):
            nested_path = os.path.join(current_path, nested_file)

            if os.path.isfile(nested_path):
                extension = os.path.splitext(nested_file)[1]
                extensions.setdefault(extension, []).append(nested_file)

result = []

for extension in sorted(extensions):
    result.append(extension)

    for file in sorted(extensions[extension]):
        result.append(f"---{file}")

with open(os.path.join(path, "report.txt"), "w") as file:
    file.write("\n".join(result))