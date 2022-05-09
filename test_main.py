import main

def test_main(text="hello_world"):
    assert "hello_world" == main.hello_world(text)
