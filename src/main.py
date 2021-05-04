import sys

msg = "Hello World"
print(msg)

running_in_virtualenv = sys.prefix != sys.base_prefix
print(f"Running in virtual env: {running_in_virtualenv}")


# To setup venv
# 1. $bash: python3 -m venv {name}
# 2. $bash: source {name}/bin/activate

# To install packages
# 3. $bash: pip(3) install PyDrive

# To Deactivate
# 4.  deactivate