my_skillz = [
    "lua",
    "aws",
    "css",
    "debian",
    "django",
    "docker",
    "fastapi",
    "git",
    "github",
    "linux",
    "py",
    "sqlite",
    "js",
    "vercel",
    "vscode",
    "ableton",
]

skills = ",".join(my_skillz)
url = "https://skillicons.dev"
perline = 8

skills_str = f"[![Skills]({url}/icons?i={skills}&perline={perline})]({url})"
top_langs = "https://github-readme-stats.vercel.app/api/top-langs/?username=edward-jazzhands&layout=compact&theme=radical"

bio = """\
Python enthusiast, web developer, expert in the Textual framework for Python.\n
I have written and maintain several libraries for Textual.

[https://edward-jazzhands.github.io/](https://edward-jazzhands.github.io/)
"""
endquote  = """\
> *"Programming is the art of building machines out of ideas."*  
> *- Edward Jazzhands*
"""

with open("README.md", "w") as f:
    f.write(f"{bio}\n")
    f.write(f"{skills_str}\n\n")
    f.write(f"![Top Langs]({top_langs})\n")
    f.write(f"{endquote}")
