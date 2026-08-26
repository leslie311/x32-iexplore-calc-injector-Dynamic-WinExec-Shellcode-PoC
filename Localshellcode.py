shellcode = "cmd.exe /c start https://www.youtube.com"
count = len(shellcode) // 4
a = int(count)

    # Check if a is an integer
if isinstance(a, int):
    print(f"{shellcode} can be divided by 4")
else:
    print(f"{shellcode} cannot be divided by 4")

esp = hex(a) # The number that u should  add in esp
print("##########################################################")
print("esp=" + esp)
print("##########################################################")
output_list = []
for i in range(a):
    out = ""
    for byte in shellcode[i*4:i*4+4]:  
        out += int(ord(byte)).to_bytes(1, 'big').hex()  
    output_list.append("68" + out)

for line in reversed(output_list):
    print(line)
