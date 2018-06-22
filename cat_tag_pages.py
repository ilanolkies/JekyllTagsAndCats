import glob
import os

post_dir = '_posts/' # Jekyll default posts folder
cat_dir = 'category/' # Category pages destination
tag_dir = 'tag/' # Tag pages destination

filenames = glob.glob(post_dir + '*md') # Files with Markdown Extension

cats = [] # Category list
tags = [] # Tag list

# Find tags and categories in all posts and add them to the respective lists
for filename in filenames:
    f = open(filename, 'r')
    crawl = False
    cat_generated = False
    tags_generated = False

    # Search all post headers
    # Stop when category and tags are added or --- is reached
    for line in f:
        stripped_line = line.strip()
        if crawl:
            current_header = stripped_line.split()

            if current_header[0] == 'category:':
                cats.extend(current_header[1:])
                cat_generated = True
            elif current_header[0] == 'tags:':
                tags.extend(current_header[1:])
                tags_generated = True

        if cat_generated and tags_generated:
            break

        if stripped_line == '---':
            if not crawl:
                crawl = True
            else:
                crawl = False
                break
    f.close()

# Remove repeated
cats = set(cats)
tags = set(tags)

# Remove old caeogry pages
old_cats = glob.glob(cat_dir + '*.md')
for cat in old_cats:
    os.remove(cat)

# Create cateogry directory
if not os.path.exists(cat_dir):
    os.makedirs(cat_dir)

# Generate category pages
for cat in cats:
    cat_filename = cat_dir + cat + '.md'
    f = open(cat_filename, 'a')
    write_str = ("---\n"
        "layout: category\n"
        "title: \"Category: " + cat + "\"\n"
        "category: " + cat + "\n"
        "---\n")
    f.write(write_str)
    f.close()
print("Category pages generated: " + str(cats.__len__()))

# Remove old tag pages
old_tags = glob.glob(tag_dir + '*.md') 
for tag in old_tags:
    os.remove(tag)

# Create tag directory
if not os.path.exists(tag_dir):
    os.makedirs(tag_dir)

# Generate tag pages
for tag in tags:
    tag_filename = tag_dir + tag + '.md'
    f = open(tag_filename, 'a')
    write_str = ("---\n"
        "layout: tag\n"
        "title: \"Tag: " + tag + "\"\n"
        "tag: " + tag + "\n"
        "---\n")
    f.write(write_str)
    f.close()
print("Tag pages generated: " + str(tags.__len__()))
