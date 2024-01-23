import requests
from requests.exceptions import HTTPError

def fetch_tor_exit_nodes(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text.split('\n')
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')

def save_to_file(file_path, nodes):
    with open(file_path, 'w') as file:
        for node in nodes:
            if node:  # Filter out empty lines
                file.write(node + '\n')


def main():
    tor_exit_node_url = "https://check.torproject.org/torbulkexitlist?ip=1.1.1.1"
    exit_nodes= fetch_tor_exit_nodes(tor_exit_node_url)
    file_path = "tor_exit_nodes.txt"
    save_to_file(file_path, exit_nodes)
    print(f"Tor exit nodes have been saved to {file_path}")



if __name__ == "__main__":
    main()