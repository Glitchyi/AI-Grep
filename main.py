#API_KEY = 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
import re
import sys
from groq import Groq

client = Groq(
    api_key="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",
)




def grep(pattern, file_path):
    """Replicates basic grep functionality."""
    files=[]
    try:
        with open(file_path, 'r') as file:
            for line_number, line in enumerate(file, start=1):
                if re.search(pattern, line):
                    print(f"{line_number}: {line.strip()}")
                    files.append(line.strip())
                    

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
        
    chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "use these words in a shakespeares style sentence" + str(files),
        }
    ],
    model="llama-3.3-70b-versatile",
    )
    print(chat_completion.choices[0].message.content)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python grep.py <pattern> <file>")
    else:
        pattern = sys.argv[1]
        file_path = sys.argv[2]
        grep(pattern, file_path)

