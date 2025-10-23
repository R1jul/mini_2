import argparse

def greet(name :str) :
    return f"Hey wassup,{name}"





def main():
    parser = argparse.ArgumentParser(description="For my mini project")
    parser.add_argument("name")
    args = parser.parse_args()
    print(greet(args.name))
  
  
  
  
    
if __name__ == "__main__":
    main()
