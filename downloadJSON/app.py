import json
import requests

def main():
    for x in range(1, 1501):
        print(x)
        # res = requests.get("https://opensea.mypinata.cloud/ipfs/QmYUosvwotwwWjDYYsTXaK1yKgUTsC7eQj8Stusy6fEE2B/" + str(x))
        res = {"name":"Alpha Fox Club","image":"https://connor.mypinata.cloud/ipfs/QmdDkRFz2SHDPh5YhqwPKFxV5RrZhrJqvbN6mcKLR6ghqw"}
        json_str = json.dumps(res)
        with open("output1/" + str(x), 'w') as f:
            f.write(json_str)

main()