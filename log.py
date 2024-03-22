import requests

def paste_to_spacebin(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()

        file_extension = file_path.split('.')[-1]
        response = requests.post('https://spaceb.in/api/v1/documents', data={'content': content, 'extension': file_extension})

        if response.status_code == 201:
            document_id = response.json().get('payload', {}).get('id')
            return f'https://spaceb.in/{document_id}'
        else:
            return f"Error: {response.json().get('error')}"

    except Exception as e:
        return f"Error: {e}"

# Example usage:
log_file_path = 'Arctix-log.txt'
result_url = paste_to_spacebin(log_file_path)
print(f"Spacebin URL: {result_url}")
