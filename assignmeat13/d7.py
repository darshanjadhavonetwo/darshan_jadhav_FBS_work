my_dict = {"name": "Alice","age": 25,"city": "Mumbai"}
print("Original Dictionary:", my_dict)
key_to_remove = input("Enter the key you want to remove: ")
if key_to_remove in my_dict:
    del my_dict[key_to_remove]
    print(f"Key '{key_to_remove}' removed successfully.")
else:
    print(f"Key '{key_to_remove}' not found in the dictionary.")

print("Updated Dictionary:", my_dict)
