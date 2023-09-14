# Email-Slicer-with-Python # 
# Email input #

email = input("Enter Your Email: ").strip()

username = email[:email.index('@')]
domain = email[email.index('@') + 1:]

print(f"Your username is {username} & domain is {domain}")


# Email slicer #

def email_slicer(email):
    username, _, domain = email.strip().partition("@")
    return f"Your username is {username} & domain is {domain}"
user_input = input("Enter Your Email: ")
print(email_slicer(user_input))



email_address = input(“enter your email address”).strip()
new = email_address.partition(“@”)
print(f”user name {new[0] } and {new[-1]}”)


email = input("Enter Your Email: ").strip()
username = email[:email.index("@")]
domain_name = email[email.index("@")+1:]
format_ = (f"Your user name is '{username}' and your domain is '{domain_name}'")
print(format_)


# Get user email address
email = input("What is your email address?: ").strip()

# Slice out the user name
user_name = email[:email.index("@")]

# Slice the domain name
domain_name = email[email.index("@")+1:]

# Format message
output = "Your username is '{}' and your domain name is '{}'".format(user_name,domain_name)

# Display output message
print(output)







