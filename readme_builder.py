my_skillz = [
    "astro",
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
    "ts",
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
"Programming is the art of building machines out of ideas." - Edward Jazzhands

Python enthusiast, web developer, expert in the Textual framework for Python. I have written and \
maintain several libraries for Textual.

Libraries: [http://www.github.com/edward-jazzhands/libraries](http://www.github.com/edward-jazzhands/libraries)

Blog: [https://edward-jazzhands.github.io/](https://edward-jazzhands.github.io/)
"""

with open("README.md", "w") as f:
    f.write(f"{bio}\n")
    f.write(f"{skills_str}\n\n")
    f.write(f"![Top Langs]({top_langs})\n")