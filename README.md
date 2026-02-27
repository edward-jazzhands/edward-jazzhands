[![Skills](https://skillicons.dev/icons?i=docker,py,debian,css,js,astro,django,aws,fastapi,git,github,linux,sqlite,vercel,vscode,ableton&perline=8)](https://skillicons.dev)

Python expert, web developer, and open-source enthusiast.

I have written and maintain two utility programs, a handful of Python libraries, and several plugins for the [Textual framework](https://textual.textualize.io/). I also write blog posts and tutorials on my website about a variety of topics, including Python, Linux, and hot takes on agentic development.

[https://edward-jazzhands.github.io/](https://edward-jazzhands.github.io/)

## Utility Programs

- [CLOCTUI](https://github.com/edward-jazzhands/cloctui) - A terminal-based tool (TUI) for counting lines of code in a directory and displaying the results in a pretty interactive table. It's a frontend for the `cloc` command line tool.
- [ezlogconsole](https://github.com/edward-jazzhands/ezlogconsole) - A modern, JSON-based logging console with an included logging handler for the Python standard library's `logging` module (Technically also a library, for the handler).
- [systemd-mount-manager (IN PROGRESS)](https://github.com/edward-jazzhands/systemd-mount-manager) - A terminal-based tool (TUI) for managing systemd mount units (The successor to /etc/fstab)

## Python Libraries

- [ezpubsub](https://github.com/edward-jazzhands/ezpubsub) - A publish-subscribe library for Python that's modern, thread-safe, supports sync and async equally, strongly typed, and has an ultra-simple API. I built this because I scoured the internet and couldn't find another one that I thought was suitable for modern Python.
- [ezlogconsole](https://github.com/edward-jazzhands/ezlogconsole) - See above. The handler can be added into projects as a dependency, or you can just copy paste the code for the handler if you don't want to add it as a project dependency.
- [rich-pyfiglet](https://github.com/edward-jazzhands/rich-pyfiglet) - A Python library for generating color ASCII text banners by combining the [rich](https://github.com/Textualize/rich) library with the [pyfiglet](https://github.com/pwaller/pyfiglet) library.

## Plugins for Textual

- [textual-pyfiglet](https://github.com/edward-jazzhands/textual-pyfiglet) - Adds a `Figlet` widget that creates colorized, animating ASCII text banners using the [pyfiglet](https://github.com/pwaller/pyfiglet) library combined with Textual's animation system.
- [textual-coloromatic](https://github.com/edward-jazzhands/textual-coloromatic) - Adds a `Coloromatic` widget which can add color animations to ASCII art.
- [textual-slidecontainer](https://github.com/edward-jazzhands/textual-slidecontainer) - Adds a `SlideContainer` widget which slides in and out of view.
- [textual-window](https://github.com/ttygroup/textual-window) - Adds a `Window` widget which can be used to create modal, desktop-like windows that can be minimized or dragged around the screen with the mouse.