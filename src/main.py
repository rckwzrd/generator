from textnode import TextNode, TextType


def main():
    print("hello world")
    text_type = TextType.BOLD
    test = TextNode("test text", text_type, "test url")
    print(test)


if __name__ == "__main__":
    main()
