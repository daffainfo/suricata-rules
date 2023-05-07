import os
import sys
import getopt

def merge_rules_files(output_path):
    rules_files = []
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(".rules"):
                rules_files.append(os.path.join(root, file))

    merged_content = ''
    for filename in rules_files:
        with open(filename, 'r') as f:
            for line in f:
                merged_content += line.rstrip('\n') + '\n'

    with open(output_path, 'w') as f:
        f.write(merged_content)

    print(f"Successfully merged {len(rules_files)} rules files into {output_path}")

def main(argv):
    path = ''
    try:
        opts, args = getopt.getopt(argv,"hp:",["path="])
    except getopt.GetoptError:
        print('main.py -p <outputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('main.py -p <outputfile>')
            sys.exit()
        elif opt in ("-p", "--path"):
            merge_rules_files(arg)
    if not opts:
        print('main.py -p <outputfile>')
        sys.exit()


if __name__ == "__main__":
    main(sys.argv[1:])
