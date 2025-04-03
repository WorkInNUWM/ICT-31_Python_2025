def hello():
    print("Hello, world!")

def hello_by_name(name:str):
    print(f"Hello, {name}!")


def suma(a:int,b:int)->int:
    """
    @a parametr
    @b parametr
    output suma @a+@b 
    """
    print(f"{a}+{b}={a+b}")

if __name__=="__main__":
    hello()
    hello_by_name("Tetiana")
    suma(2,3)
