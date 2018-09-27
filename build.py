#The 'pages' list consists of dictionaries, each of which contains the elements for a full webpage.

pages = [
    {
        "filename": "content/about.html",
        "output": "docs/about.html",
        "title": "About Me",
    },
    {
        "filename": "content/contact.html",
        "output": "docs/contact.html",
        "title": "Contact Me",
    },
    {
        "filename": "content/stories.html",
        "output": "docs/stories.html",
        "title": "Stories",
    },
    {
        "filename": "content/belgium.html",
        "output": "docs/belgium.html",
        "title": "Belgium",
    },
    {
        "filename": "content/bhutan.html",
        "output": "docs/bhutan.html",
        "title": "Bhutan",
    },
    {
        "filename": "content/egypt.html",
        "output": "docs/egypt.html",
        "title": "Egypt",
    },
    {
        "filename": "content/india.html",
        "output": "docs/india.html",
        "title": "India",
    },
    {
        "filename": "content/ireland.html",
        "output": "docs/ireland.html",
        "title": "Ireland",
    },
    {
        "filename": "content/slovenia.html",
        "output": "docs/slovenia.html",
        "title": "Slovenia",
    },
    {
        "filename": "content/spain.html",
        "output": "docs/spain.html",
        "title": "Spain",
    },
    {
        "filename": "content/uzbekistan.html",
        "output": "docs/uzbekistan.html",
        "title": "Uzbekistan",
    },
    {
        "filename": "content/vietnam.html",
        "output": "docs/vietnam.html",
        "title": "Vietnam",
    },
]     
        
#The page_create function concatenates the dictionary items to create each webpage.        
        
def page_create():
    for item in pages:
        top = open("templates/top.html").read()
        content = open(item["filename"]).read()
        fullpage = top + content
        open(item["output"], "w+").write(fullpage)
page_create()


#The title_replace function is supposed to replace the titles but I ran out of time.

def title_replace():
    for item in pages:
       old_title = (item["output"])
       new_title = (item["title"])
       replace = (new_title.replace("{{title}}", new_title))
       open("new_title", "w+").write(new_title)
title_replace()
















