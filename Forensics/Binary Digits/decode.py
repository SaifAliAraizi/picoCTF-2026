with open("digits.bin", "r") as f:
    bits = f.read().strip()

# Convert every 8 binary digits into one byte
data = bytes(
    int(bits[i:i + 8], 2)
    for i in range(0, len(bits), 8)
    if len(bits[i:i + 8]) == 8
)

with open("recovered.jpg", "wb") as f:
    f.write(data)

print(f"Recovered {len(data)} bytes")
