from pathlib import Path

current_path = Path(".").absolute()


def output(depth: int, content: str):
    print("  "*depth + content)


def process_path(path: Path, depth: int = 0):
    for dir in reversed([d for d in path.iterdir() if d.is_dir()]):
        if depth == 0:
            output(depth + 1, "<h2>" + dir.name + "</h2>")
        else:
            output(depth + 1, "<li><button onClick=\"document.getElementById('frame').src = '/" + str(dir.relative_to(".")) + "';\">" + dir.name + "</button></li>")
        output(depth, "<ul>")
        process_path(dir, depth + 1)
        output(depth, "</ul>")


def main():
    print("<!DOCTYPE html>")
    print("<head>")
    print("<title>V2Ray Protobuf Documentation</title>")
    print("""<style>
    * {box-sizing: border-box; list-style: circle;}
    div {height: 100%;}
    button {}
    .container  {display: table; width: 100%; height: 100%;}
    .left-half  {position: absolute; left:  0px; width: 20%; border-right: 1px solid grey; overflow-y: scroll; margin-left: 10px; margin-right: 10px;}
    .right-half {position: absolute; right: 0px; width: 80%;}
    iframe {width: 100%; height: 100%; border: none; margin-left: 20px}
    </style>
    """)

    print("</head>")
    print("<body class\"container\" style=\"overflow-x: hidden; overflow-y: hidden\">")
    print("<div class=\"left-half\">")
    print("<li><button onClick=\"document.getElementById('frame').src = '/main.html';\">V2Ray Root</button></li>")
    process_path(Path("."))
    print("</div>")
    print("<div class=\"right-half\">")
    print('<iframe id="frame" src="main.html"></iframe>')
    print("</div>")
    print("</body>")
    print("</html>")
    pass


if __name__ == "__main__":
    main()
