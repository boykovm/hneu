from stegano import lsb

# Path to the executable file
executable_path = "qwe.lnk"  # Replace with your executable's path

# Load the image
image_path = "tree-736885_1280.jpg"
image = lsb.hide(image_path, open(executable_path, "rb").read())

# Save the modified image (with the embedded executable)
image.save("image_with_secret.jpg")
