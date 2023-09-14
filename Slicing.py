# Email-Slicer-with-Python # 
# Email input #
# different methods to achieve the same result #

## 1) Using String Indexing

email = input("Enter Your Email: ").strip()
username = email[:email.index('@')]
domain = email[email.index('@') + 1:]
print(f"Your username is {username} & domain is {domain}")

## 2) Using the partition Method


def email_slicer(email):
    username, _, domain = email.strip().partition("@")
    return f"Your username is {username} & domain is {domain}"
user_input = input("Enter Your Email: ")
print(email_slicer(user_input))


## 3) Using the partition Method (Alternative Syntax):

email_address = input(“enter your email address”).strip()
new = email_address.partition(“@”)
print(f”user name {new[0] } and {new[-1]}”)

## 4) Using String Slicing and format Method:


email = input("Enter Your Email: ").strip()
username = email[:email.index("@")]
domain_name = email[email.index("@")+1:]
format_ = (f"Your user name is '{username}' and your domain is '{domain_name}'")
print(format_)

## 5) Using String Slicing and Concatenation:


email = input("What is your email address?: ").strip()
user_name = email[:email.index("@")]
domain_name = email[email.index("@") + 1:]
output = "Your username is '{}' and your domain name is '{}'".format(user_name, domain_name)
print(output)





