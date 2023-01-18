import textwrap

sample_text = "This is some sample text that I want to wrap based on word boundaries."
words_per_line = int(input("Enter the number of words per line: "))

# Split the text into words
words = sample_text.split()

# Initialize the counter
counter = 0

# Initialize the list to hold the wrapped text
wrapped_text = []

# Iterate over the words
for word in words:
    if counter % words_per_line == 0:
        wrapped_text.append(word)
    else:
        wrapped_text[-1] += " " + word
    counter += 1

print("Wrapped Text:\n")
print("\n".join(wrapped_text))

