import http.client

HOST = 'localhost'  # Replace with the server's hostname or IP address if needed
PORT = 8000

conn = http.client.HTTPConnection(HOST, PORT)
conn.request("GET", "/")  # Send a GET request to the root path

response = conn.getresponse()
print("status:", response.status, response.reason)

data = response.read().decode("utf-8")  # Decode the response data as UTF-8
print("Response:", data)

conn.close()  # Close the connection
