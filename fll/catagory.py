import ollama
import sys

def process_image(model_name, image_path, prompt):
    try:
        messages = [
            {
                'role': 'user',
                'content': prompt,
                'images': [image_path] 
            }
        ]

        response = ollama.chat(
            model=model_name,
            messages=messages
        )

        text_content = response['message']['content']
        print(image_path + ": " + text_content)
        path = image_path + ".txt"
        file = open(path, 'w')
        file.write(text_content)
        file.close()

    except Exception as e:
        print(f"An error occurred: {e}")


model_to_use = 'minicpm-v' 
image_files = [r"C:\Users\Ethan Li\Desktop\website\fll\artifacts\minecraft_pottery_sherd.png", r"C:\Users\Ethan Li\Desktop\website\fll\artifacts\minecraft_pottery_sherd2.png", r"C:\Users\Ethan Li\Desktop\website\fll\artifacts\rock.jpg"]
user_prompt = r'Only respond with single words discribing the image, and seperate with a comma and space! Come up with at least 50 words of the sort' 

for i in range(len(image_files)):
    process_image(model_to_use, image_files[i], user_prompt)

