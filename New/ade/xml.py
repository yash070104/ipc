from lxml import etree
from tabulate import tabulate

def print_nodes(node, path):
    try:
        nodes = node.xpath(path)
    except Exception as e:
        print("Error:", e)
        return []

    result = []
    for actual_node in nodes:
        result.append([actual_node.tag, actual_node.text])

    return result

def main():
    # Load XML file
    try:
        doc = etree.parse("C:/Users/Yash/Desktop/ade/politics.xml")
    except IOError:
        print("Failed to load XML file.")
        return 1

    # Collect nodes based on path expressions
    president_nodes = print_nodes(doc, "//Country/President")
    pm_nodes = print_nodes(doc, "//Country/PrimeMinister")
    chancellor_nodes = print_nodes(doc, "//Country/Chancellor")
    vp_nodes = print_nodes(doc, "//Country/VicePresident")
    party_nodes = print_nodes(doc, "//Country/PoliticalParty")
    

    # Display nodes in a table format
    print("\nTable for Nodes:")
    headers = ["Tag", "Text"]
    all_nodes = president_nodes + pm_nodes + chancellor_nodes + vp_nodes + party_nodes
    print(tabulate(all_nodes, headers=headers, tablefmt="grid"))

    return 0

if __name__ == "__main__":
    main()
