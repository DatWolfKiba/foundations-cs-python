MENU_TEXT = """
1. Count Digits
2. Find Max
3. Count Tags
4. Exit
"""
ENTER_CHOICE = "Enter a choice: "
ENTER_INTEGER = "Enter an integer: "
NUMBER_OF_DIGITS = "Number of digits: "
ENTER_LIST = "Enter a list of integers (comma separated): "
MAX_IS = "Max: "
ENTER_TAG = "Enter the HTML tag to count: "
TAG_COUNT = "Tag <{}> count: {}"
EXITING = "Exiting the program..."
INVALID_CHOICE = "Invalid choice, please select again."

HTML_CODE = '''<html>
<head>
<title>My Website</title>
</head>
<body>
<h1>Welcome to my website!</h1>
<p>Here you'll find information about me and my hobbies</p>
<h2>Hobbies</h2>
<ul>
<li>Playing guitar</li>
<li>Reading books</li>
<li>Traveling</li>
<li>Writing cool h1 tags</li>
</ul>
</body>
</html>'''

def count_digits(n):
    if n < 10:
        return 1
    else:
        return 1 + count_digits(n // 10)

def find_max(num_list, n):
    if n == 1:
        return num_list[0]
    else:
        return max(num_list[n-1], find_max(num_list, n-1))

def count_tags(html, tag):
    opening_tag = "<" + tag + ">"
    closing_tag = "</" + tag + ">"
    
    start = html.find(opening_tag)
    
    if start == -1:
        return 0
    
    end = html.find(closing_tag, start)
    
    if end == -1:
        return 0
    
    return 1 + count_tags(html[end + len(closing_tag):], tag)

def display_menu():
    while True:
        print(MENU_TEXT)
        choice = input(ENTER_CHOICE)
        
        if choice == '1':
            num = int(input(ENTER_INTEGER))
            print(NUMBER_OF_DIGITS + " " + str(count_digits(abs(num))))
        
        elif choice == '2':
            num_list = input(ENTER_LIST).split(',')
            num_list = [int(x.strip()) for x in num_list if x.strip().isdigit()]
            if not num_list:
                print(MAX_IS + "0")
            else:
                print(MAX_IS + " " + str(find_max(num_list, len(num_list))))
        
        elif choice == '3':
            tag = input(ENTER_TAG)
            count = count_tags(HTML_CODE, tag)
            print(TAG_COUNT.format(tag, count))
        
        elif choice == '4':
            print(EXITING)
            break
        
        else:
            print(INVALID_CHOICE)

display_menu()
