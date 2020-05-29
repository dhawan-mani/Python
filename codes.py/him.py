print("HELLO to HIM.py")

def run_during_import():
    print("RUN DURING IMPORT")
def run_when_standalone():
    print("RUN WHEN STANDALONE")
# def main():
#     print("CALLED during main")
#     # var = input("enter the binary")[::-1]
#     # print(__name__)
#     # result = 0
#     # index = 0
#     # for x in var:
#     #     if x == '1':
#     #         result = result + 2**index
#     #     index = index + 1
#     # print(result)

if __name__ == "__main__":
    run_when_standalone()
if __name__ == "him":
    run_during_import()
