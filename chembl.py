from chembl_webresource_client.new_client import new_client
import sys


def main():
    molecule = new_client.molecule

    mols = molecule.filter(pref_name__icontains='metformin').only('pref_name')
    print([m['pref_name'] for m in mols])

    return 0


if __name__ == '__main__':
    sys.exit(main())
