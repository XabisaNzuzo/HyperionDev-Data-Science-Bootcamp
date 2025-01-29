# Read the movie.xml file.
# List all child tags of the movie element.
# Print the movie descriptions.
# Find the number of movies that are favourites and ones that are not.

import xml.etree.ElementTree as ET

tree = ET.parse("movie.xml")
root = tree.getroot()

# Create an empty set to keep track of which child tags have been
# printed to avoid printing the same tag multiple times.
printed_tags = set()

print("Child tags of movie element:")
for movie in root.iter("movie"):
    for child in movie:
        child_tag = child.tag

        # The if statement ensures each child tag
        # is printed only once.
        if child_tag not in printed_tags:
            print(child_tag)
            printed_tags.add(child_tag)

print("\nMovie descriptions:")
for description in root.iter("description"):
    lines = description.text.splitlines()
    for line in lines:
        print(f"{line.strip()}")

# Initialise counts for True and False favourite movies
true_count = 0
false_count = 0

for movie in root.iter('movie'):
    # Check if 'favorite' attribute is present
    if 'favorite' in movie.attrib:
        value = movie.attrib['favorite']

        if value == "True":
            true_count += 1
        elif value == "False":
            false_count += 1

print("\nFavorite movies:", true_count)
print("Not favorite movies:", false_count)