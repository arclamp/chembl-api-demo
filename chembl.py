import requests
import sys


def main():
    chembl_api = 'https://www.ebi.ac.uk/chembl/api/data'
    s = requests.Session()

    drug_name = 'metformin'

    params = {
        'q': drug_name,
        'pref_name__icontains': drug_name,
    }

    resp = s.get(f'{chembl_api}/molecule/search.json', params=params)
    data = resp.json()

    print([d['pref_name'] for d in data['molecules']])

    return 0


if __name__ == '__main__':
    sys.exit(main())
