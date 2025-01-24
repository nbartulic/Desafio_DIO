import json
import os

def convert_labelme_to_yolo(json_path, image_width, image_height):
    with open(json_path, 'r') as f:
        data = json.load(f)

    yolo_annotations = []
    for shape in data['shapes']:
        label = shape['label']
        points = shape['points']
        
        x_min = min(points[0][0], points[1][0])
        y_min = min(points[0][1], points[1][1])
        x_max = max(points[0][0], points[1][0])
        y_max = max(points[0][1], points[1][1])

        x_center = (x_min + x_max) / 2 / image_width
        y_center = (y_min + y_max) / 2 / image_height
        width = (x_max - x_min) / image_width
        height = (y_max - y_min) / image_height

        yolo_annotations.append(f"{label} {x_center} {y_center} {width} {height}")

    yolo_filename = json_path.replace(".json", ".txt")
    with open(yolo_filename, 'w') as f:
        f.write("\n".join(yolo_annotations))

    print(f"Converted {json_path} to {yolo_filename}")

# Convert all JSON files
for file in os.listdir("annotations"):
    if file.endswith(".json"):
        convert_labelme_to_yolo(f"annotations/{file}", 1280, 720)  # Ajuste o tamanho conforme necessário
